import numpy as np

x = np.array([
    [2011.0, 1],     # [a, b, c], where a is the year, b is the rightmost digit of that year 
    [2012.0, 2],     # and c is the difference between the y values
    [2013.0, 3],
    [2014.0, 4],
    [2015.0, 5],
    [2016.0, 6]
    ])

y = np.array([
    [112.0, 113.0, 114.0, 114.0, 114.0, 114.0]
    ]).T

xmax = x.max(axis = 0)
ymax = y.max(axis = 0)

meanx = x / xmax
meany = y / ymax

w = np.random.random((2, 3))
w2 = np.random.random((3, 3))
w3 = np.random.random((3, 1))

for j in xrange(200000):
    a2 = 1/(1 + np.exp(-(np.dot(meanx, w))))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3))))
    a4delta = (meany - a4) * (a4 * (1 - a4))
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += meanx.T.dot(a2delta)

temp = a4 * y.max(axis = 0)
print(round(temp[0]), round(temp[1]), round(temp[2]), round(temp[3]), round(temp[4]), round(temp[5]))



x = [2017, 17]
meanx = x / xmax

a2 = 1/(1 + np.exp(-(np.dot(meanx, w))))
a3 = 1/(1 + np.exp(-(np.dot(a2, w2))))
a4 = 1/(1 + np.exp(-(np.dot(a3, w3))))

temp =  [i * xmax for i in a4]
print(temp)
