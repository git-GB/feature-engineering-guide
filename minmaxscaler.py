#Load Libraries
import numpy as np
from sklearn import preprocessing
import random
import matplotlib.pyplot as plt

#Creating a dataset
sales = np.array([[-200],[-10],[50],[1000],[15],[20],[30],[50],[100],[200],[10000],[-12000],[150000],[160000]])

# Create a scaler
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))

#Scale feature
scaled_sales = minmax_scale.fit_transform(sales)

#Show feature
scaled_sales
