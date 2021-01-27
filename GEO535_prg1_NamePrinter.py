# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:29:34 2021

@author: C00452874
"""

name = input("Input name: ")

if type(name) != str:
    name = input("Input name as string: ")
    
print(str(name))
