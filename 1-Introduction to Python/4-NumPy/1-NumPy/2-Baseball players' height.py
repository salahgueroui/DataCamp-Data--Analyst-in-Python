## Exercise
## Baseball players' height

## Instructions
## Create a numpy array from height_in.
## Name this array np_height_in.
## Print np_height_in.
## Multiply np_height_in by 0.0254 to convert inches to meters.
## Store the result in np_height_m.
## Print np_height_m.

## MY SOLUTION:

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in=np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m=np.array(np_height_in*0.0254)

# Print np_height_m
print(np_height_m)