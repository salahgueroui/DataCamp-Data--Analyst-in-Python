## Exercise
## Scatter Plot (1)

## Instructions
## - Change the existing line plot to a scatter plot.
## - Add a logarithmic scale to the x-axis using:
##     plt.xscale('log')
## - Finish with plt.show() to display the plot.

## MY SOLUTION:

'''
# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp)
# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

'''