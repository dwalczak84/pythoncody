# Problem 230. Project Euler: Problem 1, Multiples of 3 and 5
# Created by Doug Hull 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below the input value.
# Thank you to Project Euler Problem 1
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:19:51 2016

@author: Darek
"""


def euler001(x):

    import numpy as np
    return(sum(np.unique(np.concatenate([np.arange(3, x - 1, 3), 
                                         np.arange(5, x - 1, 5)]))))
  
