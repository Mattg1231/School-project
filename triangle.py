import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)
N=100000 #This is the greates number of samples we take, below initializes 3 default inputs setting them to the correct default values if there is no input.
p1=input("Enter (x,y) of point-1, default is (0.5,0.5): ")
p2=input("Enter (x,y) of point-2, default is (3,2.5): ")
p3=input("Enter (x,y) of point-3, default is (1,3): ")
if p1=="":
    x1=.5
    y1=.5
else:
    p=p1.split()
    x1=float(p[0])
    y1=float(p[1])
if p2=="":
    x2=3
    y2=2.5
else:
    p=p2.split()
    x2=float(p[0])
    y2=float(p[1])
if p3=="":
    x3=1
    y3=3
else:
    p=p3.split()
    x3=float(p[0])
    y3=float(p[1])

xarray=np.array([x1,x2,x3])
yarray=np.array([y1,y2,y3])
#Numbers are put into array to make them easier to handle. 
omega=abs((xarray.max()-xarray.min())*(yarray.max()-yarray.min()))
x=np.random.uniform(xarray.min(),xarray.max(),N) #This generates random x and y.
y=np.random.uniform(yarray.min(),yarray.max(),N)


m=0
Area=np.zeros(N)
plt.ylim(0,3)
bot=np.arange(0,N)
plt.figure(0)
plt.xlabel("#samples")
plt.ylabel("Area-Triangle")
plt.xscale("log")
#here we are Changing the figure one graph, lables, and scale.
A=np.array([[x1,x2,x3],[y1,y2,y3],[1,1,1]])
#creating my matrix
for i in range(N): #For loop calulates for area of triangle by checking if it is inside or not using matrix.
    point=np.array([x[i],y[i],1])
    s=np.linalg.solve(A,point)
    if(s.min()>0):
        m+=1
    Area[i]=(omega/(i+1))*m
plt.plot(bot,Area)
print("Barycentric Matrix")
print(A)
for i in range(int(np.log10(N))):#This prints out the Area values.
    print("Using %s samples, area of triangle is %s"%(10**(i+1),Area[10**(i+1)-1])) 
plt.figure(1)
xt=np.array([x1,x2,x3,x1])
yt=np.array([y1,y2,y3,y1])
for i in range(4):#Plots the 4 scatter plot graphs.
    plt.subplot(2,2,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title("m=%s, area=%.3f"%(10**(i+1),Area[10**(i+1)-1]))
    plt.scatter(x[0:10**(i+1)],y[0:10**(i+1)],c='r')
    plt.plot(xt,yt)
    #Added the title, and created the subplots. 
plt.show()
#Shows the figures. 
