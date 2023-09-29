import random
from re import L, X
from time import time
import matplotlib.pyplot as plt


times = [] 
one = []
two = []
three = []
four = []
five = []
six = []
xyas = []
for i in range(6):
        times.append(0)

for x in range(1,10000):
    for i in range(6):
        times[i] = 0
    for i in range(x):
        res = random.randint(1, 6) #roll dice
        if(res == 1):
            times[0] += 1
        elif(res == 2):
            times[1] += 1
        elif(res == 3):
            times[2] += 1
        elif(res == 4):
            times[3] += 1
        elif(res == 5):
            times[4] += 1
        elif(res == 6):
            times[5] += 1

    xyas.append(x)
    one.append(times[0]/x)
    two.append(times[1]/x)
    three.append(times[2]/x)
    four.append(times[3]/x)
    five.append(times[4]/x)
    six.append(times[5]/x)

print(one)

plt.plot(xyas, one)
plt.plot(xyas, two)
plt.plot(xyas, three)
plt.plot(xyas, four)
plt.plot(xyas, five)
plt.plot(xyas, six)
plt.legend(['point 1','point 2','point 3','point 4','point 5','point 6'])

plt.axhline(y= 0.17, color='r', linestyle='--', label='Expected Probability of Heads in Coin Tosses')
plt.text(10000, 0.22, '0.17', ha='center', va='bottom', color='r')
plt.title(f'Simulation of Rolling Dice')
plt.xlabel('Number of Rolls')
plt.ylabel('Probability of  different point appears')
plt.show()



