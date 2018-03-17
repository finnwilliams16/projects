from matplotlib import pyplot as plt
import random, math

plt.title("Word Difficulty")
plt.ylabel("Vowels")
plt.xlabel("Letters")

def euclideandis(x, y, a, b):   
    return math.sqrt((x-a)**2 + (x-a)**2)

x = [[9, 4], [4, 1], [9, 4], [4, 1], [7, 4], [11, 5], [10, 3], [10, 3], [4, 2], [10, 4], [5, 2],
    [7, 2], [7, 2], [10, 5], [11, 5], [10, 4], [9, 5], [9, 3], [2, 1], [6, 4], [8, 4], [8, 4],
    [6, 2], [11, 5], [12, 5], [6, 0], [11, 5], [9, 4], [5, 1], [4, 1], [4, 2], [11, 5], [7, 4],
    [4, 2], [9, 4], [8, 2], [8, 4], [10, 4], [4, 1], [10, 4], [6, 4], [11, 5], [4, 1], [5, 2],
    [8, 2], [8, 4], [10, 2], [10, 4]]

centroid1 = [random.uniform(1, 11), random.uniform(1, 11)]   
centroid2 = [random.uniform(1, 11), random.uniform(1, 11)] 
centroid3 = [random.uniform(1, 11), random.uniform(1, 11)]

for j in xrange(100000):   
    cluster1 = []       
    cluster2 = []
    cluster3 = []
    for item in x:
        temp1 = euclideandis(item[0], item[1], centroid1[0], centroid1[1])
        temp2 = euclideandis(item[0], item[1], centroid2[0], centroid2[1])
        temp3 = euclideandis(item[0], item[1], centroid3[0], centroid3[1]) 
        if min(temp1, temp2, temp3) == temp1:
            cluster1.append([item[0], item[1]])
        elif min(temp1, temp2, temp3) == temp2:
            cluster2.append([item[0], item[1]])
        elif min(temp1, temp2, temp3) == temp3:
            cluster3.append([item[0], item[1]])
    iterable = 0
    for item in cluster1:
        iterable = iterable + item[0]
    if len(cluster1) > 0:
        centroid1[0] = iterable/len(cluster1) 
    iterable = 0
    for item in cluster1:
        iterable = iterable + item[1]
    if len(cluster1) > 0:
        centroid1[1] = iterable/len(cluster1)   
    iterable = 0
    for item in cluster2:
        iterable = iterable + item[0]
    if len(cluster2) > 0:
        centroid2[0] = iterable/len(cluster2)
    iterable = 0
    for item in cluster2:
        iterable = iterable + item[1]
    if len(cluster2) > 0:
        centroid2[1] = iterable/len(cluster2)
    iterable = 0
    for item in cluster3:
        iterable = iterable + item[0]
    if len(cluster3) > 0:
        centroid3[0] = iterable/len(cluster3)
    iterable = 0
    for item in cluster3:
        iterable = iterable + item[1]
    if len(cluster3) > 0:
        centroid3[1] = iterable/len(cluster3)

for item in cluster1:
    plt.scatter(item[0], item[1], color = "red") 
for item in cluster2:
    plt.scatter(item[0], item[1], color = "lime")
for item in cluster3:
    plt.scatter(item[0], item[1], color = "cyan") 


print(centroid1, centroid2, centroid3)
                 
plt.scatter(centroid1[0], centroid1[1], color = "maroon") 
plt.scatter(centroid2[0], centroid2[1], color = "green")
plt.scatter(centroid3[0], centroid3[1], color = "blue")
plt.show()
