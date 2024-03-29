import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])
v = np.array([0.2, 0.8])

print(np.convolve(a, v, mode='same'))
print("-" * 30)

print(np.convolve(a, v, mode='full'))
print("-" * 30)

print(np.convolve(a, v, mode='valid'))
print("-" * 30)
