import numpy as np
x = np.array([[0], [0.5], [1]])
y = np.array([[0, 3/8, 1]]).T
w = np.random.random((1, 1))

for j in xrange(100000): 
    a2 = 1/(1 + np.exp(-(np.dot(x, w) + 1)))
    delta = (y - a2) * (a2 * (1 - a2))
    w += x.T.dot(delta)

print(a2 * 8 + 1)

