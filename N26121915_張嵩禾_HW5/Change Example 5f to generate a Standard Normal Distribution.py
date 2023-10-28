import numpy as np
import math
import matplotlib.pyplot as plt
import random
from scipy.stats import norm






def generate_normal():
  while True:
    Y = random.expovariate(1)
    U = random.random()
    if U <= math.exp(-(Y-1)**2 / 2):
        if(random.randint(0,1) == 1):
            return -Y
        return Y

    else:
        continue

if __name__ == "__main__":    
    rdv = []
    for i in range(1000):
        X = generate_normal()
        rdv.append(X)

    mu = 0  
    sigma = 1  

    x = np.linspace(-5, 5, 100)

    pdf = norm.pdf(x, loc=mu, scale=sigma)
    plt.plot(x, pdf)
    plt.hist(rdv,density=True,edgecolor = "black", bins=25)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of 1000 Normal RVs')
    plt.show()