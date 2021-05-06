# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:06:16 2021

@author: braul
"""
#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#defining parameters and initial conditions
k = 2
m = 0.5
g =0
beta = 0

xo = -1
vo = -2

xf = 10
n =  101

h = 0.1

#Define vector of x values

t = np.linspace(xo,xf,n)

#initializing array of v values
x = np.zeros([n])
v = np.zeros([n])

#For loo for forward Euler's method
x[0]=xo
v[0]=vo

for i in range(1, n):
    
    x[i] = x[i-1] + h * v[i-1]  
    v[i] = v[i-1] + h*(g-(k/m)*x[i-1] - beta/m*v[i-1])
    
#Printing the Data
for i in range(n):
    print(f't:{i}, x:{round(x[i],3)}, v:{round(v[i],3)}')
    
    

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(t, x, 'b--', label='x')
ax.plot(t, v, 'r:', label='v')

legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')

#Put a nicer background color on the legend.
legend.get_frame().set_facecolor('w')
plt.title('Forward Euler Method')
plt.xlabel('t')
plt.show()

# Create plots with pre-defined labels.
plt.plot(x,v,)
plt.title('Phase Plane')
plt.xlabel('x')
plt.ylabel('v')
plt.show()
