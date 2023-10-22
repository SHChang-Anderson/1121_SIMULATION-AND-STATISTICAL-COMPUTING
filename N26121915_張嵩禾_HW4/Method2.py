import random
import math
import numpy as np
import matplotlib.pyplot as plt

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
    


def generate_poisson_rejection(lambda_param):
    while True:
       
        Y = random.randint(0, 30) 

      
        U = random.random()

      
        max = 0 
        f_Y = (lambda_param ** Y) * math.exp(-lambda_param) / math.factorial(Y)  
        for i in range(30):
            test_Y = (lambda_param ** i) * math.exp(-lambda_param) / math.factorial(i)
            if( test_Y > max):
                max = test_Y
        print(max)
        g_Y = 1 / 30 * 1.754673697678507 * 2 
        if U <= f_Y / (g_Y):
            return Y

outx = []
outy =[]

outx1 = []
outy1 =[]
lambda_param = 10


maxer = 0
for i in range(30) :
    outy1.append((lambda_param ** i) * math.exp(-lambda_param) / math.factorial(i))
    tester = (lambda_param ** i) * math.exp(-lambda_param) / math.factorial(i)
    if( tester > maxer):
        maxer = tester
print(maxer)
for i in range(30) :
    outx.append(i)
    outy.append(1/30 * 1.754673697678507 * 2 )


plt.plot(outx, outy,color='red',label= "Proposal Function" )
plt.plot(outx, outy1,color='orange',label= "Target Function")
plt.title(f'Proposal Function vs. Target Function ')
plt.xlabel('Random Variable Value')
plt.ylabel('Mean occurrence probability')
plt.legend()
plt.show()
    
outputarr = []
outputarr1 = []

for _ in range(1000):
    random_variable = generate_poisson_rejection(lambda_param)
    outputarr.append(random_variable)

for _ in range(1000):
    random_variable = generate_poisson(lambda_param)
    outputarr1.append(random_variable)

plt.hist(outputarr1, bins=range(30),  alpha=0.25, color='red', edgecolor='black', label=  f'λ={5} by Method 1')
plt.hist(outputarr, bins=range(30),  alpha=0.25, color='green', edgecolor='black', label=  f'λ={5} by Method 2')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Times')
plt.title('Poisson Distribution Random Variable Histogram')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()