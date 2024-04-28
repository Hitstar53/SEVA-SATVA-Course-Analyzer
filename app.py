# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout with dbc
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Gapminder Data Visualization with Dash', style={'textAlign': 'center'}),
            html.Hr(),
            html.P('Select a year:', style={'textAlign': 'center'}),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            ),
            html.Hr(),
            dcc.Graph(id='gapminder-graph')
        ], width=12)
    ])
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
