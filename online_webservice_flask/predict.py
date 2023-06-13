import os
import pickle
from mlflow.tracking import MlflowClient
import mlflow
from flask import Flask, request, jsonify
import numpy as np


with open('pipeline.bin', 'rb') as f_out:
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
        'Body Fat estimation': round(pred,2)  
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
