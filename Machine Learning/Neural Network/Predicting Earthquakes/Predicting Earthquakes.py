from pandas import *
import numpy

#---------- csv to txt
pandas.options.display.max_rows = 1000000
pandas.options.display.max_columns = 1000000
pandas.options.display.height = 1000000
pandas.options.display.width = 10000000
path = "/home/parallels/Documents/Machine Learning/Neural Networks/Predicting Earthquakes/Raw Earthquake Data.csv"

f = open("Earthquake Data", "w")
f.write(str(read_csv(path)))
f.close

#---------- Batch Control
def getlines(fname):        
    with open(fname) as f:
        for i, l in enumerate(f):           #Find out how many lines in given file      
            pass
    return i + 1
f.close()

trainingsize = 0.95
datalen = getlines("Earthquake Data")
traininglen = datalen - (datalen - (int(round(datalen * trainingsize))))

f = open("Earthquake Data", "r")
g = open("Training Data", "w")
h = open("Testing Data", "w")

i = 0
while i != traininglen:
    g.write(f.readline(i))          #Creates training data file; training data is 95% of f ("Earthquake data")
    i = i + 1
i = 0
while i != (datalen - (int(round(datalen * trainingsize)))):
    h.write(f.readline(i))          #Creates testing data file; testing data is 5% of f ("Earthquake data")
    i = i + 1

f.close()
g.close()
h.close()

#Data Manipulation
date = []
time = []
lat = []
lon = []
depth = []
mag = []

with open("Training Data", "r") as f:
    for line in f:
        c = line[21] + line[22] + line[24] + line[25] + line[27] + line[28] + line[29] + line[30]
        date.append(c)
        c = line[49] + line[50] + line[52] + line[53] + line[55] + line[56]
        time.append(c)
        if line[58] == "-":
            c = line[58] + line[59] + line[60] + line[61] + line[62] + line[63] + line[64] + line[65] + line[66] + line[67]
        else:
            c = line[59] + line[60] + line[61] + line[62] + line[63] + line[64] + line[65] + line[66] + line[67]
        lat.append(c)
        if line[69] == "-":
            c = line[69] + line[70] + line[71] + line[72] + line[73] + line[74] + line[75] + line[76] + line[77] + line[78] + line[79]
        elif line[70] == "-":
            c = line[70] + line[71] + line[72] + line[73] + line[74] + line[75] + line[76] + line[77] + line[78] + line[79]
        elif line[70] == " ":
            c = line[71] + line[72] + line[73] + line[74] + line[75] + line[76] + line[77] + line[78] + line[79]
        else:
            c = line[70] + line[71] + line[72] + line[73] + line[74] + line[75] + line[76] + line[77] + line[78] + line[79]
        lon.append(c)
        if line[82] == " ":
            c = line[83] + line[84] + line[85] + line[86] + line[87] + line[88]
        else:
            c = line[82] + line[83] + line[84] + line[85] + line[86] + line[87] + line[88]
        depth.append(c)
        c = line[96] + line[97] + line[98] + line[99]
        mag.append(c)
            
date.remove(date[0])
time.remove(time[0])
lat.remove(lat[0])
lon.remove(lon[0])
depth.remove(depth[0])
mag.remove(mag[0])

x = np.array([])

i = 0
while i != len(date):
    x.append([date[i], time[i], lat[i], lon[i], depth[i], mag[i]])
    i = i + 1













