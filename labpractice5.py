# Filename: labpractice5.py
# Author: Gan Jing Ying
# Created: 20130909
# Modified: 20130909

import re

# define variables
upperkeys = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
lowerkeys = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

table = [['0', '1', '2', '3', '4', '5'],
         ['6', '7', '8', '9', 'A', 'B'],
         ['C', 'D', 'E', 'F', 'G', 'H'],
         ['I', 'J', 'K', 'L', 'M', 'N'],
         ['O', 'P', 'Q', 'R', 'S', 'T'],
         ['U', 'V', 'W', 'X', 'Y', 'Z']]

# define functions
def prelimtest():
    pattern = re.compile('[0-9]{6}[0-9A-Za-z]')
    # prompt for postal code
    code = input("Enter 7-digit postal code (enter '-1' to exit): ")
    if code == '-1':
        print("You have exited this programme. Goodbye.")
    elif len(code) != 7:
        print("Invalid. The code is not of the correct length.")
        code = '-1'
    elif not pattern.match(code):
        print("Invalid.")
        code = '-1'
    else:
        print("Invalid.")
        code = '-1'
    return code

def generatecheckdigit(code):
    upperchecksum = 0
    lowerchecksum = 0
    for i in code[:-1]: # for each letter in the code
        upperchecksum += upperkeys[int(i)]
        lowerchecksum += lowerkeys[int(i)]
    rowvalue = upperchecksum % 6
    columnvalue = lowerchecksum % 6
    if rowvalue == 0:
        if columnvalue == 0:
            checkdigit = 'Z'
        else:
            checkdigit = table[-1][columnvalue - 1]
    else:
        checkdigit = table[rowvalue - 1][columnvalue - 1]
    return checkdigit

def valid(code, checkdigit):
    if code[-1] == checkdigit:
        return True
    else:
        return False

# main

code = prelimtest()

if code != '-1':
    # check if the code is valid
    checkdigit = generatecheckdigit(code)
    if not valid(code, checkdigit):
        print("Invalid. Expected checksum character is " + checkdigit)
    else:
        print("OK")

