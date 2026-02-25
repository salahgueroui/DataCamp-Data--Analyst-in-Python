## Exercise
## Your First 2D NumPy Array

## Instructions
## Use np.array() to create a 2D numpy array from baseball.
## Name it np_baseball.
## Print out the type of np_baseball.
## Print out the shape attribute of np_baseball
## using np_baseball.shape.

## MY SOLUTION:

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array([[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]])

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)