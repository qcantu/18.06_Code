# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:13:30 2023

@author: CalmWhiz
"""

import numpy as np
from itertools import permutations
  
max_det = -float("inf")
max_array = np.array([])
allNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
allPerms = list(permutations(allNums))
for perm in allPerms:
    n_array = np.array([[perm[0], perm[1], perm[2]],
                        [perm[3], perm[4], perm[5]],
                        [perm[6], perm[7], perm[8]]])
    det = np.linalg.det(n_array)
    if det > max_det:
        max_det = det
        max_array = n_array

print("Maximizing matrix is:")
print(max_array)

print("\nDeterminant of maximizing matrix:")
print(int(max_det))