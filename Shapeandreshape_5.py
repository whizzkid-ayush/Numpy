import numpy as np
#Create a 1D Arrray and Get the shape of it 
np1 = np.array([1,2,3,44,5,6,7,8,9,10,11,12])
print(np1)
print(np1.shape)
 
# Create a 2D Array and Get The Shape, (ROws, Column)
np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(np2)
print(np2.shape)

# Reshape 2D Array
np3 = np1.reshape(3,4)
print(np3)
print(np3.shape)

#Reshape 3-d Array
np4 = np1.reshape(2,3,2)
print(np4)

#Flatten ti 1-D
np5 = np4.reshape(-1)
print(np5)