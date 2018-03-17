import numpy as np
'''path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Pima Indians Diabetes.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",")'''

path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Heights And Weights.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int64)

m = len(data)
data = data.T
y = [np.sum(data[2])/m, (m - np.sum(data[2]))/m] # 1, 0

guassians = []

test = [51, 51]

def guassian(data, new):
    means = []
    variances = []
    for i in data:
        means.append(np.mean(i))
        variances.append(np.var(i))
    del means[-1], variances[-1]

    for i in range(len(new)):
        toappend = []
        for j in range(len(means)):
            const = 1/(np.sqrt(2 * np.pi * variances[j]))
            num = (new[i] - means[j])**2
            denom = 2 * variances[j]
            toappend.append(const * np.exp(-(num/denom)))
        guassians.append(toappend)
        
guassian(data, test)
print(guassians)
