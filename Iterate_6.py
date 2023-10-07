import numpy as np

#1D Array
np1 = np.array([1,2,3,4,5,6,7,8])
for x in np1:
    print(x)


np2 = np.array([[1,2,3,4],[5,6,7,8]])
for y in np2:
    #print(y)
    for z in y:
        print(z)

#3D Array
np3 =np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
for a in np3:
    #print(a)
    for b in a:
       #print(b)
       for c in b:
           print(c)


#Now using np.nditer()
np4 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
for x in np.nditer(np4):
    print(x)