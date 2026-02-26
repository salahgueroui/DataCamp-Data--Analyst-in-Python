## Exercise
## CSV to DataFrame (2)

## Instructions
## - Use index_col=0 in pd.read_csv().
## - Print cars again.

## MY SOLUTION:

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)