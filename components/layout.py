# Separat file to build the Dash Layout
# and test different layouts.
# The function should return a html.Div object
# from the dash library.
# The main.py app than imports and
# takes the layout function:
#
#
# from component import my_layout_function
# ...
# app.layout = my_layout_function(app)

from dash import Dash, dcc, html
from . import island_dropdown

### Final layout function ###
def create_layout(app: Dash, data) -> html.Div:
    """
    Create the layout for the Palmer Penguins web application.
    Parameters:
        app (Dash): Dash application instance.
        data (DataFrame): Dataset to be displayed.

    Returns:
        html.Div: The layout of the web application.
    """
    return html.Div(
        className="container",
    children=[       
        html.H1(
            className="text-center mt-4 mb-4",
            children="Palmer Penguins Dataset",
            style={
                "font-size": "2.5rem",
                "margin-left": "auto",
                "margin-right": "auto",
                },
        ),
        html.P(
            className="text-center",
            children=(
                "Size measurements, clutch observations, and blood isotope ratios"
                "for 344 adult foraging Adélie, Chinstrap, and Gentoo penguins"
                "observed on islands in the Palmer Archipelago near Palmer Station, Antarctica."
            ),
            style={
                "font-size": "1.25rem",
                "max-width": "1200px",
                "margin-left": "auto",
                "margin-right": "auto",
                },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["flipper_length_mm"],
                        "y": data["body_mass_g"],
                        "mode": "markers",
                        "marker": {"color": "blue"},
                    },
                ],
                "layout": {
                    "title": "Body mass over flipper length",
                    "xaxis": {"title": "Flipper Length (mm)"},
                    "yaxis": {"title": "Body Mass (g)"},
                },
            },
            style={
                "max-width": "1200px",
                "margin-left": "auto",
                "margin-right": "auto",
            },
        ),
        html.Div(
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": data["species"],
                            "y": data["body_mass_g"],
                            "type": "box",
                            "boxmode": "group",
                            "marker": {"color": "green"},
                        },
                    ],
                    "layout": {
                        "title": "Body mass by species",
                        "xaxis": {"title": "Species"},
                        "yaxis": {"title": "Body Mass (g)"},
                    },
                },
            ),
            style={
                "max-width": "800px",
                "margin-left": "auto",
                "margin-right": "auto",
            },
        ),
        # ... more components here
    ],
)

### Test layout ###
def create_test_layout(app: Dash) -> html.Div:
    """
    Create a simple test layout for the Dash application.
    Parameters:
        app (Dash): The Dash application instance.
    Returns:
        html.Div: The layout of the test page.
    """
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container", children=[island_dropdown.render(app)]
            ),
        ],
    )