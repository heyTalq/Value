
from __future__ import division
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn import cross_validation, tree, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import xgboost
import math

data = pd.read_csv('kc_house_data.csv')

def MLthingy(q):
    
    import time

    start = time.time()
    
    count = float(0)
    aggregate = 0

    minEst = 0
    maxEst = 0
    
    xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                                   colsample_bytree=1, max_depth=7)
    new_data = data[['zipcode', 'sqft_living', 'sqft_lot','bedrooms', 'bathrooms','floors','waterfront', 'yr_built']]
        
    while count != 10:
        X = new_data.values
        y = data.price.values
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y ,test_size=0.1)
        #traindf, testdf = train_test_split(X_train, test_size = 0.3)
        xgb.fit(X_train,y_train)
        
        predictions = xgb.predict(q)
        #print(explained_variance_score(predictions,y_test))
        #print(X_test)
        #print(predictions)
        aggregate += float(predictions)
        count+= 1
        est = float(predictions)
        if minEst == 0:
                minEst = est
        elif est < minEst:
	        minEst = est
	
        if maxEst == 0:
                maxEst = est
        elif est > maxEst:
                maxEst = est
	
    end = time.time()
    outArr = [aggregate/count,minEst, maxEst]
    #print(end - start)
    
    return (outArr)

