#  File: Spiral.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral(n):
    i = 1
    x = 0
    y = 0
    dictionary = {}
    while i <= n**2:
        if x == 0 and y == 0:
            dictionary[i] = (x, y)
            i += 1
            x += 1
        elif x == y and x > 0 and y > 0:
            dictionary[i] = (x, y)
            x += 1
            i += 1
        elif x == -y and x > 0:
            dictionary[i] = (x, y)
            x -= 1
            i += 1
        elif x == -y and x < 0:
            dictionary[i] = (x, y)
            x += 1
            i += 1
        elif x > abs(y) and x > 0:
            dictionary[i] = (x, y)
            y -= 1
            i += 1
        elif abs(x) < abs(y) and y < 0:
            dictionary[i] = (x, y)
            x -= 1
            i += 1
        elif x == y and x < 0 and y < 0:
            dictionary[i] = (x, y)
            y += 1
            i += 1
        elif abs(x) > abs(y):
            dictionary[i] = (x, y)
            y += 1
            i += 1
        elif y > abs(x) and y > 0:
            dictionary[i] = (x, y)
            x += 1
            i += 1
        elif abs(y) > x:
            dictionary[i] = (x, y)
            x -= 1
            i += 1
    return dictionary
    
    
# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    origin = dictionary[value]
    x = origin[0] - 1
    y = origin[1] - 1
    list
    summ = 0
    c = -1
    n = 0
    while n <= 6:
        c *= -1
        for a in range(0, 2):
            x += c
            if numFinder(x, y):
                summ += numFinder(x, y)
            n += 1
           
        for b in range(0, 2):
            y += c
            if numFinder(x, y):
                summ += numFinder(x, y)
            n += 1
    return summ

def numFinder(x, y):
    try:
        val = [k for k, v in dictionary.items() if v == (x,y)][0]
        return val
    except:
        return False

def main():
    data = sys.stdin.read()
    data_list = data.split("\n")
    n = data_list[0]

    spiral = create_spiral(n)
    for i in data_list[1:]:
        print(sum_adjacent_numbers(spiral, i))
        
    
    
    

# read the input file

# create the spiral

# add the adjacent numbers

# print the result

if __name__ == "__main__":
    main()

