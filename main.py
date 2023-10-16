### Main Applicaiton ###
# press CTRL + C to stop app

import pandas as pd
from dash import Dash, dcc, html
from dash_bootstrap_components.themes import BOOTSTRAP 
from palmerpenguins import load_penguins
from components.layout import create_final_layout, create_test_layout

# Path to data; can be than added to layout function
#DATA_PATH = "./data/filename"
#data = load_data(DATA_PATH)
penguins = load_penguins()

# Dash class instance
app = Dash(__name__, external_stylesheets=[BOOTSTRAP])
app.title = "Palmer Penguins"

### Layout application ###
#app.layout = create_layout(app, penguins) #add imported layout function here 
app.layout = create_test_layout(app) #add imported layout function here 
#app.layout = create_final_layout(app, penguins)

# check if skript is main script
# and running the web application
if __name__ == "__main__":
    app.run_server(debug=True) 
    # debug mode enabled; important for dev, should be disabled for production