from CementStrength.utils import load_model,save_json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from CementStrength.entity import EvaluationConfig
from CementStrength import logger
from pathlib import Path
import os

class Evaluation:

    def __init__(self,config: EvaluationConfig):
        self.config = config

    def evaluate(self):
        logger.info("Evaluation started")
        X_test = pd.read_csv(os.path.join(self.config.test_data,'test_data_features.csv'))
        y_test = pd.read_csv(os.path.join(self.config.test_data,'test_data_labels.csv'))
        scaler = StandardScaler()
        X_test_scaled = pd.DataFrame(scaler.fit_transform(X_test),columns=X_test.columns,index=X_test.index)
        cluster_model = load_model('cluster_model',os.path.join('Training','models'))
        prediction_cluster_model = cluster_model.predict(X_test_scaled)
        X_test_scaled['cluster'] = pd.Series(prediction_cluster_model, index=X_test_scaled.index) #cluster column added
        dfs=[X_test_scaled[X_test_scaled['cluster']==i] for i in range(len(set(prediction_cluster_model)))]
        for i in range(len(dfs)):
            dfs[i] = dfs[i].drop(columns='cluster')
        y_clusterwise = [y_test.loc[dfs[i].index] for i in range(len(dfs))]
        cluster0_model = load_model('random_model_cluster0',os.path.join('Training','models'))
        cluster1_model = load_model('random_model_cluster1',os.path.join('Training','models'))
        cluster2_model = load_model('random_model_cluster2',os.path.join('Training','models'))
        cluster3_model = load_model('random_model_cluster3',os.path.join('Training','models'))
        prediction_cluster_0 = cluster0_model.predict(dfs[0])
        score_cluster_0 = r2_score(y_clusterwise[0],prediction_cluster_0)
        prediction_cluster_1 = cluster1_model.predict(dfs[1])
        score_cluster_1 = r2_score(y_clusterwise[1],prediction_cluster_1)
        prediction_cluster_2 = cluster2_model.predict(dfs[2])
        score_cluster_2 = r2_score(y_clusterwise[2],prediction_cluster_2)
        prediction_cluster_3 = cluster3_model.predict(dfs[3])
        score_cluster_3 = r2_score(y_clusterwise[3],prediction_cluster_3)
        scores = {'r2_score0':score_cluster_0,'r2_score1':score_cluster_1,'r2_score2':score_cluster_2,'r2_score3':score_cluster_3}
        save_json(path=Path("scores.json"),data=scores)
        logger.info("scores saved")