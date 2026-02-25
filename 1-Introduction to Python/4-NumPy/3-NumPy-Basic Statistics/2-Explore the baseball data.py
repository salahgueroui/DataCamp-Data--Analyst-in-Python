## Exercise
## Explore the baseball data

## Instructions
## - Complete the code for the median height.
## - Use np.std() on the first column of np_baseball
##   to calculate stddev.
## - Use np.corrcoef() to store the correlation between
##   the first and second column of np_baseball in corr.

## MY SOLUTION:
'''
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))
'''