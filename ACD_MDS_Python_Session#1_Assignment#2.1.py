# -*- coding: utf-8 -*-
"""
Spyder Editor

Accepts a sequence of comma-separated numbers from console
and generate a list.
"""
i = 1
while i < 10:
    j = i
    if (j > 5):
        j = 10 - j
    print("*" * j)
    i = i + 1
    