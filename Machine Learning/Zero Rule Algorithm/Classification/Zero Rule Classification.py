import numpy as np

data = [   # Made of Clear Glass, Handle, Tall, Is a Mug
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0]]

freq = []
counter = 0

for i in xrange(len(data[0])):
    for j in xrange(len(data)):
        counter = counter + data[j][i]
    freq.append(counter)
    counter = 0

