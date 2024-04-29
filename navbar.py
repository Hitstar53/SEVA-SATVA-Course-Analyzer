from dash import html
import dash_bootstrap_components as dbc


def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    [
                        # Font Awesome Icon
                        html.I(className="fa-brands fa-github"),
                        " "  # Text beside icon
                    ],
                    href="[YOUR GITHUB PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        # Font Awesome Icon
                        html.I(className="fa-brands fa-medium"),
                        " "  # Text beside icon
                    ],
                    href="[YOUR MEDIUM PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        # Font Awesome Icon
                        html.I(className="fa-brands fa-linkedin"),
                        " "  # Text beside icon
                    ],
                    href="[YOUR LINKEDIN PROFILE URL]",
                    target="_blank"
                )

            ),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[  # Add as many menu items as you need
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Page 2", href='/page2'),
                    dbc.DropdownMenuItem("Page 3", href='/page3'),
                ],
            ),
        ],
        brand='Home',
        brand_href="/",
        # sticky="top",  # Uncomment if you want the navbar to always appear at the top on scroll.
        # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        color="dark",
        # Change this to change color of text within the navbar (False for dark text)
        dark=True,
    )

    return navbar
