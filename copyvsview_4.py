import numpy as np
np1 = np.array([1,2,3,4,5])
np2 = np1.view()
print("This one is for view")
print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0]=41
print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')

print("This one is for copy")
np3 = np.array([1,2,3,4,5,6])
np4 = np3.copy()

print(f'Original NP3 {np3}')
print(f'Original NP4 {np4}')

np3[0]=41
print(f'Changed NP3 {np3}')
print(f'Original NP4 {np4}')