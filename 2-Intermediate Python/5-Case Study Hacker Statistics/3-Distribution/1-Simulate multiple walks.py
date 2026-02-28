## Exercise
## Simulate multiple walks

## Instructions
## - Complete the outer for loop so the random walk is simulated 5 times.
## - After each random_walk is fully generated, append it to all_walks.
## - After the top-level for loop, print all_walks.
## - Do not change the initialization of all_walks.

## MY SOLUTION:
'''
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
'''