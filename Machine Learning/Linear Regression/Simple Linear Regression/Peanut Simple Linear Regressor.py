import numpy as np
x = np.array([[1], [2], [3]])
y = np.array([[1, 2, 3]]).T
w = np.random.random((3, 1))

for j in xrange(100000): 
    a2 = np.dot(x, w) + 1
    w += x.T.dot((y - a2))
