import os
import pickle
from mlflow.tracking import MlflowClient
import mlflow
from flask import Flask, request, jsonify
import numpy as np

MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
#RUN_ID = os.getenv('RUN_ID')
RUN_ID = '888e5d3c7a154c0f96f3f989304dc744' #copy paste your run id from mlflow ui
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)

with open('models/pipeline.bin', 'rb') as f_out:
    model = pickle.load(f_out)

def predict(data):
    preds = model.predict(data)
    return float(preds[0])


app = Flask('Blaqs_Bodyfat_Prediction_App_Service')
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()

    pred = predict(data)

    result = {
        'Body Fat estimation': round(pred,2)  ,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
