import numpy as np
from matplotlib import pyplot as plt

# Length, Vowels

x = [
    [9, 4],
    [4, 1],
    [9, 4],
    [4, 1],
    [7, 4],
    [11, 5],
    [10, 3],
    [10, 3],
    [4, 2],
    [10, 4],
    [5, 2],
    [7, 2],
    [7, 2],
    [10, 5],
    [11, 5],
    [10, 4],
    [9, 5],
    [9, 3],
    [2, 1],
    [6, 4],
    [8, 4],
    [8, 4],
    [6, 2],
    [11, 5],
    [12, 5],
    [6, 0],
    [11, 5],
    [9, 4],
    [5, 1],
    [4, 1],
    [4, 2],
    [11, 5],
    [7, 4],
    [4, 2],
    [9, 4],
    [8, 2],
    [8, 4],
    [10, 4],
    [4, 1],
    [10, 4],
    [6, 4],
    [11, 5], 
    [4, 1],
    [5, 2],
    [8, 2],
    [8, 4],
    [10, 2],
    [10, 4]
    ]

y = [3, 1, 3, 1, 2, 3, 3, 2, 1, 2, 1, 3, 1, 2, 3, 2, 3, 1, 1, 2, 2, 2, 1, 3, 2, 3, 3, 2, 1, 1, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 3, 1, 1, 1, 2, 3, 3]

#-----------------------feature scaling--------------------------
for item in x:
    for i in item:
        item[0] = item[0]/12.0
        item[1] = item[1]/5.0

y[:] = [i/3.0 for i in y]

x = np.array(x)
y = np.array([y]).T
#-----------------------feature scaling--------------------------
        
w = np.random.random((2, 3))
w2 = np.random.random((3, 3))
w3 = np.random.random((3, 3))
w4 = np.random.random((3, 1))

matplotx = []
matploty = []

for j in xrange(100000):   
    a2 = 1/(1 + np.exp(-(np.dot(x, w) + 0)))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2) + 0)))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 0)))
    a5 = 1/(1 + np.exp(-(np.dot(a4, w4) + 0)))

    if j%50 == 0:
        matplotx.append(j)
        matploty.append((y[2]-a5[2]))

    a5delta = (y - a5) * (a5 * (1 - a5))
    a4delta = a5delta.dot(w4.T) * (a4 * (1 - a4))
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
    w4 += a4.T.dot(a5delta)
    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)

temp = a5
plotvar= []

for item in temp:
    for i in item:
        item[0] = item[0] * 3.0
        
for i in temp:
    plotvar.append(round(i))

'''print(temp)
print ("-------------------------")
print(plotvar)
print ("-------------------------")
print(w)
print ("-------------------------")
print(w2)
print ("-------------------------")
print(w3)
print ("-------------------------")
print(w4)'''


l = np.array(plotvar)
n = np.array([3, 1, 3, 1, 2, 3, 3, 2, 1, 2, 1, 3, 1, 2, 3, 2, 3, 1, 1, 2, 2, 2, 1, 3, 2, 3, 3, 2, 1, 1, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 3, 1, 1, 1, 2, 3, 3])
print(l-n)

plt.plot(matplotx, matploty)

print("hissssssssss")
print(a5)
print("hissssssssss")

print('a4: {} \n w4:{}'.format(a4.shape, w4.shape))
a5 = 1/(1 + np.exp(-(np.dot(a4, w4) + 1)))
print('a5:', a5.shape)

plt.show()
