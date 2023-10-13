import numpy as np

def geometric_random_log(p):
    q = 1 - p
    u = np.random.rand()
    x = int(np.log(u) / np.log(q) + 1)
    return x

# Set the parameter p
p = 0.3

# Generate a sample of Geometric random variables
samples = [geometric_random_log(p) for _ in range(10000)]
