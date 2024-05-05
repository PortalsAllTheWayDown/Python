#We first import the pyplot module using the alias plt so we dont have to type pyplot repeatedly
import matplotlib.pyplot as plt # type: ignore
#The pyplot module contains a number of functions that generate charts and plots.
#We create a list called squares to hold the data that we'll plot.
x_values = [1,2,3,4,5]
y_values = [1, 4, 9, 16, 25]
#Then we follow another common Matplotlib convention by calling the subplots() function.
#This function can generate one or more plots in the same figure.
#The variable fig represents the entire figure or collection of plots that are generated.
#The variable ax represents a single plot in the figure and is the variable we'll use most of the time
plt.style.use('seaborn-v0_8-ticks')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

#We then use the plot() method, which will try to plot the data its given in a meaningful way.
#The functoin plt.show() opens Matplotlib's viewer and displays the plot.
plt.show()