# Import packages
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Load data
df = pd.read_csv("./data/final.csv")

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Create a pie chart function
def create_pie_chart(df, column):
    fig = px.pie(df, names=column)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font_color="white"
    )
    return fig

# Create a bar chart function
def create_bar_chart(df, x, y):
    fig = px.bar(df, x=x, y=y)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font_color="white"
    )
    return fig

# App layout with dbc components
app.layout = html.Div(
    style={"backgroundColor": "#111111"},
    children=[
        html.H1(
            "SEVA/SATVA Course Analytics Dashboard",
            style={"textAlign": "center", "color": "#7FDBFF", "padding": 20, "font-size": 40, "font-weight": "bold"},
        ),
        dcc.Dropdown(
            id="slct_sem",
            options=[
                {"label": "Semester " + str(i), "value": i} for i in df["sem"].unique()
            ],
            multi=False,
            value=3,
            style={"width": "40%", "color": "#111111", "margin": "auto"},
        ),
        html.Div(id="output_container", children=[]),
        html.Br(),
        dcc.Graph(id="pie_chart", figure={}),
        dcc.Graph(id="bar_chart", figure={}),
        dcc.Graph(id="bar_chart_sem", figure={}),
    ],
)

# Callback function to update charts based on selected semester
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='pie_chart', component_property='figure'),
     Output(component_id='bar_chart', component_property='figure'),
     Output(component_id='bar_chart_sem', component_property='figure')],
    [Input(component_id='slct_sem', component_property='value')]
)

def update_graph(option_slctd):
    # print(option_slctd)
    # print(type(option_slctd))
    container = "The semester chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["sem"] == option_slctd]

    # Pie chart
    pie_chart = create_pie_chart(dff, 'category')
    # Bar chart
    bar_chart = create_bar_chart(dff, 'course', 'category')
    # Bar chart for semester wise category popularity
    bar_chart_sem = create_bar_chart(dff, 'sem', 'category')
    return container, pie_chart, bar_chart, bar_chart_sem


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
