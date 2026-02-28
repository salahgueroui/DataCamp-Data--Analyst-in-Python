## Exercise
## Indexes and values (2)

## Instructions
## - Adapt the print() function
##   in the for loop
##   so that counting starts at 1.
## - The first output should be:
##   "room 1: 11.25"
## - The second output should be:
##   "room 2: 18.0"
## - Continue this pattern
##   for all elements.

## MY SOLUTION:

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))