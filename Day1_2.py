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

countDict = {}

for l in lhs:
    for r in rhs:
        if l==r:
            if l in countDict:
                countDict[l] = countDict[l] + 1
            else:
                countDict[l] = 1
                
res = 0
for key,value in countDict.items():
    res += key * value



# Part 2 Quick solution found online LOL
res = 0
for num in lhs:
    res += num * rhs.count(num)


