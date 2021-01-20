# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:34:00 2021

@author: C00452874
"""
import numpy as np


num = []
A_total = H_total = sd_total = 0
G_total = 1.0
num.append(float(input("Input 10 numbers to be averaged (Press enter between submission): ")))
for i in range(1, 10):
    num.append(float(input()))

###Mean Calculation
for i in range(len(num)):
    A_total += num[i]
    H_total += (1/num[i])
    G_total *= num[i]

A_mean = A_total/len(num)
H_mean = len(num)/H_total
G_mean = G_total**((1/len(num)))

for i in range(len(num)):
    sd_total += (num[i] - A_mean)**2

std_dev = np.sqrt(sd_total/(len(num)))

print("Numbers submitted: " + str(num))
print("Arithmetic Mean: " + str(A_mean))
print("Harmonic Mean: " + str(H_mean))
print("Geometric Mean: " + str(G_mean))
print("Standard Deviation: " + str(std_dev))