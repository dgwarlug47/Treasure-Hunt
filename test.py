# Import Library

import matplotlib.pyplot as plt
  
# Define Data

x= [1, 2, 3, 5]
y= [9, 15, 20, 25]

# Plot error bar

plt.errorbar(x, y, xerr = 0.9, fmt = 'o',color = 'orange', 
            ecolor = 'lightgreen', elinewidth = 5, capsize=10)

# Display graph

plt.show()