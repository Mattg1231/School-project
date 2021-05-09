import numpy as np

num=input("Square root of which number? ")
#first i ask for input
num=float(num)
start=num
i=1
#now i convert num into a float and save the starting value aka the number we are rooting
while True:
    num=num-((num**2-start)/(2*num)) #Equation to actually solve the square root
    print(str(i),num)
    i=i+1 #keeps track of iterations
    if abs(num-np.sqrt(start))/abs(np.sqrt(start))<=10**(-15): #checks to see if its in range of stopping
        break