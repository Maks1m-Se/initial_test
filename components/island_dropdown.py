from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
    all_islands = ['Torgersen', 'Biscoe', 'Dream']
    return html.Div(
        children=[
            html.H6('Island'),
            dcc.Dropdown(
                id=ids.ISLAND_DROPDOWN,
                options=[{"label": island, "value": island} for island in all_islands],
                value=all_islands,
                multi=True, # option to select multiple options from dropdown
            ),
        ]
    )