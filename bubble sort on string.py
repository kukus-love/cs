# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:18:39 2024

@author: Form 6.2
"""
arrayChar = []
for i in range(5):
    arrayChar.append("")

for i in range(5):
    arrayChar[i] = input("enter a letter: ")

print(arrayChar)

upperB = 5
lowerB = 1
top = 5
swap = False

while swap == False or top == 0 :
    for i in range(4):
        tempChar = arrayChar[i]
        compChar = arrayChar[i+1]
        if tempChar > compChar:
            temp = tempChar 
            arrayChar[i] = compChar
            arrayChar[i+1] = temp 
            swap = True
    top = top - 1
    
print(arrayChar)
