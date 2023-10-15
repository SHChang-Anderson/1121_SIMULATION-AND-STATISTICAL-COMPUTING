import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import geom

def geometric_random_pq(p, q):
    count = 0
    while True:
        count += 1
        if np.random.rand() < p:
            return count



p = 0.15
q = 1 - p
samples_nums = 1000

geometric_random_numbers = []

for i in range(samples_nums):
    geometric_random_numbers.append(geometric_random_pq(p,q))

plt.hist(geometric_random_numbers, bins = max(geometric_random_numbers), density=True)
plt.xlabel('Number of Trials')
plt.ylabel('Probability')
plt.title(f'Geometric Distribution (p = {p})')


x = np.arange(1, max(geometric_random_numbers) + 1)
pmf = geom.pmf(x, p)
plt.plot(x, pmf, 'o:', label='Theoretical PMF')
plt.show()
