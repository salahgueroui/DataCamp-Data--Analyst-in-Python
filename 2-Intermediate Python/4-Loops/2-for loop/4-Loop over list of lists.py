## Exercise
## Loop over list of lists

## Instructions
## - Write a for loop
##   that goes through each sublist
##   of house.
## - Print out:
##   "the x is y sqm"
## - x should be the room name.
## - y should be the room area.

## MY SOLUTION:

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for name,area in house:
    print('the '+str(name)+ ' is '+ str(area )+ ' sqm')
