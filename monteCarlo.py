# Khanh Vu 
# [Monte Carlo simulation of the value of e]

import numpy as np
import math

N = int(input("Enter number of sub-intervals to simulate: "))

print()

array = np.zeros(N)
Z = 0

for i in range(0, N):
    num = np.random.random()

    location = int(N*num)

    array[location] += 1

for i in range(0, N):
    
    if array[i] == 0.0:
        Z += 1
        
    print("Number of random numbers fall into sub-intervat at {0} of array: {1}".format(i, array[i]))

MC_e = N/Z

exact = math.e

print()

print("The exact value of e: " + str(exact) + "\n")

print("The estimated value of e with monte carlo simulation: " + str(MC_e) + "\n")

print("Relative error between estimate of e and the exact value: " + str(abs(exact-MC_e)))
