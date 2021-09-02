import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np



app = Flask(__name__)

def load_model():
    path = './models/model_file.p'
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

@app.route('/predict', methods=['GET'])
def predict():
    request_json = request.get_json()
    x = request_json['input']


    # The reshaping process is necessary for adding 
    # an extra dim which the model requires to predict the values
    x_input = np.array(x).reshape(1, -1)
    
    # Loading the model
    model = load_model()
    prediction = model.predict(x_input)[0]
    response = json.dumps({'response': prediction})
    return response, 200



if __name__ == '__main__':
    application.run(debug=True)