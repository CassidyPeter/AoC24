# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:49:41 2024

@author: cassidy
"""

import re


with open("input.txt", "r") as f:
    memory = f.read()

muls = re.findall("mul\([0-9]+,[0-9]+\)",memory)

total = 0

for mul in muls:
    first, second = mul[4:-1].split(',')
    total += int(first) * int(second)

print(total)
