## Exercise
## loc and iloc (3)

## Instructions
## - Print the drives_right column as a Series using loc or iloc.
## - Print the drives_right column as a DataFrame using loc or iloc.
## - Print both the cars_per_cap and drives_right columns as a DataFrame using loc or iloc.

## MY SOLUTION:

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap','drives_right']])

