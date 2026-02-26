## Exercise
## loc and iloc (1)

## Instructions
## - Select the row for Japan (label 'JPN', index 2) as a Series and print it.
## - Select the rows for Australia and Egypt as a DataFrame and print it.

## MY SOLUTION:

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])
