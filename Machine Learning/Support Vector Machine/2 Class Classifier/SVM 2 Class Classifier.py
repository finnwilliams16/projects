import numpy as np
from matplotlib import pyplot as plt
path = r"C:\Users\Finn Williams\Documents\Machine Learning\Support Vector Machine\2 Class Classifier\2 Wines.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",")

def f(x):
    return x

x = [[1, 2],
               [2, 3],
               [2, 4],
               [3, 4], 
               [1, 3],
               [1, 2],
               [3, 1]],[[6, 5],
               [7, 6],
               [5, 7],
               [7, 6],
               [7, 7],
               [6, 8],
               [5, 5]]

tildeSVs = []
tildeSVs.append([x[0][3][0], x[0][3][1], 1]) # Repeat for m
tildeSVs.append([x[1][3][0], x[1][3][1], 1])

tildeSVs = np.array(tildeSVs)

boundaryN = tildeSVs[0].dot(tildeSVs[0]) + tildeSVs[1].dot(tildeSVs[0]) + 1
boundaryP = tildeSVs[0].dot(tildeSVs[1]) + tildeSVs[1].dot(tildeSVs[1]) - 1
print(boundaryN, boundaryP)

