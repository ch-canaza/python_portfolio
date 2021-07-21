import pytest
import pytest_mock
import requests_mock
from mock import MagicMock
import os
from visualize_data import graphics, x_axis_coordinates, y_axis_coordinates
import numpy as np
import bokeh
import requests

mock = MagicMock()

xaxis = mock.__iter__.return_value = range(100)
yaxis = mock.__iter__.return_value = range(100)

my_graphics = graphics.line(
                            xaxis,
                            yaxis,
                            color = 'red',
                            legend_label = 'test_label'
                            )

def test_output_file_has_been_created():
    assert os.path.isfile('data.html')

def test_graphiccs_xaxis_label_must_be_date():
    assert graphics.xaxis.axis_label == 'Date'

def test_graphics_yaxis_label_must_be_price_usd():
    assert graphics.yaxis.axis_label == 'Price (in USD)'

def test_any_element_in_x_axis_coordinates_is_type_datetime64():
    assert type(x_axis_coordinates[0]) == np.datetime64 
    assert type(x_axis_coordinates[5]) == np.datetime64 
    assert type(x_axis_coordinates[13]) == np.datetime64 
    assert type(x_axis_coordinates[25]) == np.datetime64

def test_any_element_in_x_axis_coordinates_is_type_date():
    assert type(y_axis_coordinates[0]) == float 
    assert type(y_axis_coordinates[5]) == float 
    assert type(y_axis_coordinates[13]) == float 
    assert type(y_axis_coordinates[25]) == float 
    
def test_type_generated_graphics_instance():
    assert type(my_graphics) == bokeh.models.renderers.GlyphRenderer

def test_legend_location():
    assert graphics.legend.location == 'top_left'

def test_correct_HTML_response(requests_mock):
    requests_mock.get("http://your/custom/file/path", text="data")
    response = requests.get("http://your/custom/file/path")

    assert response.text == "data"