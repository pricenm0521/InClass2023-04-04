# main.py
import numpy as np
from funcationsPackage.functions import *

# test the function
# cobble up a numpy array, invoke the function

ourArray = np.arange(20,50).reshape(10,3)
print_odd_rows(ourArray)

ffArray = np.arange(20).reshape(4,5)
sum_odd_array(ffArray)
