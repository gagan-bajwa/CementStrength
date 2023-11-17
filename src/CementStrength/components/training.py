from CementStrength.entity import TrainingConfig
from CementStrength import logger
from CementStrength.utils import read_yaml,create_directories,save_model,load_model
import shutil
import pandas as pd
from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os



class Training:
    def __init__(self,config: TrainingConfig):
        self.config = config
         
        create_directories(self.config.preprocessed_data_dir)
        create_directories(self.config.Models_dir)
        create_directories(self.config.images)
        create_directories(self.config.test_data)

    def copy_training_file(self):
        create_directories(self.config.training_dir)
        shutil.copy(self.config.source_dir,self.config.local_training_file)
        logger.info("file copied")

    def preprocessing(self):
        df = pd.read_csv(self.config.local_training_file)
        df = df.drop(columns='Unnamed: 0')
        if df.isnull().values.any():
            for column in df.columns:
                if df[column].dtype == 'int64'or df[column].dtype == 'float64':
                    df[column] = df[column].fillna(df[column].mean())
                else:
                    df[column] = df[column].fillna(df[column].mode())
        # removing outliers
        Q1 = df.quantile(.25)
        Q3 = df.quantile(.75)
        IQR = Q3-Q1
        df = df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR))).any(axis=1)]
        for column in df.columns:
            df[column] += 1
            df[column] = np.log(df[column])
        fig= plt.figure(figsize=(10,10))
        sns.boxplot(df)
        plt.xticks(rotation=90)
        plt.title("Data after outlier correction")
        plt.savefig(self.config.images+'/'+'after_outlier.png', format="png")
        plt.close(fig=fig)
        fig= plt.figure(figsize=(8,8))
        sns.heatmap(df.corr(),annot=True,cmap="Spectral_r")
        plt.savefig(self.config.images+'/'+'heatmap.png', format="png")
        plt.close(fig=fig)
        logger.info("Data cleaned")
        return df.to_csv(self.config.preprocessed_data,index=False)
                
    def clustering(self):
        df = pd.read_csv(self.config.preprocessed_data)
        X = df.drop(columns='Concrete_compressive _strength')
        y = df['Concrete_compressive _strength']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        X_test.to_csv(os.path.join(self.config.test_data,'test_data_features.csv'),index=False)
        y_test.to_csv(os.path.join(self.config.test_data,'test_data_labels.csv'),index=False)
        #X_valid,X_test,y_valid,y_test = train_test_split(X_test,y_test,test_size=0.5,random_state=42)

        scaler = StandardScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X_train),columns=X_train.columns,index=X_train.index)
        
        
        inertia = []
        K = range(1,11)
        for k in K:
            km = KMeans(n_clusters=k)
            km = km.fit(X_scaled.values)
            inertia.append(km.inertia_)
        fig = plt.plot(K, inertia, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.savefig(self.config.images+'/'+'elbow_method_K.png')
        plt.close()
        
        kl = KneeLocator(range(1, 11), inertia, curve="convex", direction="decreasing")
        no_of_clusters = kl.elbow
        cluster_model = KMeans(n_clusters=no_of_clusters,init="k-means++",random_state=42).fit(X_scaled.values)
        save_model(cluster_model,self.config.Models_dir,'cluster_model')

        clusters_train = cluster_model.predict(X_scaled.values)
        #clusters_valid = cluster_model.predict(X_valid_scaled.values)
        #clusters_test = cluster_model.predict(X_test_scaled.values)
        X_scaled['cluster'] = pd.Series(clusters_train, index=X_scaled.index) #cluster column added
        dfs=[X_scaled[X_scaled['cluster']==i] for i in range(no_of_clusters)]
        y_cluster = [y_train.loc[dfs[i].index] for i in range(len(dfs))]
        new_dfs = []
        for i in range(len(dfs)):
            dfs[i]['Concrete Compressive strength'] = y_cluster[i] 
            new_dfs.append(dfs[i])
        for i in range(len(new_dfs)):
            new_dfs[i].to_csv(self.config.preprocessed_data_dir+'/'+'cluster'+str(i)+'.csv',index=False)
        logger.info('Data divided into clusters')    

    def regressor(self):
        logger.info('Building models for all clusters')
        models = []
        for i,cluster in enumerate(os.listdir(self.config.preprocessed_data_dir)):
            df = pd.read_csv(os.path.join(self.config.preprocessed_data_dir,cluster))
            df = df.drop(columns='cluster')
            X = df.drop(columns='Concrete Compressive strength')
            y = df['Concrete Compressive strength']
            #X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
            
            rm = RandomForestRegressor(random_state=42)
            params = { 'n_estimators': [50,100,150],'criterion':['squared_error','absolute_error','friedman_mse','poisson']}
            grid = GridSearchCV(estimator=rm,param_grid=params)
            grid.fit(X, y)
            random_model = RandomForestRegressor(criterion=grid.best_params_['criterion'],n_estimators=grid.best_params_['n_estimators']).fit(X, y)
            save_model(random_model,self.config.Models_dir,'random_model_cluster'+str(i))
            models.append(random_model)
        logger.info('models saved for every cluster')

