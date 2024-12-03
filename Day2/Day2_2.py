# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:49:41 2024

@author: cassidy
"""


f = open("input.txt", 'r')

reports = f.readlines()

total = 0
total2 = 0

def check(r):
    diff = [r[i+1] - r[i] for i in range(len(r)-1)]
    if all(d>0 and d<=3 for d in diff) or all(d<0 and d>=-3 for d in diff):
        return True
    return False

def checkpt2(r):
    for i in range(len(r)):
        if check(r[:i]+r[i+1:]):
            return True
    return False
    
for report in reports:
    rep = [int(n) for n in report.split(" ")]
    
    if check(rep):
        total += 1
    elif checkpt2(rep):
        total2 += 1

total2 = total + total2