## Exercise
## Loop over NumPy array

## Instructions
## - Import the numpy package
##   under the alias np.
## - Write a for loop
##   that iterates over all elements
##   in np_height
##   and prints:
##   "x inches"
##   where x is the value.
## - Write a for loop
##   that visits every element
##   of the np_baseball array
##   and prints it out.

## MY SOLUTION:
'''
# Import numpy as np
import numpy as np
# For loop over np_height
for x in np_height:
    print(str(x)+' inches')

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)
'''