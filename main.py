import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from generate_data import get_data
df = get_data()

# Inizializzazione dell'app Dash
app = dash.Dash(__name__)

###########
# Layout  #
###########
app.layout = html.Div(children=[
    html.H1(children='Dashboard delle Prestazioni Aziendali nel Settore Primario in Sicilia'),

    #Aggiorniamo l'interfaccia ogni 5 secondi
    dcc.Interval(
        id='interval-component',
        interval=5000, 
        n_intervals=0
    ),

    dcc.Graph(id='grafico-temperatura'),
    dcc.Graph(id='grafico-umidita'),
    dcc.Graph(id='grafico-precipitazioni'),
    dcc.Graph(id='grafico-raccolto'),
    dcc.Graph(id='grafico-crescita')
])

# Callback per aggiornare i grafici
@app.callback(
    [Output('grafico-temperatura', 'figure'),
     Output('grafico-umidita', 'figure'),
     Output('grafico-precipitazioni', 'figure'),
     Output('grafico-raccolto', 'figure'),
     Output('grafico-crescita', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    fig_temp = px.line(df, x='Data', y='Temperatura (°C)', title='Temperatura Giornaliera')
    fig_umid = px.line(df, x='Data', y='Umidità (%)', title='Umidità Giornaliera')
    fig_prec = px.line(df, x='Data', y='Precipitazioni (mm)', title='Precipitazioni Giornaliere')
    fig_racc = px.line(df, x='Data', y='Quantità Raccolto (q)', title='Quantità di Raccolto Giornaliera')
    fig_cres = px.line(df, x='Data', y='Tempi Crescita (giorni)', title='Tempi di Crescita')

    return fig_temp, fig_umid, fig_prec, fig_racc, fig_cres

# Esecuzione dell'app
if __name__ == '__main__':
    app.run_server(debug=True)
 