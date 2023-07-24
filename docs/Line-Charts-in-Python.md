# Line Charts in Python

1. In the following function call, what does the list [0, 2, 4, 6, 8] represent? `The lower-bound y-values to plot`

   ```python
   plt.fill_between(range(5), [0, 2, 4, 6, 8], [4, 6, 8, 10, 12], alpha=0.2)
   ```

2. Which line of code will create a bar graph with error bars displaying +/- 4 error, with caps of size 10? `plt.bar(x, y, yerr=4, capsize=10)`
3. What is the command to set x-axis ticks to be "Carbohydrates", "Lipids", "Protein"?  `ax.set_xticklabels(["Carbohydrates", "Lipids", "Protein"])`
4. What is the command to plot a bar graph in Matplotlib?   `plt.bar`
5. What is the command to divide the data in a histogram into 10 equally-sized bins?    `plt.hist(data, bins=10)`
6. What are the inputs to the plt.bar function, in order?   `x values (list of numbers), y values (list of numbers)`
7. What is the command to stack a set of bars representing y2 on top of the set of bars representing y1?    `plt.bar(range(len(y2)), y2, bottom=y1)`
8. What is the result of adding autopct='%d%%' to a plt.pie function call?  `The pie chart will now display percentages, rounded to the nearest int, on each slice of the pie.`
9. What does it mean to normalize a histogram?  `Normalizing is dividing the height of each column by a constant such that the area under the curve sums to 1.`
10. What type of graph would work best to display the proportion of team members who own a cat, dog, bird, or no pet? (Assume each team member can only own one pet.) `Pie`
11. What type of graph would work best to display the change in temperature in a city over time?    `Line`
