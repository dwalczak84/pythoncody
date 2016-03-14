# Problem 48. Making change
# Created by Cody Team 
#
# Given an amount of currency, return a vector of this form:
# [100 50 20 10 5 2 1 0.5 0.25 0.1 0.05 0.01]
#
# Example:
# Input a = 257.68
# Output b is [2 1 0 0 1 1 0 1 0 1 1 3]
#
# Always use bigger bills/coins if possible.

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:38:28 2016

@author: Darek
"""
def makingChange(a):
    
    import numpy as np
    x = 100 * np.array([100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01])
    y = np.array([])
    a = round(100 * (a * 100) / 100)
    i = 0
    j = 0

    while i <= len(x) and a > 0:
        while a - j * x[i] >= x[i]:         
            j = j + 1
        y = np.append([y], 0)
        y[i] = j
        a = a - j * x[i]
        i = i + 1
        j = 0
    return(y)
