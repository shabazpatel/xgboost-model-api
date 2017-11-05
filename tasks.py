import re
import numpy as np
import pandas as pd
import math
import cPickle
import os
import pickle
import xgboost as xgb
import sys
from celery_init import celery_app

@celery_app.task(bind=True, soft_time_limit=1000)
def add(self, params):
    return params['a'] + params['b']

@celery_app.task(bind=True, soft_time_limit=1000)
def predict(self, params):
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

