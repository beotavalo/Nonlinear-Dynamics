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
g = 9.81
beta = 0.5

xo = -1
vo = -2
to = 0

tf = 10
n =  101

h = 0.1

#Define vector of x values

t = np.linspace(to,tf,n)

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
print('------Fordwar Euler Method------')
for i in range(n):
    print(f't:{round(t[i],2)}, x:{round(x[i],4)}, v:{round(v[i],4)}')
    
    

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
plt.plot(x,v,'g')
plt.title('Phase Plane')
plt.xlabel('x')
plt.ylabel('v')
plt.show()
