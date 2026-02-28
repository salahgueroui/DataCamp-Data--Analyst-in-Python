## Exercise
## Roll the dice

## Instructions
## - Use randint() with the appropriate arguments
##   to randomly generate the integer 1, 2, 3, 4, 5 or 6.
## - Print the result.
## - Repeat the outcome to see if the second throw is different.
## - Print the second result.

## MY SOLUTION:
'''
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))
'''