%matplotlib notebook 
# ^^ Only run this line if you're using Jupyter

import matplotlib.pyplot as plt
import numpy as np
import math
from random import uniform as rand

#data = np.loadtxt('pi_approx.txt') #This line written when random numbers were generated in Processing

#This Monte Carlo simulation works by placing points randomly inside a square (with inscribed circle),
#then dividing the number of points inside by the number of points total and multiplying by 4 to get pi.
#(It works out if you do the area equations.)

iterations = 50000
data = [0]*iterations
inside = 0
for i in range(1,iterations):
    pos = [rand(0,1),rand(0,1)]
    if (pos[0]**2 + pos[1]**2)**0.5 <= 1: #Circle membership test
        inside += 1
    data[i] = inside/i*4

x = np.arange(0,len(data),1)
plt.plot(x,data)
plt.plot(x,[math.pi for x in range(len(data))])
plt.ylim([3.0,3.25])
plt.show()
