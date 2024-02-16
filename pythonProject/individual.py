#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

x1 = float(input("Write X1: "))
y1 = float(input("Write Y1: "))
x2 = float(input("Write X2: "))
y2 = float(input("Write Y2: "))
x3 = float(input("Write X3: "))
y3 = float(input("Write Y3: "))
print("Point 1 = (",x1,",",y1,")")
print("Point 2 = (",x2,",",y3,")")
print("Point 3 = (",x3,",",y3,")")
a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("Perimeter =", p)
print("Square = ", s)