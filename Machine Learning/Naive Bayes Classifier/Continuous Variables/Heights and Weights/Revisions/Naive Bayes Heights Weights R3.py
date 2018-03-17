import numpy as np
path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Heights And Weights.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int64)
m = len(data)
fm = len(data.T)
variances = [[], [], [], []] # 0x1, 0x2, 1x1...
means = [[], [], [], []] # 0x1, 0x2, 1x1...
gaussians = [[], []] # 2 gaussians made from n features
                     # 0, 1
                     
newcase = [51, 51]

for i in range(len(data)):
    if data[i][fm-1] == 0:      # Builds means/variances for each feature/y class
        variances[0].append(data[i][0])
        variances[1].append(data[i][1])
        means[0].append(data[i][0])
        means[1].append(data[i][1])
    else:
        variances[2].append(data[i][0])
        variances[3].append(data[i][1])
        means[2].append(data[i][0])
        means[3].append(data[i][1])

for i in range(len(variances)):
    variances[i] = np.var(variances[i])
    means[i] = np.mean(means[i])

prior_y = [(m-(np.sum(data.T[fm-1])) + 0.0)/m, (np.sum(data.T[fm-1]) + 0.0)/m] # 0, 1

def constGauss(x, vari, mean):
    const = 1/(np.sqrt(2 * np.pi * vari))
    num = (x - mean)**2
    denom = 2 * vari
    return const * np.exp(-(num/denom))

for i in range(len(means)/2):
    gaussians[0].append(constGauss(newcase[i], variances[i], means[i]))
for i in range(len(means)/2):
    gaussians[1].append(constGauss(newcase[i], variances[i+2], means[i+2]))

probs = [np.prod(gaussians[0]), np.prod(gaussians[1])] # 0, 1
classprobs = [((probs[0] * prior_y[0])/(np.prod(probs) * np.prod(prior_y)))] # 0, 1
print(classprobs)
