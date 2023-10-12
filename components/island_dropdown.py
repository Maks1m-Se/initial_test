from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids

def render(app: Dash) -> html.Div:
    all_islands = ['Torgersen', 'Biscoe', 'Dream']

    # implementing functionality to add all islands to dropdown
    @app.callback(
        Output(ids.ISLAND_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_ISLANDS_BUTTON, "n_clicks")
    )
    def select_all_islands(_: int) -> list[str]:
        return all_islands
    
    return html.Div(
        children=[
            html.H6('Island'),
            dcc.Dropdown(
                id=ids.ISLAND_DROPDOWN,
                options=[{"label": island, "value": island} for island in all_islands],
                value=all_islands,
                multi=True, # option to select multiple options from dropdown
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_ISLANDS_BUTTON
            )
        ]
    )