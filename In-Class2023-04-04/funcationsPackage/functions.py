# functions.py
import numpy as np

# write a function that accepts an np array and prints the odd-numbered rows only

def print_odd_rows(myArray):
    row_counter = 0 # 0 is my first row
    for row in myArray:
        if row_counter %2 == 1:
            print(row)
        row_counter = row_counter + 1

# write a function that accepts two integers, rows, and columns, and returns an np array of those dimensions of those dimensions randomly inti'd with integer value

def print_random_array(rows, columns):
    newArray = np.random.rand(rows, columns)
    return newArray
    
# write a function that sums the odd-numbered elements in a numpy array of 2-dimensions, return the sum

def sum_odd_array(fArray):
    element_counter = 0 # 0 is the first element and is neither odd or even
    np.shape(fArray,1)
    for element in fArray:
        if element_counter %2 == 1:
            print(sum(element))
        element_counter = element_counter + 1