import numpy as np
path = "C:\Users\Finn Williams\Documents\Machine Learning\Naive Bayes Classifier\Continuous Variables\Diabetes\Pima Indians Diabetes.csv"
rawdata = open(path, "rt")
data = np.loadtxt(rawdata, delimiter = ",", dtype = np.int32)

print(data)

m = len(data)
fm = len(data.T)

'''2,122,70,27,0,36.8,0.340,27,0
5,121,72,23,112,26.2,0.245,30,0
1,126,60,0,0,30.1,0.349,47,1
1,93,70,31,0,30.4,0.315,23,0
3,171,72,33,135,33.3,0.199,24,1
7,142,90,24,480,30.4,0.128,43,1'''

variances = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 0x1, 0x2, 1x1...
means = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 0x1, 0x2, 1x1...
gaussians = [[], []] # 2 gaussians 0, 1 made from n features
                     
x = [7,142,90,24,480,30.4,0.128,43]

for i in range(m):
    if data[i][fm-1] == 0:      # Builds means/variances for each feature/y class
        variances[0].append(data[i][0])
        variances[1].append(data[i][1])
        variances[2].append(data[i][2])
        variances[3].append(data[i][3])
        variances[4].append(data[i][4])
        variances[5].append(data[i][5])
        variances[6].append(data[i][6])
        variances[7].append(data[i][7])
        means[0].append(data[i][0])
        means[1].append(data[i][1])
        means[2].append(data[i][2])
        means[3].append(data[i][3])
        means[4].append(data[i][4])
        means[5].append(data[i][5])
        means[6].append(data[i][6])
        means[7].append(data[i][7])
    else:
        variances[8].append(data[i][0])
        variances[9].append(data[i][1])
        variances[10].append(data[i][2])
        variances[11].append(data[i][3])
        variances[12].append(data[i][4])
        variances[13].append(data[i][5])
        variances[14].append(data[i][6])
        variances[15].append(data[i][7])
        means[8].append(data[i][0])
        means[9].append(data[i][1])
        means[10].append(data[i][2])
        means[11].append(data[i][3])
        means[12].append(data[i][4])
        means[13].append(data[i][5])
        means[14].append(data[i][6])
        means[15].append(data[i][7])

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
print(probs.index(max(probs)))  # Classify'''
