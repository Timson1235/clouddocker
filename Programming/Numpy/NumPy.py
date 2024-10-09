#Numpy Programming Quiz
# pylint: disable=no-member
import numpy as np
import numpy_minmax

x = np.arange(5, 21)


# Write a Python function that creates a 5x5 NumPy array filled with random integers between 1 and 100.
#  Then find the maximum and minimum values in the array.

def random_array(x,y,z):
    x = np.random.randint(x, size = (y,z))
    print(x)
    min_val, max_val = numpy_minmax.minmax(x)
    print("min =" ,min_val, "max =", max_val )

random_array(50,2,3)

#Problem: Create a NumPy array with values ranging from 10 to 50. Extract only the even numbers from this array.

def even_numbers(x,y):
    x = np.arange(x,y)
    y = x[x % 2 == 0]
    print(y)

even_numbers(10,26)