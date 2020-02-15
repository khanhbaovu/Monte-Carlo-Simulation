# Khanh Vu
# [Histogram of 5000 Monte Carlo simulations of the value of e]

import numpy as np
import math
import matplotlib.pyplot as plt

N = int(input("Enter the number of sub-intervals and random numbers: "))

eList = []

for i in range(0, 5000):
    array = np.zeros(N)
    Z = 0
    for i in range(0, N):
        num = np.random.random()
        
        location = int(N*num)

        array[location] += 1

    for i in range(0, N):
        if array[i] == 0.0:
            Z += 1

    e = N/Z

    eList.append(e)


    
   
plt.hist(eList)
plt.title("Estimates of e")
plt.ylabel("Number of estmates")
plt.xlabel("Values of estimates")
plt.show()


    
