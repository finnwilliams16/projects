'''import numpy as np
x = np.array([[65,50],
[62,49],
[130,78],
[124,79],
[54,47],
[169,76],
[59,58],
[169,79],
[52,52]])

y = np.array([0, 0, 1, 1, 0, 1, 0, 1, 0])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x, y)
GaussianNB(priors = None)
print(clf.predict([[51, 51]])) 
'''

import numpy as np

def constGauss(x, vari, mean):
    const = 1/(np.sqrt(2 * np.pi * vari))
    num = (x - mean)**2
    denom = 2 * vari
    return const * np.exp(-(num/denom))

print(constGauss(54, 1.5, 78))
