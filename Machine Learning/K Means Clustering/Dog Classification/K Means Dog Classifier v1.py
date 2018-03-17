from matplotlib import pyplot as plt
import random, math

plt.title("Big Dogs and Small Dogs")
plt.ylabel("Height (cm)")
plt.xlabel("Weight (kg)")

def plotRandomCentroid(maxx, minx, maxy, miny): # Function to create a random centroid
    return [random.uniform(minx, maxx), random.uniform(miny, maxy)]

def euclideandis(x, y, a, b):
    return math.sqrt((x-a)**2 + (x-a)**2)



x = {5:31,
     3.2:19,
     4.6:32,        # Data- key = weight, value = height
     4:25,
     4.1:29,
     2.8:17,
     2.9:11}

centroid1 = [plotRandomCentroid(max(x.keys()), min(x.keys()), max(x.values()), min(x.values()))]
centroid2 = [plotRandomCentroid(max(x.keys()), min(x.keys()), max(x.values()), min(x.values()))]

for j in xrange(1):
    cluster1 = {}
    cluster2 = {}
    for key in x:
        temp1 = 0
        temp2 = 0
        temp1 = euclideandis(key, x[key], centroid1[0][0], centroid1[0][1]) # Dis betw point, red centroid
        temp2 = euclideandis(key, x[key], centroid2[0][0], centroid2[0][1]) # Dis betw point, green centroid
        if temp1 < temp2:
            cluster1[key] = x[key]
        else:
            cluster2[key] = x[key]

plt.scatter(cluster1.keys(), cluster1.values(), color = "red")
plt.scatter(cluster2.keys(), cluster2.values(), color = "lime")
plt.scatter(centroid1[0][0], centroid1[0][1], color = "maroon") 
plt.scatter(centroid2[0][0], centroid1[0][1], color = "green")
plt.show()
