import numpy as np

x = np.array([
    [1, 0],
    [1, 1],
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 0]
    ])

y = np.array([
    [0, 1, 0, 0, 1, 0]
    ]).T

w = np.random.random((2, 3))
w2 = np.random.random((3, 1))

for j in xrange(100000):
    a2 = 1/(1 + np.exp(-(np.dot(x, w))))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
    a3delta = (y - a3) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)

print(a3)

x = np.array([0, 1])
a2 = 1/(1 + np.exp(-(np.dot(x, w))))
a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))

print(a2, w2, a3)
