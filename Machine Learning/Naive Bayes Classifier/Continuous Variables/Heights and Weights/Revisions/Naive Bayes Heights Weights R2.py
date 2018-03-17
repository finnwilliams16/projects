import numpy as np
'''path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Pima Indians Diabetes.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",")'''

path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Heights And Weights.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int64)

m = len(data)
class0 = []
class1 = []
for i in range(m):
    if data[i][len(data[i])-1] == 0:
        class0.append(data[i])
    else:
        class1.append(data[i])

print(class0, class1)
    
data = data.T
prior_y = [np.sum(data[2])/m, (m - np.sum(data[2]))/m] # 1, 0

guassians = [[], []] # 1, 0

test = [51, 51]

def guassian(data, new):
    means = []
    variances = []
    for i in data:
        means.append(np.mean(i))
        variances.append(np.var(i))
    del means[-1], variances[-1]

    for i in range(2): # Binary classes
        toappend = []
        for j in range(len(new)):
            const = 1/(np.sqrt(2 * np.pi * variances[i]))
            num = (new[j] - means[i])**2
            denom = 2 * variances[i]
            toappend.append(const * np.exp(-(num/denom)))
        guassians.append(toappend)
        
guassian(data, test)

