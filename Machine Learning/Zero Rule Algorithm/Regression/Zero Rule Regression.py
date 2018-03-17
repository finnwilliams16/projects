import numpy as np

data = [   # Volume, Height, Slant Factor, Mug (1) or Glass (0)
    [923.4, 11.0, 1.5, 1],
    [506.25, 9.0, 0, 1],
    [570.775, 7.9, 0, 1],
    [310.96, 11.5, 0.5, 0],
    [830.875, 11.5, 0.5, 0],
    [522, 14.5, 0, 0]]

avg = []
counter = 0

for i in xrange(len(data[0])):
    for j in xrange(len(data)):         # Find avg of each column
        counter = counter + data[j][i]
    avg.append(counter/len(data))
    counter = 0
    
print(avg)
