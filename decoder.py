import numpy as np
import matplotlib.pyplot as plt

#File name:
name=input("Enter full matrix file name: ")
#Loads the entire matrix.
A = np.loadtxt(name)
xmax=0
ymax=0
#This sets min and max temporarily to 0.
for i in A:
    if i[0]>xmax:
        xmax=i[0]
    if i[1]>ymax:
        ymax=i[1]
#Here we find biggest x and y in file.
xmax=int(xmax)+1
ymax=int(ymax)+1
#Now set to new min and max.
B=np.zeros((xmax,ymax))
#And create new array with 0's.
for i in A:
    B[int(i[0]),int(i[1])]=i[2]
#Then insert color shade number in each point in place of 0's.    
plt.imshow(B,cmap="binary")
plt.show()
#Index through matrix and plot point.
