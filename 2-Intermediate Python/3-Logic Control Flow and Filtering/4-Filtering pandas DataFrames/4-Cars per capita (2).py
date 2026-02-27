## Exercise
## Cars per capita (2)

## Instructions
## - Use the code sample provided
##   to create a DataFrame medium.
## - Include all observations of cars
##   that have cars_per_cap between 100 and 500.
## - Use NumPy logical operators if needed.
## - Print out medium.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc=cars['cars_per_cap']
between=np.logical_and(cpc>=100,cpc<=500)
medium=cars[between]

# Print medium
print(medium)
'''