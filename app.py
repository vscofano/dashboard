import dash
import dash_bootstrap_components as dbc
from dash import dcc,html,callback,Input,Output
import plotly.express as px
from workers import pipeline


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.Div(
            [
                # menu esquerdo
                dbc.Col(
                    [
                        html.H2("Título Dashboard", className="left-menu"),
                        html.Hr(),
                        dbc.Nav(
                            [
                                dcc.Dropdown(
                                    id='choice-menu',  
                                    options=[
                                        {
                                            "label": html.Span(
                                                [
                                                    html.Img(src="/assets/images/everybody.png", height=20),
                                                    html.Span("Todos", style={'color': '#000000', 'font-size': 20, 'padding-left': 10}),
                                                ], style={'align-items': 'center', 'justify-content': 'center'}
                                            ),
                                            "value": "Todos",
                                        },
                                        {
                                            "label": html.Span(
                                                [
                                                    html.Img(src="/assets/images/womens.png", height=20),
                                                    html.Span("Mulheres", style={'color': '#000000', 'font-size': 20, 'padding-left': 10}),
                                                ], style={'align-items': 'center', 'justify-content': 'center'}
                                            ),
                                            "value": "Mulheres",
                                        },
                                        {
                                            "label": html.Span(
                                                [
                                                    html.Img(src="/assets/images/mens.png", height=20),
                                                    html.Span("Homens", style={'color': '#000000', 'font-size': 20, 'padding-left': 10}),
                                                ], style={'align-items': 'center', 'justify-content': 'center'}
                                            ),
                                            "value": "Homens",
                                        },
                                    ],
                                    placeholder='Filtros',
                                    style={'background-color': '#061E44'}
                                ),
                            ],
                            vertical=True,
                            pills=True,
                            style={'background-color': '#061E44'}
                        ),
                    ], class_name="menu"
                ),
            ], className="div_1 col-2",
        ),
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '350px'}, className="grafico", id='grafico_6'),
                                dcc.Graph(style={'height': '250px'}, className="grafico", id='grafico_4'),
                            ], className=("graph-container col-4")
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '600px'}, className="grafico", id="grafico_5"),
                            ], className=("graph-container col-7")
                        ),
                    ], class_name="mt-3 graphs_1 col-10"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '650px'}, className="grafico", id="grafico_2"),
                            ], className=("graph-container col-7")
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '350px'}, className="grafico", id='grafico_3'),
                                dcc.Graph(style={'height': '300px'}, className="grafico", id='pizza_2'),
                            ], className=("graph-container col-4")
                        ),
                    ], class_name="mt-3 graphs_1 col-10"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '400px'}, className="grafico", id='pizza_1'),
                            ], className=("graph-container col-7")
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(style={'height': '400px'}, className="grafico", id='grafico_1'),
                            ], className=("graph-container col-4")
                        )
                    ], class_name="mt-3 graphs_1 col-10"
                ),
            ]
        ),
    ], fluid=True, class_name=("pai")
)

@callback(
    Output('grafico_1', 'figure'),
    Output('grafico_2', 'figure'),
    Output('grafico_3', 'figure'),
    Output('grafico_4', 'figure'),
    Output('grafico_5', 'figure'),
    Output('grafico_6', 'figure'),
    Output('pizza_1', 'figure'),
    Output('pizza_2', 'figure'),
    Input('choice-menu', 'value')
)
def update_graphs(input_value):
    if input_value == 'Mulheres':
        fig_hierarchy, fig_post, fig_shift, fig_afast = pipeline.bar_graph_womens()
        fig_company, fig_gender, fig_sanitary = pipeline.pie_graph_womens()
        fig_ala = pipeline.dispersion_womens()
    elif input_value == 'Homens':
        fig_hierarchy, fig_post, fig_shift, fig_afast = pipeline.bar_graph_mens()
        fig_company, fig_gender, fig_sanitary = pipeline.pie_graph_mens()
        fig_ala = pipeline.dispersion_mens()
    else:
        fig_hierarchy, fig_post, fig_shift, fig_afast = pipeline.bar_graph()
        fig_company, fig_gender, fig_sanitary = pipeline.pie_graph()
        fig_ala = pipeline.dispersion()

    figs = [fig_hierarchy, fig_post, fig_shift, fig_afast, fig_company, fig_gender, fig_sanitary, fig_ala]
    for fig in figs:
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    return figs


if __name__ == "__main__":
    app.run_server(debug=True)





