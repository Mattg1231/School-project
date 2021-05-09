import numpy as np
import matplotlib.pyplot as plt

#File name:
name=input("Enter full matrix file name: ")
#Loads entire matrix.
A = np.loadtxt(name)


#This prints image of A.
plt.imshow(A,cmap="binary")
plt.show()



