# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:24:15 2020

@author: lucas
"""
import sys
import math
fnum = input('Enter first number: ')
try:
    x = float(fnum)
except:
    print("Invalid input")
    sys.exit()
snum = input('Enter second number: ')
try:
    y = float(snum)
except:
    print('Invalid input')
    sys.exit()
print(fnum,'raised to the power of',snum,'is:',x**y)
print('Log (base 2) of',fnum,'is:',math.log2(x))
