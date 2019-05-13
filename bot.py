# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:37:13 2019

@author: UARTman
"""

def make_turn(field):
    variants={}
    r = []
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == 0:
                variants[(i, j)] = 0
    for q in variants:
        for i in range(len(field)):
            if i != q[0] and field[i][q[1]] == 0:
                variants[q] += 1
            if i != q[1] and field[q[0]][i] == 0:
                variants[q] += 1
    for i in variants:
        r.append(variants[i])
    for i in variants:
        if variants[i] == max(r):
            return [i[0], i[1], 4]
    return [-1, -1, 4]