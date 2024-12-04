# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:56:13 2024

@author: cassidy
"""

with open("input.txt", "r") as f:
    ws = f.read().splitlines()


rows = len(ws)
cols = len(ws[0])

total2 = 0

# X-MAS
for ii in range(rows-2):
    for jj in range(cols-2):
        firstDiag = ws[ii][jj] + ws[ii+1][jj+1] + ws[ii+2][jj+2]
        secDiag = ws[ii+2][jj] + ws[ii+1][jj+1] + ws[ii][jj+2]
        if (firstDiag=='MAS' or firstDiag=='SAM') and (secDiag=='MAS' or secDiag=='SAM'):
            total2 += 1


print(total2)

