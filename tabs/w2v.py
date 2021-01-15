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
        dbc.Input(id="w2v-text-bar", placeholder="enter text to see what words are used in similar contexts", type="text", n_submit=0),
        dbc.Button("SUBMIT", id="w2v-submit-button", color="primary", className="mr-1", n_clicks=0)
    ])

layout = html.Div([
    html.H1("Word Similarity Search"),
    search_bar,
    html.Div(id="w2v-output", children=[]),
])


# callback for search bar
@app.callback(Output(component_id="w2v-output", component_property="children"),
              [Input(component_id="w2v-submit-button", component_property="n_clicks"),
              Input(component_id="w2v-text-bar", component_property="n_submit")],
              [State(component_id="w2v-text-bar", component_property="value")])
def generate_w2v_similarity(n_clicks, n_submit, text):
    if n_clicks < 1 and n_submit < 1:
      return None
    else:
      try:
        similar_words = custom_vectors.most_similar(text)
        heading = f'Words Most Similar to {text.title()}  '
        formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
        head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
        return head_and_list
      except:
        return 'Sorry, that word or phrase is not in the vocabulary'
