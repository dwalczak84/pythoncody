# Problem 2593. Polite numbers. N-th polite number.
#  Created by Jan Orwat 
# 
# A polite number is an integer that sums of at least two consecutive 
# positive integers.
# 
# For example 7 = 3+4 so 7 is a polite number.
# 
# Given N return N-th polite number.
# 
# See also 2595

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:16:03 2016

@author: Darek
"""


def Nth_polite(n):
    
    import numpy as np    
    A =  pow(2, np.arange(0, 35, dtype = float))
    if n < 1e7:
        return(np.delete(np.arange(1, 1e7), A - 1)[n-1])
    else:
        return(int((n + sum(n > A))))
