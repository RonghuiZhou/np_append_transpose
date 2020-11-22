"""
To transpose the 2d arrays inside a 3d array

"""

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# append numpy array
b = np.append(a,a.T).reshape(-1,a.shape[0], a.shape[1])

print(f'\nBefore transpose:\n{b}')

# transpose:

c = np.moveaxis(b.T, -1, 0)
c_ravel = c.ravel().astype(np.int)

print(f'\nAfter transpose:\n{c}')

np.savetxt("c_ravel.txt", c_ravel)

d = np.loadtxt("c_ravel.txt").astype(int).reshape(-1,a.shape[0], a.shape[1])
print(f'\nAfter save and reload: \n{d}')