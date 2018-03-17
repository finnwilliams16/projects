import numpy as np

x = np.array([
    [1, 0, 0]])

y = np.array([
    [1]]).T

w = np.random.random((len(x[0]), len(y[0])))

for j in xrange(100000):
    a = 1/(1 + np.exp(-(np.dot(x, w) + 0.1)))
    adelta = (y - a) * (a * (1 - a))
    w += a.T.dot(adelta)

