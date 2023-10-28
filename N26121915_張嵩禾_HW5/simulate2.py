import rdvy
import matplotlib.pyplot as plt




mean = 70 
std_dev = 5
samples = []
def transform(z):
    return mean + std_dev * z

for i in range(50):
    z = rdvy.generate_normal()
    sample = transform(z)
    if(sample < 0):
        sample = 0
    if(sample > 100):
        sample = 100
    samples.append(sample)

plt.hist(samples, bins=50, edgecolor = "black",density=True, alpha=0.6, color='r', label='Generated Samples')
plt.title('Classroom Grade Simulation')
plt.xlabel('Score')
plt.ylabel('Density')
plt.grid()
plt.legend()
plt.show()
