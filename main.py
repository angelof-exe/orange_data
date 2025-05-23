import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from generate_data import get_data
from istat_data import load_istat_data

df_env = get_data()
df_istat = load_istat_data()

# Inizializzazione dell'app Dash con Bootstrap 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])

# Stile personalizzato
CARD_STYLE = {
    "backgroundColor": "white",
    "boxShadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
    "padding": "15px",
    "borderRadius": "8px",
    "marginBottom": "20px"
}

app.layout = dbc.Container(
    [
        html.Div(style={"backgroundColor": "#FFE0B2", "minHeight": "100vh", "padding": "20px"}, children=[
            
            # Navbar migliorata
            dbc.NavbarSimple(
                brand="OrangeData - Monitoraggio Settore Primario",
                color="dark",
                dark=True,
                className="mb-4"
            ),

            # Grafici esistenti
            dbc.Row([
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-temperatura')], style=CARD_STYLE), md=6),
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-umidita')], style=CARD_STYLE), md=6),
            ]),

            dbc.Row([
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-imprese-settori')], style=CARD_STYLE), md=6),
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-popolazione')], style=CARD_STYLE), md=6),
            ]),

            dbc.Row([
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-attrazione')], style=CARD_STYLE), md=6),
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-poverta')], style=CARD_STYLE), md=6),
            ]),

            # Nuovi grafici aggiunti
            dbc.Row([
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-produttivita')], style=CARD_STYLE), md=6),
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-precipitazioni')], style=CARD_STYLE), md=6),
            ]),

            dbc.Row([
                dbc.Col(dbc.Card([dcc.Graph(id='grafico-disoccupazione')], style=CARD_STYLE), md=6),
            ]),

            # Aggiornamento automatico
            dcc.Interval(id='interval-component', interval=5000, n_intervals=0),
        ])
    ],
    fluid=True
)

@app.callback(
    [
        Output('grafico-temperatura', 'figure'),
        Output('grafico-umidita', 'figure'),
        Output('grafico-imprese-settori', 'figure'),
        Output('grafico-popolazione', 'figure'),
        Output('grafico-attrazione', 'figure'),
        Output('grafico-poverta', 'figure'),
        Output('grafico-produttivita', 'figure'),
        Output('grafico-precipitazioni', 'figure'),
        Output('grafico-disoccupazione', 'figure'),
    ],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    fig_temp = px.line(df_env, x='Data', y='Temperatura (°C)', title='Temperatura Giornaliera')
    fig_temp.update_layout(title={'text': '<b>Temperatura Giornaliera</b>'})

    fig_umid = px.line(df_env, x='Data', y='Umidità (%)', title='Umidità Giornaliera')
    fig_umid.update_layout(title={'text': '<b>Umidità Giornaliera</b>'})

    fig_imprese = px.bar(df_istat, x='Provincia', y=['Imprese Commercio', 'Imprese Agricoltura'], 
                         title='Distribuzione delle Imprese per Settore', barmode='group')
    fig_imprese.update_layout(title={'text': '<b>Distribuzione delle Imprese per Settore</b>'})
    
    fig_pop = px.bar(df_istat, x='Provincia', y=['Popolazione 0-14', 'Popolazione 65+'], 
                     title='Distribuzione della Popolazione per Fascia di Età', barmode='group')
    fig_pop.update_layout(title={'text': '<b>Distribuzione della Popolazione per Fascia di Età</b>'})
    
    fig_attrazione = px.scatter(df_istat, x='Provincia', y='Attrazione (%)', 
                                size='Autocontenimento (%)', color='Autocontenimento (%)',
                                title='Indice di Attrazione e Autocontenimento del Lavoro')
    fig_attrazione.update_layout(title={'text': '<b>Indice di Attrazione e Autocontenimento del Lavoro</b>'})
    
    fig_poverta = px.bar(df_istat, x='Provincia', y='Povertà Relativa (%)', 
                         title='Incidenza della Povertà Relativa per Provincia')
    fig_poverta.update_layout(title={'text': '<b>Incidenza della Povertà Relativa per Provincia</b>'})
    
    fig_produttivita = px.line(df_env, x='Data', y='Indice Produttività', title='Indice di Produttività Agricola')
    fig_produttivita.update_layout(title={'text': '<b>Indice di Produttività Agricola</b>'})

    fig_prec = px.line(df_env, x='Data', y='Precipitazioni (mm)', title='Precipitazioni Giornaliere')
    fig_prec.update_layout(title={'text': '<b>Precipitazioni Giornaliere</b>'})

    fig_disoccupazione = px.bar(df_istat, x='Provincia', y='Disoccupazione Settore Primario (%)', 
                                title='Disoccupazione Settore Primario')
    fig_disoccupazione.update_layout(title={'text': '<b>Disoccupazione Settore Primario</b>'})

    return fig_temp, fig_umid, fig_imprese, fig_pop, fig_attrazione, fig_poverta, fig_produttivita, fig_prec, fig_disoccupazione

if __name__ == '__main__':
    app.run_server(debug=True)
