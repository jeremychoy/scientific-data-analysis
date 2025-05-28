#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 11:03:25 2025

@author: jeremychoy
"""
value=1
previous_value=0
new_value=0
for i in range(20):
    previous_value = value
    value=new_value
    new_value = previous_value+value
    print(value)
    
fib=[0,1]
for i in range(18):
    fib.append(fib[-1]+fib[-2])
print(fib)

def fibgen(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibgen(n-1)+fibgen(n-2)

for i in range(20):
    print(fibgen(i+1))
