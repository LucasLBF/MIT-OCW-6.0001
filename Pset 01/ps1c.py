# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:56:08 2021

@author: lucas
"""

import sys
try:
    starting_annual_salary = float(input('Enter your starting annual salary: '))
except:
    print('Invalid input.')
    sys.exit()

possible_to_pay = True
semi_annual_raise = 0.07
high = 7000
low = 0
portion_saved_int = high
monthly_savings = 0
current_savings = 0
annual_r = 0.04
monthly_invst = current_savings * (annual_r / 12)
house_cost = 1000000
down_pay = house_cost * 0.25
epsilon = 100
steps = 0


while True:
    steps += 1
    annual_salary = starting_annual_salary
    current_savings = 0
    months = 0
    portion_saved = portion_saved_int / 7000
    
    while months < 36:
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        
        monthly_salary = annual_salary / 12    
        monthly_savings = monthly_salary * portion_saved   
        current_savings += monthly_savings + monthly_invst   
        months += 1
        
    if abs(current_savings - down_pay) <= epsilon: break
    
    if current_savings > down_pay:
        high = portion_saved_int
        
    else:
        low = portion_saved_int
        
    if low >= high:
        possible_to_pay = False
        break
        
    portion_saved_int = (high + low) / 2

if possible_to_pay:
    print("Best savings rate: ",portion_saved)
    print("Steps in bisection search: ",steps) 

else:
    print("Not possible to reach goal with this amount.")    
