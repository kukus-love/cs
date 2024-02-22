# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:33:36 2024

@author: Form 6.2
"""
fileA = "fileA.txt"

file = open(fileA, 'w')

for i in range(3):
    line = input("enter a something: ")
    file.write(line + '\n')
file.close()
