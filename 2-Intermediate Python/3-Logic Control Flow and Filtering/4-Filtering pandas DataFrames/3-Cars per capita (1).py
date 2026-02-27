## Exercise
## Cars per capita (1)

## Instructions
## - Select the cars_per_cap column from cars
##   as a Pandas Series and store it as cpc.
## - Use cpc with a comparison operator and 500.
## - Create a boolean Series that is True
##   if cars_per_cap is greater than 500,
##   and False otherwise.
## - Store this boolean Series as many_cars.
## - Use many_cars to subset cars,
##   similar to before.
## - Store the result as car_maniac.
## - Print car_maniac.

## MY SOLUTION:

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc=cars['cars_per_cap']
many_cars=cpc>500
car_maniac=cars[many_cars]


# Print car_maniac
print(car_maniac)