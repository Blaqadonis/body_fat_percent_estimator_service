import requests
import numpy as np

data = {
    "Density": 1.0736,
    "Age": 70,
    "Weight": 134.25,
    "Height": 67.00,
    "Neck": 34.9,
    "Chest": 89.2,
    "Abdomen": 83.6,
    "Hip": 88.8,
    "Thigh": 49.6,
    "Knee": 34.8,
    "Ankle": 21.5,
    "Biceps": 25.6,
    "Forearm": 25.7,
    "Wrist": 18.5
}

# Reshape the dictionary into a 2D array
#data = np.array(list(data.values())).reshape(1, -1)

url = 'http://localhost:9696/predict'
response = requests.post(url, json=data)
print(response.json())
