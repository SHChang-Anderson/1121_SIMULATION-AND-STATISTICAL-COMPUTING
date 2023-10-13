import numpy as np

def geometric_random_inverse_transform(p):
    return int(np.log(1 - np.random.rand()) / np.log(1 - p)) + 1

# Set the parameter p
p = 0.3

# Generate a sample of Geometric random variables
samples = [geometric_random_inverse_transform(p) for _ in range(10000)]
