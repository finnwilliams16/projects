import numpy as np

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


for item in x:
    for i in item:
        item[0] = item[0]/12.0
        item[1] = item[1]/5.0

y[:] = [i/3.0 for i in y]

x = np.array(x)
y = np.array([y]).T


np.random.seed(1)
w =  np.random.random((2, 3)) 
w2 =  np.random.random((3, 3)) 
w3 =  np.random.random((3, 3)) 
w4 =  np.random.random((3, 1)) 

for j in xrange(10000):   
    a2 = 1/(1 + np.exp(-(np.dot(x, w) + 0)))
    a3 = 1/(1 + np.exp(-(np.dot(a2, w2) + 0)))
    a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 0)))
    a5 = 1/(1 + np.exp(-(np.dot(a4, w4) + 0)))

    a5delta = (y - a5) * (a5 * (1 - a5)) * 0.7
    a4delta = a5delta.dot(w4.T) * (a3 * (1 - a3))
    a3delta = a4delta.dot(w3.T) * (a3 * (1 - a3))
    a2delta = a3delta.dot(w2.T) * (a2 * (1 - a2))
    w4 += a4.T.dot(a5delta)
    w3 += a3.T.dot(a4delta)
    w2 += a2.T.dot(a3delta)
    w += x.T.dot(a2delta)


disp = []
n = np.array([3, 1, 3, 1, 2, 3, 3, 2, 1, 2, 1, 3, 1, 2, 3, 2, 3, 1, 1, 2, 2, 2, 1, 3, 2, 3, 3, 2, 1, 1, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 3, 1, 1, 1, 2, 3, 3])


for i in a5:
    disp.append(round(i * 3))

print(disp)
disp = np.array([disp])
print(disp - n)

print("hgiughghjgjhjh")
print(w)
print("hgiughghjgjhjh")
print(w2)
print("hgiughghjgjhjh")
print(w3)
print("hgiughghjgjhjh")
print(w4)

x = np.array([
    [2, 1]])

a2 = 1/(1 + np.exp(-(np.dot(x, w) + 0)))
a3 = 1/(1 + np.exp(-(np.dot(a2, w2) + 0)))
a4 = 1/(1 + np.exp(-(np.dot(a3, w3) + 0)))
a5 = 1/(1 + np.exp(-(np.dot(a4, w4) + 0)))

disp = []
n = np.array([3, 1, 3, 1, 2, 3, 3, 2, 1, 2, 1, 3, 1, 2, 3, 2, 3, 1, 1, 2, 2, 2, 1, 3, 2, 3, 3, 2, 1, 1, 1, 3, 3, 1, 3, 2, 3, 3, 1, 2, 3, 3, 1, 1, 1, 2, 3, 3])


for i in a5:
    disp.append(round(i * 3))

print(disp)
