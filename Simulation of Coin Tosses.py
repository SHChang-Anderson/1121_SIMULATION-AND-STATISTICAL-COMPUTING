import random
import matplotlib.pyplot as plt

xyas = []
headyyas = []
tailyyas = []

for x in range(1,10000):
    xyas.append(x)
    head = 0
    tail = 0
    for i in range(x):
        temp = random.randint(0, 1)
        if(temp == 0):
            head += 1
        else:
            tail += 1
    tailyyas.append(tail/x)
    headyyas.append(head/x)
    
plt.plot(xyas, headyyas,color='orange')
plt.axhline(y=0.5, color='r', linestyle='--', label='Expected Probability of Heads in Coin Tosses')
plt.text(10000, 0.6, '0.5', ha='center', va='bottom', color='r')
plt.title(f'Simulation of Coin Tosses')
plt.xlabel('Number of Coin Tosses')
plt.ylabel('Probability of Heads in Coin Tosses')
plt.show()
plt.plot(xyas, tailyyas)
plt.axhline(y=0.5, color='r', linestyle='--', label='Expected Probability of Tails in Coin Tosses')
plt.text(10000, 0.6, '0.5', ha='center', va='bottom', color='r')
plt.title(f'Simulation of Coin Tosses')
plt.xlabel('Number of Coin Tosses')
plt.ylabel('Probability of Tails in Coin Tosses')
plt.show()