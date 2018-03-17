import numpy as np

x = np.array([
    [1, 0],
    [1, 1],
    [0, 0],
    [0, 1]
    ])

y = np.array([
    [0, 1, 0, 0]
    ]).T

w = np.random.random((2, 3))
w2 = np.random.random((3, 1))

def trainAndTest(subject1, subject2):
    global w, w2, x, y, p
    for j in xrange(100000):
        a2 = 1/(1 + np.exp(-(np.dot(x, w))))
        a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
        a3delta = (y - a3) * (a3 * (1 - a3))
        a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
        w2 += a2.T.dot(a3delta)
        w += x.T.dot(a2delta)

    testx = np.array([
        [subject1, subject2]])
    
    a2 = 1/(1 + np.exp(-(np.dot(testx, w))))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
    print(a3)
