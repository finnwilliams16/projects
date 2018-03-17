import numpy as np

def entropy(p, n):
    if p == 0 or n == 0:
        return 0
    else:
        return - p * np.log2(p) - n * np.log2(n)

data = np.array([
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0]]).T

m = len(data.T) + 0.0
'''x1 = np.sum(data[0]) + 0.0
x2 = np.sum(data[1]) + 0.0    # Adds up columns to get the amount of ones
x3 = np.sum(data[2]) + 0.0    # in each feature, and converts to float'''
y = np.sum(data[3]) + 0.0
yent = entropy((y/m), ((m-y)/m))

prop = [
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],   # One row for each x feature
    [[0, 0], [0, 0]]]

data = data.T

def buildProp(numFeatures, target, m, store):
    for j in xrange(m):
        if data[j-1, target] == 0:
            if data[j-1, target] == data[j-1, numFeatures-1]:           # Amount of features inc. y
                prop[store][0][0] = prop[store][0][0] + 1.0             # Target feature
            elif data[j-1, target] != data[j-1, numFeatures-1]:         # Tmount of training examples
                prop[store][0][1] = prop[store][0][1] + 1.0             # There to store the result in xwrty
        elif data[j-1, target] == 1:
            if data[j-1, target] == data[j-1, numFeatures-1]:
                prop[store][1][0] = prop[store][1][0] + 1.0
            elif data[j-1, target] != data[j-1, numFeatures-1]:
                prop[store][1][1] = prop[store][1][1] + 1.0

buildProp(4, 0, int(m), 0)
buildProp(4, 1, int(m), 1)
buildProp(4, 2, int(m), 2)

def calcGain(yent, feature, m):
    return yent - ((np.sum(prop[feature][0])/m) * entropy(prop[feature][0][0]/np.sum(prop[feature][0]), prop[feature][0][1]/np.sum(prop[feature][0])) + (np.sum(prop[feature][1])/m) * entropy(prop[feature][1][0]/np.sum(prop[feature][1]), prop[feature][1][1]/np.sum(prop[feature][1])))

gains = [calcGain(yent, 0, m), calcGain(yent, 1, m), calcGain(yent, 2, m)]
root = 






