import numpy as np

x = np.array([
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,1]])

y = np.array([
    [0,1,1,0]]).T

w = 2 * np.random.random((3, 4)) - 1
w2 = 2 * np.random.random((4, 1)) - 1

for j in xrange(10):
    for j in xrange(10000):
        a2 = 1/(1+np.exp(-(np.dot(x, w))))
        a3 = 1/(1+np.exp(-(np.dot(a2, w2))))
        a3_delta = (y - a3) * (a3 * (1 - a3))
        a2_delta = a3_delta.dot(w2.T) * (a2 * (1 - a2))
        w2 += a2.T.dot(a3_delta)
        w += x.T.dot(a2_delta)
    print(a3)

