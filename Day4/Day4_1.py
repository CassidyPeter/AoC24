# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:56:13 2024

@author: cassidy
"""

with open("input.txt", "r") as f:
    ws = f.read().splitlines()


rows = len(ws)
cols = len(ws[0])


# Brute force babbbyyyyyy


def check(found):
    if found=='XMAS' or found=='SAMX':
        return 1
    else:
        return 0

total = 0

# Left and right
for ii in range(rows):
    for jj in range(cols-3):
        found = ws[ii][jj:jj+4]
        total += check(found)

# Up and down
for ii in range(rows-3):
    for jj in range(cols):
        found = ws[ii][jj] + ws[ii+1][jj] + ws[ii+2][jj] + ws[ii+3][jj]
        total += check(found)
                


# Diagonally down
for ii in range(rows-3):
    for jj in range(cols-3):
        found = ws[ii][jj] + ws[ii+1][jj+1] + ws[ii+2][jj+2] + ws[ii+3][jj+3]
        total += check(found)
        

# Diagonally up
for ii in range(rows-3):
    for jj in range(cols-3):
        found = ws[ii+3][jj] + ws[ii+2][jj+1] + ws[ii+1][jj+2] + ws[ii][jj+3]
        total += check(found)


print(total)
