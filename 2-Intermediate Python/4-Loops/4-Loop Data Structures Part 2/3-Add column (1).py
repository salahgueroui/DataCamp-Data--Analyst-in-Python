## Exercise
## Add column (1)

## Instructions
## - Use a for loop
##   to add a new column
##   named COUNTRY.
## - COUNTRY should contain
##   the uppercase version
##   of the values
##   in the "country" column.
## - Use the string method upper().
## - After the loop,
##   print cars.
## - Do NOT indent the print statement.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,'COUNTRY']= (row['country']).upper()
# Print cars
print(cars)
'''