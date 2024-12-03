# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:49:41 2024

@author: cassidy
"""

import re


with open("input.txt", "r") as f:
    memory = f.read()
    
muls = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)",memory)

total = 0
total2 = 0

do = True

for mul in muls:
    if mul == 'do()':
        do = True
    elif mul == 'don\'t()':
        do = False
    else:
        first, second = mul[4:-1].split(',')
        total += int(first) * int(second)
        if do == True:
            total2 += int(first) * int(second)
        
print(total, total2)
