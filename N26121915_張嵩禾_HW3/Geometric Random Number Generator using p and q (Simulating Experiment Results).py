import numpy as np

def geometric_random_pq(p, q):
    count = 0
    while True:
        count += 1
        if np.random.rand() < p:
            return count

# Set the parameters p and q
p = 0.3
q = 1 - p

# Generate a sample of Geometric random variables
samples = [geometric_random_pq(p, q) for _ in range(10000)]
print(samples)