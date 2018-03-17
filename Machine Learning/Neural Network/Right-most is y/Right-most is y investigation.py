from matplotlib import pyplot as plt, numpy as np

graphicalDataError = []
graphicalDataEpochs = []
print("0000 | 0\n0001 | 1\n0010 | 0\n0100 | 0\n1000 | 0\n0011 | 1\n0110 | 0\n1100 | 0\n1001 | 1\n1111 | 1\n\n0111 | ?\n1110 | ?")

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
    [1,1,1,1]
    ])

y = np.array([
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 1]
    ]).T

w = np.random.random((4, 5)) 
w2 = np.random.random((5, 5)) 
w3 = np.random.random((5, 1))

for j in xrange(50000):
    a2 = 1/(1 + np.exp(-( (np.dot(x, w) + 1) )))
    a3 = 1/(1 + np.exp(-( (np.dot(a2, w2) + 1) )))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 1)))
    
    graphicalDataError.append(np.mean(np.abs(y - a4)))
    graphicalDataEpochs.append(j)

    print(y.shape, a4.shape)
    
    a4delta = (y - a4) * (a4 * (1 - a4))
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))

    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)

print(a4)

x = [0, 1, 1, 1]
a2 = 1/(1 + np.exp(-( (np.dot(x, w) + 1) )))
a3 = 1/(1 + np.exp(-( (np.dot(a2, w2) + 1) )))
a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 1)))
print("\n0111:")
print(a4)

x = [1, 1, 1, 0]
a2 = 1/(1 + np.exp(-( (np.dot(x, w) + 1) )))
a3 = 1/(1 + np.exp(-( (np.dot(a2, w2) + 1) )))
a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 1)))
print("1110:")
print(a4)

plt.plot(graphicalDataError, graphicalDataEpochs)
plt.xlabel("Error")
plt.ylabel("Epochs")
data = [[]]
plt.show()
