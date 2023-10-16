from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
from . import ids
from palmerpenguins import load_penguins


penguins = load_penguins() 

def render(app: Dash)-> html.Div:
    ct_plot_penguins = pd.crosstab(penguins.year, 'count')
    fig = px.bar(ct_plot_penguins, x='year', y='count', text='Year of sample collection')
    return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)