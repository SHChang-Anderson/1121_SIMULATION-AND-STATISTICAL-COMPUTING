import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime


mean = 70 
stddev = 5
random.seed(str(datetime.now()))
def target_pdf(x):
    return 1 / (stddev * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x - mean) / stddev)**2)

 
def Uniform_pdf(x):
    return 1/101


C = target_pdf(mean) / Uniform_pdf(mean)

n = 1000
samples = []
for i in range(n):
    while True:

        # generated variables to be integers or floating-point
        # x = random.uniform(0, 100) 
        x = random.randint(0, 100)

        accept_prob = target_pdf(x) / (C * Uniform_pdf(x))

        if random.random() < accept_prob:
            samples.append(x)
            break

# 1個標準差內的學生數量
in1dev = 0 
for i in range(len(samples)):
    if(samples[i]<=75 and samples[i] >= 65):
        in1dev += 1
string = "The proportion of students within one standard deviation from the mean in relation to the total number of students." + str(in1dev / len(samples))
print(string)

# 2個標準差內的學生數量
in1dev = 0 
for i in range(len(samples)):
    if(samples[i]<=80 and samples[i] >= 60):
        in1dev += 1
string = "The proportion of students within two standard deviation from the mean in relation to the total number of students." + str(in1dev / len(samples))
print(string)


# 3個標準差內的學生數量
in1dev = 0 
for i in range(len(samples)):
    if(samples[i]<=85 and samples[i] >= 55):
        in1dev += 1
string = "The proportion of students within three standard deviation from the mean in relation to the total number of students." + str(in1dev / len(samples))
print(string)

plt.hist(samples, bins=50, edgecolor = "black",density=True, alpha=0.6, color='r')
plt.title('Classroom Grade Simulation')
plt.xlabel('Score')
plt.ylabel('Density')
plt.grid()
plt.show()