## Exercise
## Add column (2)

## Instructions
## - Replace the for loop
##   with a one-liner
##   that uses:
##   .apply(str.upper)
## - The result should add
##   a new column COUNTRY
##   to cars,
##   containing uppercase
##   versions of the country names.
## - Print cars
##   after adding the column.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
#for lab, row in cars.iterrows() :
#    cars.loc[lab, "COUNTRY"] = row["country"].upper()

cars['COUNTRY']=cars["country"].apply(str.upper)
'''