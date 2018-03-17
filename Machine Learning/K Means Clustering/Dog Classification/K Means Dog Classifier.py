from matplotlib import pyplot as plt
import random, math

plt.title("Big Dogs and Small Dogs")
plt.ylabel("Height (cm)")
plt.xlabel("Weight (kg)")

def euclideandis(x, y, a, b):   # Formula for euclidean distance
    return math.sqrt((x-a)**2 + (y-b)**2)

x = {5:31,
     3.2:19,
     4.6:32,        # Data- key = weight, value = height
     4:25,
     4.1:29,
     2.8:17,
     2.9:11}

centroid1 = [[random.uniform(min(x.keys()), max(x.keys())), random.uniform(max(x.values()), min(x.values()))]]   # create random centroids
centroid2 = [[random.uniform(min(x.keys()), max(x.keys())), random.uniform(max(x.values()), min(x.values()))]]

for j in xrange(100000):   # keep updating colours, position of centroids
    cluster1 = {}       # Everything in cluster 1 is closest to the dark red spot, therefore gets included in this dict, and gets scattered in light red
    cluster2 = {}       # Everything in cluster 2 is closest to the dark green spot, therefore gets included in this dict, and gets scattered in light green
    for key in x:
        temp1 = 0       # works out euclidean distance for all data points in x, then compares them
        temp2 = 0
        temp1 = euclideandis(key, x[key], centroid1[0][0], centroid1[0][1]) # Dis betw data point, red centroid
        temp2 = euclideandis(key, x[key], centroid2[0][0], centroid2[0][1]) # Dis betw data point, green centroid
        if temp1 < temp2:
            cluster1[key] = x[key]      # if the euclidean distance between datapoint and red spot,
                                        # smaller than the euclidean distance between datapoint and green spot,
                                        # add the point to the red cluster, else add to green cluster
        else:
            cluster2[key] = x[key]
            
    centroid1 = [[0, 0]]        # Centroids reset as they will be changed  
    centroid2 = [[0, 0]]
    
    iterable = 0
    for key in cluster1:        # works out mean coordinates of each cluster and changes the centroids coordinates to this
        iterable = iterable + key
    centroid1[0][0] = iterable/len(cluster1)
    iterable = 0
    for key in cluster1:
        iterable = iterable + cluster1[key]
    centroid1[0][1] = iterable/len(cluster1)
    iterable = 0
    for key in cluster2:
        iterable = iterable + key
    centroid2[0][0] = iterable/len(cluster2)
    iterable = 0
    for key in cluster2:
        iterable = iterable + cluster2[key]
    centroid2[0][1] = iterable/len(cluster2)

plt.scatter(cluster1.keys(), cluster1.values(), color = "red")      # scatters everythning
plt.scatter(cluster2.keys(), cluster2.values(), color = "lime")
plt.scatter(centroid1[0][0], centroid1[0][1], color = "maroon") 
plt.scatter(centroid2[0][0], centroid2[0][1], color = "green")
plt.show()

