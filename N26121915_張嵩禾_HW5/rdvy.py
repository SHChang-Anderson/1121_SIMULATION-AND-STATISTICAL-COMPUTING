import numpy as np
import math
import matplotlib.pyplot as plt

# Set the seed for reproducibility (optional)
np.random.seed(0)

# Generate a random variable from an exponential distribution with rate 1
rate = 1
sample_size = 1  # You can change the sample size if you want more samples
ans = []
x = []
for i in range(1000):
    while(1):
        Y = np.random.exponential(scale=1/rate, size=sample_size)
        U = np.random.random()
        if(U <= math.exp((-(Y-1)) * (-(Y-1))/ 2)):
            break
    ans.append(Y)       

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.hist(ans, bins=30, density=True, alpha=0.6, label='Histogram')
plt.xlabel('随机变量')
plt.ylabel('频率')
plt.title('直方图')

# 绘制正态概率图 (Q-Q plot)
plt.subplot(1, 2, 2)
plt.title('正态概率图 (Q-Q plot)')

plt.show()