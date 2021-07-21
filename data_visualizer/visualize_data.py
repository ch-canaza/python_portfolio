""" 
module created to show skills in data processing and visualization
"""
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, FB, GOOG


# file to save the model
output_file('data.html')


# instantiate the figure object
graphics = figure(x_axis_type = 'datetime', title = 'Stock Closing Prices')

# x axis
graphics.xaxis.axis_label = 'Date'

#y axis
graphics.yaxis.axis_label = 'Price (in USD)'

#plotting the graphs for Apple
x_axis_coordinates = np.array(AAPL['date'], dtype = np.datetime64)

y_axis_coordinates = AAPL['adj_close']

color = 'blue'
legend_label = 'AAPL'
graphics.line(
              x_axis_coordinates, 
              y_axis_coordinates, 
              color = color, 
              legend_label = legend_label
            )

# plotting line for Facebook
x_axis_coordinates = np.array(FB['date'], dtype = np.datetime64)

y_axis_coordinates = FB['adj_close']

color = 'black'
legend_label = 'FB'
graphics.line(
              x_axis_coordinates, 
              y_axis_coordinates, 
              color = color, 
              legend_label = legend_label
            )
# plotting line for Facebook
x_axis_coordinates = np.array(GOOG['date'], dtype = np.datetime64)

y_axis_coordinates = GOOG['adj_close']

color = 'red'
legend_label = 'GOOG'
graphics.line(x_axis_coordinates, y_axis_coordinates, color = color, legend_label = legend_label)

# relocating legend table to avoid obstruction of the graph
graphics.legend.location = 'top_left'

#displaying the model
show(graphics)