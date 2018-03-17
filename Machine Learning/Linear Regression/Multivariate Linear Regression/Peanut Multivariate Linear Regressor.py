import numpy as np
x = np.array([[0.0], [0.33], [0.66], [1.0]])
x2 = np.array([[0.0], [0.33], [0.66], [1.0]])
y = np.array([[1.0, 2.0, 3.0, 4.0]]).T
w = np.random.random((1, 2))
sumx = np.concatenate((x, x2), axis = 1)

for j in xrange(1): 
    mx = np.dot(sumx, w.T)
    w += (sumx.T.dot((y - mx))).T
