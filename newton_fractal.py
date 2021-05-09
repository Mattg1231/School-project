import numpy as np
import matplotlib.pyplot as plt

num=input("Newton fractal z**n=1, Enter n (default 3): ")
if num=="":
    num=3
else:
    num=int(num)
cords=input("Enter xmin,xmax,ymin,ymax (default -1.35,1.35,-1.35,1.35): ")
if cords=="":
    cords=[-1.35,1.35,-1.35,1.35]
else:
    cords=cords.split()
    for i in range(len(cords)):
        cords[i]=float(cords[i])
sol=[]
print("Solutions are")
#These two funtion take the input given by the user. If there is none then it goes with the defult
for i in range(num): #This is how we get the newton factorial. 
    sol.append(np.exp(1j*2*np.pi*(i)/num))
    print(sol[i])
x=np.linspace(cords[0]+0.00011,cords[1],1000)
y=np.linspace(cords[2]+0.00011,cords[3],1000)
#Creating x and y cords.
C=np.zeros((1000,1000),dtype=complex) 
for i in range(1000):
    for j in range(1000):
        C[i,j]=x[j]+1j*y[999-i]
#Creating the matrix for c.
for i in range(20): # Do 20 Newton Iterations of the C matrix.
  C=C-((C**num-1)/(num*C**(num-1)))
col=np.zeros((1000,1000))#Set the new color matrix.
for i in range(1000):
    for j in range(1000):
        m=0
        dif=abs(C[i,j]-sol[0])/abs(sol[0])#Initial dif is for sol 0.
        for k in range(1,num):
            diftemp=abs(C[i,j]-sol[k])/abs(sol[k])#Compare each one.
            if diftemp<dif:
                m=k
                dif=diftemp
        col[i,j]=m*255/(num-1)#Set color based off of m.
plt.imshow(col,cmap='rainbow',origin='lower',interpolation='bilinear',extent=(cords[0],cords[1],cords[2],cords[3]))#plot each point
plt.show()
#Show image.