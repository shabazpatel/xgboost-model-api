from __future__ import print_function # In python 2.7
import os
import subprocess
import json
import re
from flask import Flask, request, jsonify
from inspect import getmembers, ismethod
import numpy as np
import pandas as pd
import math
import cPickle
import os
import pickle
import xgboost as xgb
import sys


def add(params):
    return params['a'] + params['b']

def predict(params):
    model_filename = os.path.join(os.getcwd(), 'model.dat')
    # load model from file
    loaded_model = pickle.load(open(model_filename, "rb"))
    X = params 
    x_test = pd.DataFrame(X)
    x_test.sort_index(axis=1,inplace=True)
    #x_test = xgb.DMatrix(x_test)
    y_pred = loaded_model.predict(x_test)
    y_pred[y_pred > 0.5] = 1
    y_pred[y_pred <= 0.5] = 0
    return int(y_pred[0])

functions_list = [add, predict]

app = Flask(__name__)

@app.route('/<func_name>', methods=['POST'])
def api_root(func_name):
    for function in functions_list:
        if function.__name__ == func_name:
            try:
                json_req_data = request.get_json()
                if json_req_data:
                    res = function(json_req_data)
                else:
		    return jsonify({"error": "error in receiving the json input"})
            except Exception as e:
                return jsonify({"error": "error while running the function"})
            return jsonify({"result": res})
    output_string = 'function: %s not found' % func_name
    return jsonify({"error": output_string})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

