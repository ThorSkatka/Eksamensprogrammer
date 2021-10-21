# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:34:38 2021

@author: Andreas
"""


def integer_to_roman(x):
    roman_numerals = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" ,"IV", "I" ]
    integers = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    i = 0
    roman_string = ""
    while x > 0:
        #Runs through each integer untill floor division is bigger than 0
        while (x // integers[i]) > 0:
            roman_string += roman_numerals[i]
            #Change x to take out the number that has just been added to the roman_string
            x -= integers[i]
        #This happens if floor division is less than 0
        i+=1
    return roman_string


