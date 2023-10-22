import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time

def generate_poisson(lambda_param):
    U = random.random()
    i = 0
    p = math.exp(-lambda_param)
    F = p
    while(U >= F):
        p = lambda_param*p/(i+1)
        F = F + p
        i = i + 1

    return i
    
    

outputarr = []
outputarr1 = []
outputarr2 = []
lambda_param = 5  


for _ in range(1000):
    random_variable = generate_poisson(2.5) # Generate results for different values of lambda_param
    outputarr.append(random_variable)
end = time.time()



start = time.time()
for _ in range(1000):
    random_variable = generate_poisson(lambda_param) # Generate results for different values of lambda_param
    outputarr1.append(random_variable)
outtime = format(end - start)
print(outtime)
out = "Generate 1000 R.D.V Time (λ = 5) : " + outtime + " seconds."
print(out)


for _ in range(1000):
    random_variable = generate_poisson(10) # Generate results for different values of lambda_param
    outputarr2.append(random_variable)

plt.hist(outputarr, bins=range(30),  alpha=0.5, color='green', edgecolor='black', label=  f'λ={2.5}')
plt.hist(outputarr1, bins=range(30),  alpha=0.5, color='orange', edgecolor='black', label=  f'λ={5}')
plt.hist(outputarr2, bins=range(30),  alpha=0.5, color='red', edgecolor='black', label=  f'λ={10}')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Times')
plt.title('Poisson Distribution Random Variable Histogram')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()