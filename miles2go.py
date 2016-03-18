# Problem 1372. Miles to go before I sleep
#  Created by James 
# 
# Recently, my car's odometer passed 56789. Given an odometer reading, 
# output how many miles need to be driven to get the next mileage made up 
# of consecutive increasing numbers. If the mileage is already made up of 
# consecutive digits, output 0.
# 
# Use the digits 0-9 only. For example, if your odometer is at 67903 miles, 
# your script should output 10998, which is the number of miles needed to 
# reach 78901 (7-8-9-0-1), rather than 78910 (7-8-9-10).
# 
# You may need to increase the number of digits in your odometer reading to 
# accomplish this task. For example, a reading of 9843 means that you will 
# need to travel 2502 miles to get to 12345. However, a reading of 9011 
# needs only one more mile to get to 9012.

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 22:28:06 2016

@author: Darek
"""



def miles2go(x):
    
    import numpy as np
    
    A = np.array(map(int, '000000001,000000012,000000023,000000034,000000045,000000056,000000067,000000078,000000089,000000090,000000012,000000123,000000234,000000345,000000456,000000567,000000678,000000789,000000901,000001234,000002345,000003456,000004567,000005678,000006789,000007890,000008901,000009012,000012345,000023456,000034567,000045678,000056789,000067890,000078901,000089012,000090123,000123456,000234567,000345678,000456789,000567890,000678901,000789012,000890123,000901234,001234567,002345678,003456789,004567890,005678901,006789012,007890123,008901234,009012345,012345678,023456789,034567890,045678901,056789012,067890123,078901234,089012345,090123456,123456789,234567890,345678901,456789012,567890123,678901234,789012345,890123456,901234567'.split(','))) - x 
    min(A[A >= 0])
