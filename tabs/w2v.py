from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

from dash.dependencies import Input, Output, State

from gensim.models import KeyedVectors


custom_vectors = KeyedVectors.load('model_data\w2v_models\german_idealism_w2v.wordvectors')

search_bar = html.Div(id="w2v-bar-container", children=
    [
        dbc.Input(id="w2v-bar", placeholder="enter text to see what words are used in similar contexts", type="text"),
        dbc.Button("SUBMIT", id="w2v-bar-submit-button", color="primary", className="mr-1", n_clicks=0)
    ])

layout = html.Div([
    html.H1("Word Similarity Search"),
    search_bar,
    html.Div(id="w2v-bar-output", children=[])  
])


# callback for search bar
@app.callback(Output(component_id="w2v-bar-output", component_property="children"),
              [Input(component_id="w2v-bar-submit-button", component_property="n_clicks")],
              [State(component_id="w2v-bar", component_property="value")])
def generate_explainer_html(n_clicks, text):
    empty_obj = html.Iframe(
        srcDoc='''<div>Enter input text to see LIME explanations.</div>''',
        width='100%',
        height='100px',
        style={'border': '2px #d3d3d3 solid'},
        hidden=True,
    )
    if n_clicks < 1 or text == '':
      return empty_obj
    else:
      try:
        similar_words = custom_vectors.most_similar(text)
        formatted = [f'{x[0].title()}, {round(x[1], 3)}\t\n\n' for x in similar_words]
        joined = '\n- '.join(formatted)
        return joined
      except:
        return 'Sorry, that word or phrase is not in the vocabulary'