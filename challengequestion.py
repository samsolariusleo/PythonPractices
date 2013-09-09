# Filename: challengequestion.py
# Author: Gan Jing Ying
# Created: 20130909
# Modified: 20130909

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
def currentchecksums(currentcode):
    upperchecksum = 0
    lowerchecksum = 0
    # calculate the checksum with current characters first
    for i in currentcode[:3]:
        upperchecksum += upperkeys[int(i)]
        lowerchecksum += lowerkeys[int(i)]
    return upperchecksum, lowerchecksum

def findchecksums(checkdigit):
    for i in table:
        if checkdigit in i:
            upperchecksum = table.index(i) + 1
            lowerchecksum = i.index(checkdigit) + 1
            if upperchecksum == 0:
                upperchecksum = 0
            elif lowerchecksum == 6:
                lowerchecksum = 0
            break
    return upperchecksum, lowerchecksum

# greatest lowerchecksum is 28, code uses 5s
# smallest lowerchecksum is 13, code uses 0s and 6s

# greatest upperchecksum is 10, based on currentcode

# main

currentcode = '436XYZG'
upper, lower = currentchecksums(currentcode)
# print(str(upper) + ' , ' + str(lower))

# finding the checksum due to the checkdigit
checkupper, checklower = findchecksums(currentcode[-1])
# print(str(checkupper) + ' , ' + str(checklower))

while checkupper < upper:
    checkupper += 6

# finding the lowest possible lower half values
while checklower < (lower + 3):
    checklower += 6

# first set of lower half values for last 3 digits
checklower -= lower
checkupper -= upper
print(checklower)
print(checkupper)

# lower halves add together = 7
# upper halves add together = 5

# numbers come from 6, 7, 8, 9 and 0, 1, 2, 3



## This programme is incomplete.
