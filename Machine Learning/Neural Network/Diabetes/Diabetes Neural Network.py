import numpy as np
path = "C:\Users\Finn Williams\Documents\Machine Learning\Neural Networks\Diabetes\Diabetes Training.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int32)

x = np.array(data[:, [0, 1, 2, 3, 4, 5, 6, 7]])
y = (data[:, -1])
y = np.array([y]).T

w = np.random.random((8, 9))
w2 = np.random.random((9, 9))
w3 = np.random.random((9, 1))

for j in xrange(50000):
    a2 = 1/(1 + np.exp(-( (np.dot(x, w) + 1) )))
    a3 = 1/(1 + np.exp(-( (np.dot(a2, w2) + 1) )))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 1)))

    a4delta = (y - a4) 
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))

    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)   

score = 0

for i in range(len(y)):
    if round(a4[i]) == y[i]:
        score = score
    else:
        score = score + 1

print(score)
