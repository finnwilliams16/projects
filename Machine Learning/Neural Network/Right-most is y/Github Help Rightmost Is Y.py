import numpy as np

x = np.array([
    [0,0,0,0],
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0],
    [0,0,1,1],
    [0,1,1,0],
    [1,1,0,0],
    [1,0,0,1],
    [1,0,0,1],
    [1,1,1,0],
    [1,1,0,1],
    [1,0,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ])

y = np.array([
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    ]).T

w = np.random.random((4, 5))
w2 = np.random.random((5, 5))
w3 = np.random.random((5, 1))

for j in range(10000):
    a2 = 1/(1 + np.exp(-(np.dot(x, w))))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3))))
    a4delta = (y - a4) * (a4 * (1 - a4))
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
    if (j% 1000) == 0:
        print ("Error:" + str(np.mean(np.abs(y - a4))))
    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)
print(a4)
