import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap

def make_spiral(arr):
    nrows, ncols = arr.shape
    idx = np.arange(nrows * ncols).reshape(nrows, ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append(idx[0])
        idx = idx[1:]
        idx = idx.T[::-1]
    spiral_idx = np.hstack(spiral_idx)
    spiral = np.empty_like(arr)
    spiral.flat[spiral_idx] = arr.flat[::-1]
    return spiral

# Fast sieve of Eratosthenes
def sieve_primes(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : limit + 1 : i] = False
    return np.flatnonzero(sieve)

# Spiral size (use small value for testing)
w = 60000
N = w * w

# Generate primes and map to 1s
prime_mask = np.zeros(N, dtype='u1')
prime_mask[sieve_primes(N) - 1] = 1

# Spiral into matrix
spiral = make_spiral(prime_mask.reshape((w, w)))

# Mark the center (start of the spiral) as a special value
center = w // 2
spiral[center, center] = 2  # Unique value for start

# Create a custom colormap: 0 = white, 1 = black (primes), 2 = red (start)
cmap = ListedColormap(['white', 'black', 'red'])

# Plot
plt.figure(figsize=(8, 8))
plt.imshow(spiral, cmap=cmap)
plt.axis('off')
plt.savefig('ulam_start_colored.png', dpi=300)
plt.show()

