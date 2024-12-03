# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:49:41 2024

@author: cassidy
"""

f = open("input.txt", 'r')

reports = f.readlines()

total = 0

for report in reports:
    rep = [int(n) for n in report.split(" ")]
    diff = [rep[i+1] - rep[i] for i in range(len(rep)-1)]
    if all(d>0 and d<=3 for d in diff) or all(d<0 and d>=-3 for d in diff):
        total += 1
    
print(total)
