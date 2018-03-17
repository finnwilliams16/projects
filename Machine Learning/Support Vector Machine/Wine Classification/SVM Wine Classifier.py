import numpy as np
from matplotlib import pyplot as plt
    
path = r'C:\Users\Finn Williams\Documents\Machine Learning\Support Vector Machine\Wine Classification\2 Wines.csv'
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int32)

m = len(data)
fm = len(data.T)

x1 = []
x2 = []
SVs = []

for i in range(m):
    if data[i][0] == 1:
        x1.append(data[i])
    elif data[i][0] == 2:
        x2.append(data[i])
