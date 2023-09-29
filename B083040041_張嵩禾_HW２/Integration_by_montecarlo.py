import random
import matplotlib.pyplot as plt
import math
from scipy import integrate
def func(x):
    y = math.exp(x+math.pow(x,2))
    return y

yyas = []
xyas = []

for k in range(1,10000):
    sum  = 0
    simtimes = k
    for i in range(simtimes):
        var = random.uniform(-2,2)
        sum = sum + func(var)
    ans = (sum / simtimes) * 4
    result, error = integrate.quad(func, -2, 2)
    
    

    relative_err = abs(ans - result) / abs(result)
    yyas.append(relative_err)
    xyas.append(k)
    
s = "Estimate result = " + str(ans)  
print(s)

s = "SciPy result = " + str(result)  
print(s)

plt.plot(xyas, yyas,color='orange')
plt.title(f'Simulate integration using the Monte Carlo method')
plt.xlabel('Number of random sampling point')
plt.ylabel('Relative Error')
plt.show()