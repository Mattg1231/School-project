##################################################
###### IF YOU WORK BY GROUP OF TWO ###############
###### ENTER YOUR TWO NAMES HERE:  ###############
###### Name1= Matthew Gjanci
###### Name2= Julian Day 
######
###### Only 1 submission on moodle (either names ok)
##################################################

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
N=1000000
x=np.random.uniform(-1,1,N) #generate random x and y
y=np.random.uniform(-1,1,N)
m=0
pi=np.zeros(N)
d=x**2+y**2 #radius of circle
bot=np.arange(0,N)
plt.figure(0)
plt.ylim(1.5,4)
plt.xlabel("#samples")
plt.ylabel("pi")
plt.xscale("log")
#changing the figure one graph lables and scale
for i in range(N): #for loop calulates for pi by checking if it is inside or not
    if(np.sqrt(d[i])<1):
        m+=1
    pi[i]=(4/(i+1))*m
plt.plot(bot,pi)
for i in range(int(np.log10(N))):# prints out pi values
    print("Using %s samples, pi is %s"%(10**(i+1),pi[10**(i+1)-1])) 
plt.figure(1)
theta=np.linspace(0,2*np.pi,360)#creates the circle data point values
cos=np.cos(theta)
sin=np.sin(theta)
for i in range(4):#plots the 4 scatter graphs
    plt.subplot(2,2,i+1)
    plt.axis("equal")
    plt.xticks([])
    plt.yticks([])
    plt.title("n=%s, pi=%.3f"%(10**(i+1),pi[10**(i+1)-1]))
    plt.scatter(x[0:10**(i+1)],y[0:10**(i+1)],c='r')
    plt.plot(cos,sin)
    #added the title, and created the subplots 
plt.show()
#shows the figures 