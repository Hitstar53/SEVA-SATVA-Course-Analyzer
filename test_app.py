import pytest
import pandas as pd
from dash import html
from unittest.mock import patch
from dash.testing.application_runners import import_app
from app import update_options, render_content

def test_app():
    app = import_app('app')  
    # Write your tests here
    assert app is not None

def test_server_starts():
    app = import_app('app')
    assert app.server is not None

@patch("app.get_df")
def test_update_options(mock_get_df):
    # Create a mock DataFrame
    mock_df = pd.DataFrame(
        {"sem": [1, 3, 4, 2], "branch": ["ETRX", "IT", "EXTC", "COMP"]}
    )
    mock_get_df.return_value = mock_df

    # Call update_options with a dummy selected_period
    sem_options, branch_options = update_options("ALL")

    # Assert that the returned options are as expected
    expected_sem_options = [
        {"label": "ALL", "value": 0},
        {"label": "1", "value": 1},
        {"label": "3", "value": 3},
        {"label": "4", "value": 4},
        {"label": "2", "value": 2},
    ]
    assert sem_options == expected_sem_options

    expected_branch_options = [
        {"label": "ALL", "value": "ALL"},
        {"label": "ETRX", "value": "ETRX"},
        {"label": "IT", "value": "IT"},
        {"label": "EXTC", "value": "EXTC"},
        {"label": "COMP", "value": "COMP"},
    ]
    assert branch_options == expected_branch_options


# render content
def test_render_content():
    # Test for tab-1
    result = render_content("tab-1")
    assert isinstance(result, html.Div)

    # Test for tab-2
    result = render_content("tab-2")
    assert isinstance(result, html.Div)

    # Test for tab-3
    result = render_content("tab-3")
    assert isinstance(result, html.Div)

    # Test for an invalid tab
    result = render_content("invalid")
    assert result is None
