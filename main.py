### Main Applicaiton ###
# press CTRL + C to stop app

import pandas as pd
from dash import Dash, dcc, html
from dash_bootstrap_components.themes import BOOTSTRAP
from palmerpenguins import load_penguins
from components.layout import create_layout, create_test_layout


# Read data
penguins = load_penguins() #<class 'pandas.core.frame.DataFrame'>
#print(data)


# Dash class instance
app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
app.title = "Palmer Penguins"

### Layout application ###
app.layout = create_layout(app, penguins) #add imported layout function here 

# check if skript is main script
# and running the web application
if __name__ == "__main__":
    app.run_server(debug=True) 
    # debug mode enabled; important for dev, should be disabled for production