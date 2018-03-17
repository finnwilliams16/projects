import numpy as np
path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Heights And Weights\Heights And Weights.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int64)

m = len(data)
fm = len(data.T)

variances = [[], [], [], []] # 0x1, 0x2, 1x1...
means = [[], [], [], []] # 0x1, 0x2, 1x1...
gaussians = [[], []] # 2 gaussians 0, 1 made from n features
                     
x = [58, 54]

for i in range(m):
    if data[i][fm-1] == 0:      # Builds means/variances for each feature/y class
        variances[0].append(data[i][0])     # Appends data to first half of arrays if 0 (arrays 1 and 2/4)
        variances[1].append(data[i][1])
        means[0].append(data[i][0])
        means[1].append(data[i][1])
    else:
        variances[2].append(data[i][0])
        variances[3].append(data[i][1])
        means[2].append(data[i][0])
        means[3].append(data[i][1])

for i in range(len(variances)):     # Work out means and variances
    variances[i] = np.var(variances[i])
    means[i] = np.mean(means[i])

prior_y = [(m-(np.sum(data.T[fm-1])) + 0.0)/m, (np.sum(data.T[fm-1]) + 0.0)/m] # 0, 1

def buildGauss(x, vari, mean):  # Function to build gaussians
    const = 1/(np.sqrt(2 * np.pi * vari))
    num = (x - mean)**2
    denom = 2 * vari
    return const * np.exp(-(num/denom))

for i in range(fm-1):   # Build gaussuans from means/variances
    gaussians[0].append(buildGauss(x[i], variances[i], means[i]))
for i in range(fm-1):
    gaussians[1].append(buildGauss(x[i], variances[i + (fm - 1)], means[i + (fm - 1)]))

gaussians = [np.prod(gaussians[0]), np.prod(gaussians[1])]   # Build multivariate normals
probs = [gaussians[0] * prior_y[0], gaussians[1] * prior_y[1]]  # Numerator of Bayes theorem
probs = [probs[0]/(probs[0] + probs[1]), probs[1]/(probs[0] + probs[1])] # Denominator of Bayes theorem
print(probs.index(max(probs)))  # Classify
