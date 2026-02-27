## Exercise
## Driving right (2)

## Instructions
## - The previous example created an intermediate variable dr.
## - Convert the code to a one-liner.
## - Calculate the variable sel as before.
## - Do not create an intermediate variable.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]


# Print sel
print(sel)
'''