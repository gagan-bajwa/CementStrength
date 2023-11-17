from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
from CementStrength.utils import load_model
import os

app = Flask(__name__)

# Load the pre-trained models
cluster_model = load_model('cluster_model',os.path.join('Training','models'))
cluster0_model = load_model('random_model_cluster0',os.path.join('Training','models'))
cluster1_model = load_model('random_model_cluster1',os.path.join('Training','models'))
cluster2_model = load_model('random_model_cluster2',os.path.join('Training','models'))
cluster3_model = load_model('random_model_cluster3',os.path.join('Training','models'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [
            float(request.form['cement']),
            float(request.form['blast_furnace_slag']),
            float(request.form['fly_ash']),
            float(request.form['water']),
            float(request.form['superplasticizer']),
            float(request.form['coarse_aggregate']),
            float(request.form['fine_aggregate']),
            float(request.form['age'])
        ]

        input_data = pd.DataFrame([features], columns=['Cement_component_1', 'Blast_Furnace_Slag_component_2',
                                                      'Fly_Ash_component_3', 'Water_component_4',
                                                      'Superplasticizer_component_5', 'Coarse_Aggregate_component_6',
                                                      'Fine_Aggregate_component_7', 'Age_day'])

        # Standardize the input data
        scaler = StandardScaler()
        input_scaled = scaler.fit_transform(input_data)

        # Predict the cluster
        cluster_prediction = cluster_model.predict(input_scaled)[0]

        # Choose the appropriate model based on the predicted cluster
        if cluster_prediction == 0:
            final_prediction = cluster0_model.predict(input_scaled)
        elif cluster_prediction == 1:
            final_prediction = cluster1_model.predict(input_scaled)
        elif cluster_prediction == 2:
            final_prediction = cluster2_model.predict(input_scaled)
        else:
            final_prediction = cluster3_model.predict(input_scaled)

        return render_template('result.html', prediction=final_prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
