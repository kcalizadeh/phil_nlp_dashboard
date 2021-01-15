import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server

# if __name__ == "__main__":
#     app.run_server(host='localhost', debug=False)