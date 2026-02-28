## Exercise
## Add conditionals

## Instructions
## - Initialize offset to -6.
## - Inside the while loop, complete the if-else statement:
##   - If offset is greater than zero,
##     decrease offset by 1.
##   - Else,
##     increase offset by 1.
## - Make sure offset != 0 eventually becomes False.

## MY SOLUTION:

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset=offset-1
    else : 
      offset=offset+1    
    print(offset)