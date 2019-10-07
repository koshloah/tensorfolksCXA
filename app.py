import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from blocks.app_header import AppHeaderBlock

server = flask.Flask(__name__)

@server.route("/map")
def map():
    return flask.render_template("map.html", abc=123)

@server.route("/popularity")
def popularity():
    return flask.render_template("popularity.html")

@server.route("/evaluation")
def eval():
    return flask.render_template("evaluation.html")

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css']

app = dash.Dash(
    __name__,
    server = server,
    external_stylesheets=external_stylesheets
    )
app.config.suppress_callback_exceptions = True

### df for 2###
df = pd.read_csv('hello-world-stock.csv')
dfKnn = pd.read_csv('dfKnn.csv')
dfMba = pd.read_csv('dfMba.csv')
dfMba2 = pd.read_csv('dfMba2.csv')
df['Date'] = pd.to_datetime(df.Date, infer_datetime_format=True)
###############

###array for 1###
y_array_dict = {
    'Total Food Demand Forecast': [2, 2, 3],
    'Total Meat Demand Forecast': [1, 2, 4],
    'Total Vegetable Demand Forecast': [3, 3, 5],
    'Total Grain Demand Forecast': [1, 3, 7],
    'Total Dairy Demand Forecast': [3, 3, 3],
}
################

app.layout = html.Div(children=[
    html.Div(id = '1', children =[
    html.H2(className='section-title',
    children='''
        Canteen Food Analytics 
    ''',),

    dcc.Dropdown(
        id='consolidated-dropdown',
        options=[
            {'label': 'Predicted Total Food Demand', 'value': 'Predicted Total Food Demand'},
            {'label': 'Predicted Total Meat Demand', 'value': 'Predicted Total Meat Demand'},
            {'label': 'Predicted Total Vegetables Demand', 'value': 'Predicted Total Vegetables Demand'},
            {'label': 'Predicted Total Grains Demand', 'value': 'Predicted Total Grains Demand'},
            {'label': 'Predicted Total Dairy Demand', 'value': 'Predicted Total Dairy Demand'},
        ],
        value='Predicted Total Food Demand'
    ),
    dcc.Graph(
        id='predict-graph',
        config={
            'showSendToCloud': True,
            'plotlyServerURL': 'https://plot.ly'
        }
    ),

    dcc.Graph(
        id='food-waste-today',
        figure={
            'data': [
                {'x': [1], 'y': [400], 'type': 'bar', 'name': 'Meat'},
                {'x': [1], 'y': [790], 'type': 'bar', 'name': 'Vegetables'},
                {'x': [1], 'y': [832], 'type': 'bar', 'name': 'Grains'},
                {'x': [1], 'y': [215], 'type': 'bar', 'name': 'Dairy'},
            ],
            'layout': {
                'title': 'Food Item Wasted Today (kg)'
            }
        }
    ),
    ], className="container"),

    html.Div(id ='2', children =[
    html.H2(className='section-title',
    children = 'Total Wastage History'),
    html.Div([html.H1("", style={'textAlign': 'center'}),
    dcc.Dropdown(id='my-dropdown',options=[{'label': 'Food wastage', 'value': 'TSLA'}],
        # ,{'label': 'Apple', 'value': 'AAPL'},{'label': 'Coke', 'value': 'COKE'}],
        multi=True,value=['TSLA'],style={"display": "block","margin-left": "auto","margin-right": "auto","width": "60%"}),
    dcc.Graph(id='my-graph')
    ])
    ], className="container"),

    html.Div(id = '3', children=[
    html.H2(className='section-title',
    children = 'Results from K-NN'),
    dash_table.DataTable(
        id='knn-table',
        columns = [{'name':i, "id": i} for i in dfKnn.columns],
        data = dfKnn.to_dict('records'),
        css=[{
        'selector': '.dash-cell div.dash-cell-value',
        'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit; width:100%'
        }],
        style_cell={'textAlign': 'center', 'width':'90%'},
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    ),

    html.H2(className='section-title',
    children = 'Association rules from Market Basket Analysis (Likely to waste)'),
    dash_table.DataTable(
        id='mba-table',
        columns = [{'name':i, "id": i} for i in dfMba.columns],
        data = dfMba.to_dict('records'),
        css=[{
        'selector': '.dash-cell div.dash-cell-value',
        'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit; width:100%'
        }],
        style_cell={'textAlign': 'center', 'width':'15%'},
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Date', 'Region']
        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    ),

    html.H2(className='section-title',
    children = 'Association rules from Market Basket Analysis (Food Combinations likely to have low waste)'),

    dash_table.DataTable(
        id='mba2-table',
        columns = [{'name':i, "id": i} for i in dfMba2.columns],
        data = dfMba2.to_dict('records'),
        css=[{
        'selector': '.dash-cell div.dash-cell-value',
        'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit; width:100%'
        }],
        style_cell={'textAlign': 'center', 'width':'15%'},
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Date', 'Region']
        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )
    ], className= "container"),

    html.Div(id = '4', children=[
        html.A(html.Button('Go to menu planning'), href='/popularity'),
        html.A(html.Button('Go to food item evaluation'), href='/evaluation'),
        html.A(html.Button('Go to admin overview'), href='/map')
    ], className= "container")
])


#####FOR 1#####
@app.callback(
    dash.dependencies.Output('predict-graph', 'figure'),
    [dash.dependencies.Input('consolidated-dropdown', 'value')])
def update_output(value):
    y_array_dict = {
        'Predicted Total Food Demand': [4000,2233,3342,2334,2227,1324,6432,9087],
        'Predicted Total Meat Demand': [6000, 7000, 5321,1215,3432,2345,3523,3535],
        'Predicted Total Vegetables Demand' : [2321, 1232, 1432, 1020, 312,1030,260,450],
        'Predicted Total Grains Demand': [2313, 321, 2123, 5510, 2650,3560, 1240, 2222],
        'Predicted Total Dairy Demand': [2312, 3214, 4123, 2223, 1234, 432, 4231, 3333],
    }
    return {
        'data': [{
            'type': 'scatter',
            'y': y_array_dict[value]
        }],
        'layout': {
            'title': value + ' For Next 7 Days (kg)'
        }
    }
##############################################################################




#####FOR 2###########
@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    dropdown = {"TSLA": "Tesla","AAPL": "Apple","COKE": "Coke",}
    trace1 = []
    trace2 = []
    for stock in selected_dropdown_value:
        trace1.append(go.Scatter(x=df[df["Stock"] == stock]["Date"],y=df[df["Stock"] == stock]["Open"],mode='lines',
            opacity=0.7,name=f'Open {dropdown[stock]}',textposition='bottom center'))
    traces = [trace1, trace2]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
        'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
            height=600,title=f"Amount of Food Wastage"
            # f"{', '.join(str(dropdown[i]) for i in selected_dropdown_value)}"
            f" Over Time (kg)",
            xaxis={"title":"Date",
                   'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 'step': 'month', 'stepmode': 'backward'},
                                                      {'count': 6, 'label': '6M', 'step': 'month', 'stepmode': 'backward'},
                                                      {'step': 'all'}])},
                   'rangeslider': {'visible': True}, 'type': 'date'},yaxis={"title":"Food Wastage (kg)"})}
    return figure
#####################


if __name__ == '__main__':
    app.run_server(debug=True, port=8060)
