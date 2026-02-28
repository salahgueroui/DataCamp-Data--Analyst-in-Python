## Exercise
## Determine your next move

## Instructions
## - Roll the dice using randint() and store the result in dice.
## - Complete the if-elif-else structure:
##   * If dice is 1 or 2: go one step down.
##   * If dice is 3, 4 or 5: go one step up.
##   * Else: throw the dice again and go up as many steps as the new dice value.
## - Print out dice and step.

## MY SOLUTION:
'''
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice<=5 :
        step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
'''