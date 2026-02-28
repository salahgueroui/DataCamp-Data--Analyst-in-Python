## Exercise
## Loop over DataFrame (1)

## Instructions
## - Write a for loop
##   that iterates over the rows of cars.
## - Use iterrows().
## - On each iteration:
##   - Print the row label.
##   - Print all contents of the row.
## - Use two print() calls.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab,row in cars.iterrows():
    print (lab)
    print (row)
'''    