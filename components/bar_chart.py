from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
from . import ids
from dash.dependencies import Input, Output
from palmerpenguins import load_penguins


penguins = load_penguins()

def render(app: Dash)-> html.Div:

    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.ISLAND_DROPDOWN, "value")
    )
    def update_bar_chart(islands: list[str]) -> html.Div:
        # preparing data
        peng_gb_year_island_cnt = penguins.groupby(['year', 'island']).count()
        peng_gb_year_island_cnt = peng_gb_year_island_cnt.reset_index()
        peng_gb_year_island_cnt = peng_gb_year_island_cnt  \
                            .rename(columns={'species':'count'}) \
                            .loc[:, ['year', 'island', 'count']]
        # filter data
        filtered_data = peng_gb_year_island_cnt.query("island in @islands")
        if filtered_data.shape[0] == 0: # message if no data selected
            return html.Div("No data selected. Choose at least one island.")

        fig = px.bar(filtered_data,
                    x='year',
                    y='count',
                    color='island', text='island')
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    return html.Div(id=ids.BAR_CHART)