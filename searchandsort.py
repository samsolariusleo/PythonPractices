# Filename: searchandsort.py
# Author: Gan Jing Ying
# Created: 20130925
# Modified: 20130925

def linearsearch(target, array):
    i = 0
    while i < len(array):
        if array[i] == target:
            return i
        else:
            i = i + 1
    return -1

# main
testlist = [2, 4, 1, 9, 20, 14]

print(linearsearch(1, testlist))
# >>> 2
print(linearsearch(5, testlist))
# >>> -1

def bubblesort(array):
    passes = len(array) - 1
    swapped = True
    while swapped:
        i = 0
        swapped = False
        while i < passes:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
            i = i + 1
        passes = passes - 1
    return array

print(bubblesort(testlist))
# >>> [1, 2, 4, 9, 14, 20]

def insertionsort(array):
    for j in range(1, len(array)):
        num = array[j]
        i = j - 1
        while i >= 0 and array[i] > array[i+1]:
            array[i] = array[i+1]
            i = i + 1
        array[i+1] = num
    return array

print(insertionsort(testlist))
# >>> [1, 2, 4, 9, 14, 20]

def quicksort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        less = []
        great = []
        for element in array[1:]:
            if element > pivot:
                great.append(element)
            else:
                less.append(element)
        return quicksort(less) + [pivot] + quicksort(great)

print(quicksort(testlist))
# >>> [1, 2, 4, 9, 14, 20]

def binarysearch(array, target, mid):
    while mid < len(array):
        if array[mid] == target:
            return "Found."
        elif array[mid] > target:
            newmid = len(array[:mid]) // 2
            return binarysearch(array[:mid], target, newmid)
        else:
            newmid = len(array[mid+1:]) // 2
            return binarysearch(array[mid+1:], target, newmid)
    return "Not found."

test = bubblesort(testlist)
print(binarysearch(test, 4, len(test) // 2))
# >>> "Found."
print(binarysearch(test, 5, len(test) // 2))
# >>> "Not found.")
print(binarysearch(test, 1, len(test) // 2))
# >>> "Found."
print(binarysearch(test, 20, len(test) // 2))
# >>> "Found."

