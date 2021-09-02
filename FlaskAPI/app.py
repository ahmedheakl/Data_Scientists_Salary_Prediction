import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np



app = Flask(__name__)

# Loading our saved model to predict the input vals
def load_model():
    path = './models/model_file.p'
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

# If we go to the route predict using a GET method,
# we run the predict function
@app.route('/predict', methods=['GET'])
def predict():
    
    # Getting the json respose sent via the GET method
    request_json = request.get_json()
    x = request_json['input']


    # The reshaping process is necessary for adding 
    # an extra dim which the model requires to predict the values
    x_input = np.array(x).reshape(1, -1)
    
    # Loading the model
    model = load_model()
    prediction = model.predict(x_input)[0]
    
    # Converting the prediction into a json response
    response = json.dumps({'response': prediction})
    return response, 200



if __name__ == '__main__':
    application.run(debug=True)