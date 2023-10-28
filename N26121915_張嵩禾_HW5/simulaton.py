import numpy as np
import random


mean = 70 
stddev = 5

def target_pdf(x):
    return 1 / (stddev * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x - mean) / stddev)**2)

 
def standard_normal_pdf(x):
    return np.exp(-x**2/2) / np.sqrt(2*np.pi)


C = target_pdf(mean) / standard_normal_pdf(mean)

n = 1000 
samples = []
for i in range(n):
    while True:

        x = np.random.normal(0, 1)

        accept_prob = target_pdf(x) / (C * standard_normal_pdf(x))

        if random.random() < accept_prob:
            samples.append(x)
            break

print(np.mean(samples), np.std(samples))