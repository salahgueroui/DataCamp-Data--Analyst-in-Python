## Exercise
## Square Brackets (2)

## Instructions
## - Print the first 3 rows of cars.
## - Print rows with index 3, 4 and 5.

## MY SOLUTION:

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])