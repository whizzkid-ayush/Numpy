import numpy as np
np1 = np.array([1,2,3,4,5,6,7,8])
print(np1[1:5])

np2 = np.array([1,2,3,4,5,6,7,8])
print(np2[1:])

np3 = np.array([1,2,3,4,5,6,7,8])
print(np3[-3:-1])

np4 = np.array([1,2,3,4,5,6,7,8])
print(np4[:])

np5 = np.array([1,2,3,4,5,6,7,8])
print(np5[1:6:2])

np6 = np.array([
    [1,2,3,4,5], 
    [6,7,8,9,10]])
#Pulling out a single item from 2D Array. Lets Take 8 out from the array
print(np6[1,2])
#Slice A 2D Array
print(np6[0:1, :])
