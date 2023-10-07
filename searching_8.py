import numpy as np
np1 = np.array([1,2,3,4,5,6,7,8,9])
x = np.where(np1 ==3)
print(np1)
print(x)

np2 = np.array([1,2,3,4,5,2,6,3,7,8,9,2,3])
x = np.where(np2 ==2)
print(np2)
print(x)

#just to print the index
y = np.where(np2 ==2)
print(np2)
print(y[0])
print(np2[y[0]])

#return even items
y= np.where(np1%2==0)
print(np2)
print(y[0])
