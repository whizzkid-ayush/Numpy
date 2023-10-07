import numpy as np
# Numerical Array
np1 = np.array([6,3,9,2,6,5,7,1,0])
print(np1)
print(np.sort(np1))
print(np.sort(np1)[::-1])

np2 = np.array(["John", "Teeena", "Aaaron", "Zed"])
print(np2)
print(np.sort(np2))

np3 = np.array([True, True, False, False])
print(np3)
print(np.sort(np3))

#We are not changign the value pf array, we are jsut making athe array of that one

#2D Ayrray
np4 = np.array([[6,7,1,9],[8,3,9,5]])
print(np.sort(np4))