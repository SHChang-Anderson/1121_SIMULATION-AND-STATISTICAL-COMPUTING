from hashlib import new
import random
import matplotlib.pyplot as plt
import math
from scipy import integrate

sum = 0
ct = 0
ctt = 0
newans = 0
oldans = 0
y = []
x = []
for simtuT in range(1,1000):
    oldans = newans
    ctt = 0
    for i in range(simtuT):
        sum = 0
        ct = 0
        varr = 0
        
        while(1):
            varr = random.uniform(0,1)
            sum += varr
            ct += 1
            if(sum > 1):
                break
        ctt += ct
 
    newans = ctt / simtuT
    print(newans)
    relative_err = abs((newans - oldans)  / newans)

    y.append(relative_err)
    x.append(simtuT)


plt.plot(x, y,color='orange')
plt.title(f'Estimate E[N] by generating x values of N')
plt.xlabel('The number of generated N values')
plt.ylabel('Relative error between the Previous and Current')
plt.show()