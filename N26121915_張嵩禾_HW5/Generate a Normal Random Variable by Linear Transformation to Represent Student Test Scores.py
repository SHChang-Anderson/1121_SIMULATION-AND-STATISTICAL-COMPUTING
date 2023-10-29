import rdvy
import matplotlib.pyplot as plt




mean = 70 
std_dev = 5
samples = []
def transform(z):
    return mean + std_dev * z

for i in range(1000):
    z = rdvy.generate_normal()
    sample = transform(z)
    if(sample < 0):
        sample = 0
    if(sample > 100):
        sample = 100
        
    # generated variables to be integers or floating-point
    samples.append(int(sample))
    # samples.append(sample)


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

plt.hist(samples, bins=50, edgecolor = "black",density=True, alpha=0.6, color='r', label='Generated Samples')
plt.title('Classroom Grade Simulation')
plt.xlabel('Score')
plt.ylabel('Density')
plt.grid()
plt.legend()
plt.show()
