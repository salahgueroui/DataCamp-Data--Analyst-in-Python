## Exercise
## Motivation for dictionaries

## Instructions
## - Use index() on countries to find the index of 'germany' and store it in ind_ger.
## - Use ind_ger to print the corresponding capital from capitals.

## MY SOLUTION:

## Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger=countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])