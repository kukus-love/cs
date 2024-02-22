# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#a
arrayData = [10,5,6,7,1,12,13,15,21,8]

#b(i)
def linearSearch(number):
    for i in range(len(arrayData)):
        if arrayData[i] == number :
            return True 
    return False
    
#b(ii)
SearchValue = int(input("Enter a number to be searched for : "))
if linearSearch(SearchValue) == True:
    print("The number you entered has been found ")
else:
    print("The number you entered is not within the array")
    
#c 
def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
            
            
