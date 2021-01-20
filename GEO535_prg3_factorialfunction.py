# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:58:17 2021

@author: C00452874
"""
def factorial(n):
    if n == 1:
        factValue = 1
    if n != 1:
        factValue = n*factorial(n-1)
    return factValue
    
n = int(input("Input Value: "))
print(factorial(n))


