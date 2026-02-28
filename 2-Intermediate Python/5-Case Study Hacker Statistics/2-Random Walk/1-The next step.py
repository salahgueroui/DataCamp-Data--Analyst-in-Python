## Exercise
## The next step

## Instructions
## - Create a list random_walk that contains the first step (0).
## - Write a for loop that runs 100 times.
## - On each iteration:
##   * Set step equal to the last element of random_walk (use index -1).
##   * Roll the dice using randint().
##   * Use the if-elif-else structure to update step.
## - Append step to random_walk.
## - Print random_walk.

## MY SOLUTION:
'''
# NumPy is imported, seed is set

# Initialize random_walk
random_walk=[0]
# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step=random_walk[x]
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
'''