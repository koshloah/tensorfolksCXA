import dash_html_components as html


def app_header_layout():
    """Get layout for header

    Returns:
        List of Dash components which constitute the layout of the main component

    """
    return html.Div(
        [
            html.Span(
                "Munch Management",
                className="app-title",
                style={"margin-left": "2%", "margin-top": "0.25%"},
            ),
            html.Div(
                html.Img(src="assets/logo.svg", height="41px"),
                style={"float": "left", "height": "100%", "margin-top": "1%"},
            ),
            html.Div(
                html.A(html.Img(src="assets/logo.svg", height="41px"), href='/'),
                style={"float": "right", "height": "100%", "margin-top": "1%"},
            ),
        ],
        className="row header",
    )
