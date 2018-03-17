import numpy as np
x = np.array([[0]])
x2 = np.array([[1]])
y = np.array([[1]]).T
w = np.random.random((1, 1))

for j in xrange(100000): 
    a2 = 1/(1 + np.exp(-((np.dot(x, w) + np.dot(x2, w)) + 1)))
    delta = (y - a2) * (a2 * (1 - a2))
    w += x.T.dot(delta)
