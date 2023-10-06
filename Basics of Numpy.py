import numpy as np
#list1 = [1,2,3,4,5,6,7,8,9,10]
#print(list1)
#list2 = ["John Smith", list1, 1, True]
#print(list1[3])
np1= np.array([1,2,3,4,5,6,7,8,9,10])
print(np1)
print(np1.shape)

#Range
np2 = np.arange(10)
print(np2)

#Range with Step
np3 = np.arange(0, 10, 2)
print(np3)

#Zeros for the arrays
np4 =np.zeros(10)
print(np4)

# MultiDimentional Arrays Zero
np5 = np.zeros((2,10))
print(np5)

#Full 
np6 = np.full((10), 6)
print(np6)

#MultiDimensional Full
np7 = np.full((2,10),6)
print(np7)

# Convert List into np
my_list = [1,2,3,4,5,6,7,8,9]
np8 = np.array(my_list)
print(np8)