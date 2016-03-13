# Problem 21. Return the 3n+1 sequence for n
# % A Collatz sequence is the sequence where, for a given number n, the 
# next number in the sequence is either n/2 if the number is even or 3n+1 
# if the number is odd. The sequence always terminates with 1.
# 
# So if
#  n = 13
# 
# then
#  c = [13    40    20    10     5    16     8     4     2     1]


# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:19:37 2016

@author: Darek
"""

def collatz(n):
    c = [n]

    while c[-1] != 1:
        if n % 2 == 0:
            c.append(n / 2)
        else:
            c.append(3 * n + 1)
        n = c[-1]
    return(c)
    
 

# version using Numpy:   
# def collatz(n):
#    import numpy as np
#    c = np.array([n])
#    
#    while c[-1] != 1:
#        if c[-1] % 2 == 0:
#            c = np.append([c], c[-1] / 2)
#        else:
#            c = np.append([c], 3 * c[-1] + 1)
#    print(c)
