import numpy as np
# Filtering Numpy Arrays with boolean Index List
np1 =np.array([1,2,3,4,5,6,7,8])

x= [True, True, False, False,False, False, False, False]
print(np1)
print(np1[x])

#Not a good option
filtered = []
for thing in np1:
    if thing % 2==0:
        filtered.append(True)
    else:
        filtered.append(False)
print(np1)
print(filtered)
new = np1[filtered]
print(np1[filtered])

#hortHand

filtered = np1 %2==0
print(filtered)
new = np1[filtered]
print(np1[filtered])
      