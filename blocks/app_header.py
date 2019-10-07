import dash_html_components as html

from blocks.base import BaseBlock


class AppHeaderBlock(BaseBlock):
    def __init__(self, app):
        BaseBlock.__init__(self, app)
        self.layout = html.Div(
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
                    html.A(html.Img(src="assets/home.svg", height="41px"), href='/'),
                    style={"float": "right", "height": "100%", "margin-top": "1%"},
                ),
            ],
            className="row header",
        )

    def callbacks(self, app):
        pass
