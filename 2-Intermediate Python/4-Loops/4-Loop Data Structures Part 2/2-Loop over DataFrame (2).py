## Exercise
## Loop over DataFrame (2)

## Instructions
## - Use the iterators lab and row.
## - Adapt the for loop.
## - On the first iteration,
##   it should print:
##   "US: 809"
## - On the second iteration,
##   it should print:
##   "AUS: 731"
## - Output format must be:
##   "country: cars_per_cap"
## - Make sure spacing is exact.
## - Use str() if needed.

## MY SOLUTION:

'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+': '+ str (  row [ 'cars_per_cap']))
'''