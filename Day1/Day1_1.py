# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:37:34 2024

@author: cassidy
"""

with open("input.txt") as f:
    lines = f.read().splitlines()

lhs = []
rhs = []

for line in lines:
    l,r = line.split()
    lhs.append(int(l))
    rhs.append(int(r))
    
lhs = sorted(lhs)
rhs = sorted(rhs)

res = 0

for l,r in zip(lhs, rhs):
    res += abs(l-r)
    
print(res)
