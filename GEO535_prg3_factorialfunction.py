# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:58:17 2021

@author: C00452874
"""
def factorial(n):
    factValue = 1
    for i in range(1, n+1):
        factValue *= i
    return factValue
#Recursive Formula (Fails at n=2961)
#    if n == 1:
#        factValue = 1
#    if n != 1:
#        factValue = n*factorial(n-1)
#    return factValue
    
n = int(input("Input Value: "))
print(factorial(n))


