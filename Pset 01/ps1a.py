# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:47:26 2020

@author: lucas
"""
import sys
try:
    annual_salary = float(input('Enter your annual salary: '))
except:
    print('Invalid input.')
    sys.exit()                   
try:
    portion_saved = float(input('Enter the percent you want to save, as a decimal: '))
except:
    print('Invalid input.')
    sys.exit()
try:
    total_cost = float(input('Enter the cost of your dream home: '))
except:
    print('Invalid input')
    sys.exit()
current_savings = 0
portion_down_payment = total_cost * 0.25
r = 0.04
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + (annual_salary / 12 * portion_saved) + (current_savings * r / 12)
    months = months + 1
print('Number of months: ',months)
