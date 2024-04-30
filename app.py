# Import packages
import os
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dash_table, dcc, callback, Output, Input, dash_table
from db import load_data
import warnings

warnings.filterwarnings("ignore")

# Load data
main_data = load_data()
courses_path = os.path.join("data", "courses.csv")
course_category = pd.read_csv(courses_path)

# Initialize the app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

server = app.server

year_22_23_df = main_data[
    (main_data["period"] == "ODD_SEM_22_23") | (main_data["period"] == "EVEN_SEM_22_23")
]

year_23_24_df = main_data[
    (main_data["period"] == "ODD_SEM_23_24") | (main_data["period"] == "EVEN_SEM_23_24")
]

period_df = {
    "ODD_SEM_22_23": main_data[main_data["period"] == "ODD_SEM_22_23"],
    "EVEN_SEM_22_23": main_data[main_data["period"] == "EVEN_SEM_22_23"],
    "ODD_SEM_23_24": main_data[main_data["period"] == "ODD_SEM_23_24"],
    "EVEN_SEM_23_24": main_data[main_data["period"] == "EVEN_SEM_23_24"],
}


def get_df(selected_period):
    if selected_period == "ALL_TIME":
        return main_data
    if "SEM" in selected_period:
        selected_period = selected_period
        return period_df[selected_period]
    elif selected_period == "YEAR_22_23":
        return year_22_23_df
    else:
        return year_23_24_df


# Create a pie chart function
def create_pie_chart(df, column):
    fig = px.pie(df, names=column)
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font_color="white",
    )
    return fig


# Create a bar chart function
def create_bar_chart(df, x, y):
    fig = px.bar(df, x=x, y=y)
    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        font_color="white",
    )
    return fig


# App layout with dbc components
app.layout = html.Div(
    style={
        "backgroundColor": "#18181B",
        "padding": 20,
        "color": "#7FDBFF",
    },
    children=[
        html.H1(
            "SEVA/SATVA Course Analytics Dashboard",
            style={
                "textAlign": "center",
                "color": "#7FDBFF",
                "padding-top": "2rem",
                "padding-bottom": "2rem",
                "font-size": "3em",
                "font-weight": "bold",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label(
                            "Select period to analyse:",
                            style={
                                "color": "#7FDBFF",
                                "font-size": 25,
                                # "padding": 20,
                                "text-align": "center",
                            },
                        ),
                    ],
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="period",
                            options=[
                                {"label": "All time", "value": "ALL_TIME"},
                                {
                                    "label": "Odd Semester 2022-23",
                                    "value": "ODD_SEM_22_23",
                                },
                                {
                                    "label": "Even Semester 2022-23",
                                    "value": "EVEN_SEM_22_23",
                                },
                                {
                                    "label": "Odd Semester 2023-24",
                                    "value": "ODD_SEM_23_24",
                                },
                                {
                                    "label": "Even Semester 2023-24",
                                    "value": "EVEN_SEM_23_24",
                                },
                                {
                                    "label": "Academic year 2022-23",
                                    "value": "YEAR_22_23",
                                },
                                {
                                    "label": "Academic year 2023-24",
                                    "value": "YEAR_23_24",
                                },
                            ],
                            multi=False,
                            value="ALL_TIME",
                            style={
                                "color": "#111111",
                                # "padding": 10,
                                "text-align": "center",
                            },
                        ),
                    ],
                    # width={"size": 3, "offset": 0},
                    style={
                        "height": "80%",
                    },
                    # width={"size": 4, "offset": 1},
                ),
            ],
        ),
        dcc.Tabs(
            id="tabs-example-1",
            value="tab-1",
            children=[
                dcc.Tab(
                    label="At a glance",
                    value="tab-1",
                    style={
                        "margin": "10px",
                        "padding": "10px",
                        "border-radius": "15px",
                        # "backgroundColor": "222.2 47.4% 11.2%",
                        #
                    },
                ),
                dcc.Tab(
                    label="Overall",
                    value="tab-2",
                    style={
                        "margin": "10px",
                        "padding": "10px",
                        "border-radius": "15px",
                    },
                ),
                dcc.Tab(
                    label="Course",
                    value="tab-3",
                    style={
                        "margin": "10px",
                        "padding": "10px",
                        "border-radius": "15px",
                    },
                ),
            ],
            style={
                "padding": 20,
                "display": "flex",
                "justify-content": "space-evenly",
                "align-items": "center",
                "border-radius": "15px",
            },
        ),
        html.Div(
            id="tabs-example-content-1",
            style={
                "padding": 20,
            },
        ),
    ],
)

# @callback(in("period", "value"))
# def update_view():
#     if value == "overall":


@callback(
    Output("tabs-example-content-1", "children"),
    Input("tabs-example-1", "value"),
)
def render_content(tab):
    if tab == "tab-3":
        return html.Div(
            # [
            #     dbc.Row(
            #         [
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Semester",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_sem",
            #                         options=[
            #                             {"label": "Semester " + str(i), "value": i}
            #                             for i in range(1, 9)
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={
            #                             "width": "100%",
            #                             "color": "#111111",
            #                             "padding": 5,
            #                         },
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Branch",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_branch",
            #                         options=[
            #                             {"label": str(i), "value": i}
            #                             for i in main_data["branch"].unique()
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={
            #                             "width": "100%",
            #                             "color": "#111111",
            #                             "padding": 5,
            #                         },
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Category",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_cat",
            #                         options=[
            #                             {"label": "Category " + str(i), "value": i}
            #                             for i in main_data["category"].unique()
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={
            #                             "width": "100%",
            #                             "color": "#111111",
            #                             "padding": 5,
            #                         },
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #         ],
            #         justify="center",
            #         # style={"backgroundColor": "#333333", "padding": "10px"},
            #     ),
            #     html.Br(),
            #     dbc.Row(
            #         [
            #             dbc.Col(dcc.Graph(id="pie_chart", figure={}), width=6),
            #             dbc.Col(dcc.Graph(id="bar_chart", figure={}), width=6),
            #         ],
            #         style={"backgroundColor": "#333333", "padding": "10px"},
            #     ),
            #     dbc.Row(
            #         [
            #             dbc.Col(dcc.Graph(id="bar_chart_sem", figure={}), width=6),
            #             # dbc.Col(dcc.Graph(id="sunburst_chart", figure={}), width=6),
            #         ],
            #         style={"backgroundColor": "#333333", "padding": "10px"},
            #     ),
            # ]
        )

        # dbc.Row(
        #     [
        #         dbc.Col(dcc.Graph(id="line_chart", figure={}), width=6),
        #         dbc.Col(dcc.Graph(id="hbar_chart", figure={}), width=6),
        #     ],
        #     style={"backgroundColor": "#333333", "padding": "10px"},
        # ),
    elif tab == "tab-2":
        return html.Div(
            # [
            #     dbc.Row(
            #         [
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Semester",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_sem",
            #                         options=[
            #                             {"label": "Semester " + str(i), "value": i}
            #                             for i in main_data["sem"].unique()
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={"width": "100%", "color": "#111111"},
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Branch",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_branch",
            #                         options=[
            #                             {"label": str(i), "value": i}
            #                             for i in main_data["branch"].unique()
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={"width": "100%", "color": "#111111"},
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #             dbc.Col(
            #                 [
            #                     html.Label(
            #                         "Select Category",
            #                         style={"color": "#7FDBFF"},
            #                     ),
            #                     dcc.Dropdown(
            #                         id="slct_cat",
            #                         options=[
            #                             {"label": "Category " + str(i), "value": i}
            #                             for i in main_data["category"].unique()
            #                         ],
            #                         multi=False,
            #                         value=1,
            #                         style={"width": "100%", "color": "#111111"},
            #                     ),
            #                 ],
            #                 width=4,
            #             ),
            #         ],
            #         justify="center",
            #         # style={"backgroundColor": "#333333", "padding": "10px"},
            #     ),
            #     html.H3("Tab content 2"),
            #     dcc.Graph(
            #         figure=dict(data=[dict(x=[1, 2, 3], y=[5, 10, 6], type="bar")])
            #     ),
            # ]
        )
    elif tab == "tab-1":
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label(
                                    "Select Semester",
                                    style={"color": "#7FDBFF"},
                                ),
                                dcc.Dropdown(
                                    id="sem-tab-3",
                                    options=[{"label": "ALL", "value": 0}],
                                    multi=False,
                                    value=0,
                                    style={
                                        # "width": "75%",
                                        "color": "#111111",
                                        "font-size": "18px",
                                        "border-radius": "7px",
                                        # "padding":"10px",
                                    },
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                html.Label(
                                    "Select Branch",
                                    style={"color": "#7FDBFF"},
                                ),
                                dcc.Dropdown(
                                    id="branch-tab-3",
                                    options=[{"label": "ALL", "value": "ALL"}],
                                    multi=False,
                                    value="ALL",
                                    style={
                                        # "width": "50%",
                                        "color": "#111111",
                                        "font-size": "18px",
                                        "border-radius": "7px",
                                    },
                                ),
                            ],
                            width=4,
                        ),
                    ],
                    # justify="center",
                    style={
                        "backgroundColor": "transperent",
                        # "padding": "10px",
                        "display": "flex",
                        "justify-content": "space-evenly",
                        "align-items": "center",
                        "padding": "15px",
                    },
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id="horizontal-bar-tab-3", figure={}),
                        ),
                    ],
                    style={
                        "padding": 5,
                        "margin": "5px",
                        "border-radius": "10px",
                        "backgroundColor": "#333333",
                    },
                    align="center",
                    justify="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id="pie-category-wise-tab-3", figure={}), width=8
                        ),
                    ],
                    style={
                        "backgroundColor": "#333333",
                        "padding": "10px",
                        "margin": "5px",
                        "border-radius": "10px",
                    },
                ),
                dbc.Row(
                    [
                        # dbc.Col(dcc.Graph(id="bar_chart_sem", figure={}), width=6),
                        # dbc.Col(dcc.Graph(id="sunburst_chart", figure={}), width=6),
                    ],
                    style={
                        "backgroundColor": "#333333",
                        "padding": "10px",
                        "margin": "5px",
                        "border-radius": "10px",
                    },
                ),
                # dcc.Graph(
                #     figure=dict(data=[dict(x=[1, 2, 3], y=[15, 110, 160], type="bar")])
                # ),
            ],
        )


# Callback function to update charts based on selected semester
# @app.callback(
#     [
#         Output(component_id="pie_chart", component_property="figure"),
#         Output(component_id="bar_chart", component_property="figure"),
#         Output(component_id="bar_chart_sem", component_property="figure"),
#     ],
#     [
#         Input(component_id="period", component_property="value"),
#         Input(component_id="slct_sem", component_property="value"),
#         Input(component_id="slct_branch", component_property="value"),
#         Input(component_id="slct_cat", component_property="value"),
#     ],
# )
# def update_graph(selected_period, option_slctd, branch, cat):
#     # print(option_slctd)

#     dff = get_df(selected_period)

#     # Pie chart
#     pie_chart = create_pie_chart(dff, "category")
#     # Bar chart
#     bar_chart = create_bar_chart(dff, "course", "category")
#     # Bar chart for semester wise category popularity
#     bar_chart_sem = create_bar_chart(dff, "sem", "category")
#     return pie_chart, bar_chart, bar_chart_sem


# this is for tab 3:
# Callback function to update charts based on selected semester
@app.callback(
    [
        Output(component_id="horizontal-bar-tab-3", component_property="figure"),
        Output(component_id="pie-category-wise-tab-3", component_property="figure"),
        # Output(component_id="bar_chart_sem", component_property="figure"),
    ],
    [
        Input(component_id="period", component_property="value"),
        Input(component_id="sem-tab-3", component_property="value"),
        Input(component_id="branch-tab-3", component_property="value"),
    ],
)
def update_graph_tab_3(selected_period, sem, branch):
    df = get_df(selected_period)
    if sem != 0:
        df = df[df["sem"] == sem]
    if branch != "ALL":
        df = df[df["branch"] == branch]

    # Horizontal bar chart
    # pie_chart_1 = create_pie_chart(df, "course")
    x = df.groupby("course")["uid"].count().sort_values(ascending=True)
    x.name = "Count of students"
    x = (
        pd.merge(x, course_category, left_index=True, right_on="course_name")
        .dropna()
        .sort_values(by="Count of students", ascending=True)
    )
    x = x[x["Count of students"] > 0]
    x.rename(columns={"course_name": "Course"}, inplace=True)
    hor_bar_1 = px.bar(
        x, x="Count of students", y="Course", orientation="h", color="category"
    )
    hor_bar_1.update_layout(height=1500)
    # Bar chart
    pie_chart_2 = create_pie_chart(df, "category")
    # # Bar chart for semester wise category popularity
    # bar_chart_sem = create_bar_chart(df, "sem", "category")
    return hor_bar_1, pie_chart_2


# call backs to update dropdown options
@app.callback(
    [
        Output(component_id="sem-tab-3", component_property="options"),
        Output(component_id="branch-tab-3", component_property="options"),
        # Output(component_id="bar_chart_sem", component_property="figure"),
    ],
    [
        Input(component_id="period", component_property="value"),
    ],
)
def update_options(selected_period):
    df = get_df(selected_period)
    sem_options = [{"label": "ALL", "value": 0}]
    sem_options += [{"label": str(i), "value": i} for i in df["sem"].unique()]
    branch_options = [{"label": "ALL", "value": "ALL"}]
    branch_options += [{"label": str(i), "value": i} for i in df["branch"].unique()]
    return sem_options, branch_options


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
