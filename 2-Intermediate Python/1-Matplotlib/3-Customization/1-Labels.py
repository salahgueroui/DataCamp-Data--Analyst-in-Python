## Exercise
## Labels

## Instructions
## - Use xlab and ylab to set the x- and y-axis labels.
## - Use title to add a title to the plot.
## - Finish with plt.show().

## MY SOLUTION:

'''
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
# Add title
plt.title(title)
# After customizing, display the plot
plt.show()
'''