## Exercise
## Indexes and values (1)

## Instructions
## - Adapt the for loop
##   to use enumerate()
##   and two iterator variables.
## - Update the print() statement
##   so that on each run
##   a line of the form
##   "room x: y"
##   is printed.
## - x should be the index.
## - y should be the area.
## - Make sure spacing is exact.

## MY SOLUTION:

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas) :
    print('room'+str(index)+':'+str(a))