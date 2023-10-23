import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def generate_poisson_method2(lambda_param):
    sum = 1
    ct = 0
    varr = 0
    while(1):
        varr = random.uniform(0,1)
        sum *= varr
        ct += 1
        if(sum < math.exp(-lambda_param)):
            break
    ct = ct - 1
    return ct


def generate_poisson_method1(lambda_param):
    U = random.random()
    i = 0
    p = math.exp(-lambda_param)
    F = p
    while(U >= F):
        p = lambda_param*p/(i+1)
        F = F + p
        i = i + 1

    return i

outx = []
outy =[]

outx1 = []
outy1 =[]
lambda_param = 5


    
outputarr = []
outputarr1 = []
outputarr2 = []
lambda_param = 5  


for _ in range(1000):
    random_variable = generate_poisson_method2(2.5) # Generate results for different values of lambda_param
    outputarr.append(random_variable)



for _ in range(1000):
    random_variable = generate_poisson_method2(5) # Generate results for different values of lambda_param
    outputarr1.append(random_variable)



for _ in range(1000):
    random_variable = generate_poisson_method2(10) # Generate results for different values of lambda_param
    outputarr2.append(random_variable)

plt.hist(outputarr2, bins=range(30),density=True,  alpha=0.25,  edgecolor='black', label=  f'λ={10} by Method 2')
plt.hist(outputarr1, bins=range(30),density=True,  alpha=0.25, color='red', edgecolor='black', label=  f'λ={5} by Method 2')
plt.hist(outputarr, bins=range(30),density=True,  alpha=0.25, color='green', edgecolor='black', label=  f'λ={2.5} by Method 2')
plt.xlabel('Random Variable Value')
plt.ylabel('Proportion')
plt.title('Poisson Distribution Random Variable Histogram')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


