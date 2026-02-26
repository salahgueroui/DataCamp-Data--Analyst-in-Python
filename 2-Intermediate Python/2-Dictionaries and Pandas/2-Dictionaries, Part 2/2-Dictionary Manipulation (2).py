## Exercise
## Dictionary Manipulation (2)

## Instructions
## - Update germany's capital to 'berlin'.
## - Remove the key 'australia' from europe.
## - Print europe.

## MY SOLUTION:

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany']='berlin'
# Remove australia
del europe['australia']

# Print europe
print(europe)