import numpy as np

def entropy(p, n):
    return (-p/(p+n)) * (np.log2(p/(p+n))) + (-n/(p+n)) * (np.log2(n/(p+n)))

data = np.array([
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0]]).T

m = len(data.T) + 0.0
x1 = np.sum(data[0]) + 0.0
x2 = np.sum(data[1]) + 0.0    # Adds up columns to get the amount of ones
x3 = np.sum(data[2]) + 0.0    # in each feature, and converts to float
y = np.sum(data[3]) + 0.0
yent = entropy((y/m), ((m-y)/m))

a = [0, 0]
b = [0, 0]

xwrty = [
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]],
    [[0, 0], [0, 0]]]

data = data.T

for j in xrange(int(m)):
    if data[j-1, 0] == 0:
        if data[j-1, 0] == data[j-1, 3]:
            xwrty[0][0][0] = xwrty[0][0][0] + 1
        elif data[j-1, 0] != data[j-1, 3]:
            xwrty[0][0][1] = xwrty[0][0][1] + 1
    elif data[j-1, 0] == 1:
        if data[j-1, 0] == data[j-1, 3]:
            xwrty[0][1][0] = xwrty[0][1][0] + 1
        elif data[j-1, 0] != data[j-1, 3]:
            xwrty[0][1][1] = xwrty[0][1][1] + 1




print(xwrty)
