## Exercise
## Loop over dictionary

## Instructions
## - Write a for loop
##   that goes through each key:value pair
##   of europe.
## - On each iteration,
##   print:
##   "the capital of x is y"
## - x should be the key.
## - y should be the value.

## MY SOLUTION:

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key,value in europe.items():
    print('the capital of '+key+' is '+ str(value))


