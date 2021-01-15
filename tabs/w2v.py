from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from tabs.w2v_functions import *

from dash.dependencies import Input, Output, State

from gensim.models import KeyedVectors

school_list = ['plato', 'aristotle', 'capitalism', 'communism',
                'continental', 'empiricism', 'german_idealism', 
                'phenomenology', 'rationalism', 'analytic']

w2v_dict = {}
for school in school_list:
    w2v_dict[school] = KeyedVectors.load(f'model_data\w2v_models\{school}_w2v.wordvectors')
w2v_dict['all'] = KeyedVectors.load('model_data\w2v_models\general_w2v.wordvectors')

layout = html.Div([
  html.H1('Word Similarity'),
  dbc.Row([
    dbc.Col(html.Div([
      dcc.Dropdown(id="w2v-selection-1", 
                  options=get_dropdown_list_w2v(),
                  style={'width': '90%'},
                  placeholder='Start typing to search...'),
      dbc.Input(id='w2v-text-bar-1',
                placeholder="Enter text to see what words are used in similar contexts", 
                type="text", 
                n_submit=0,
                style={'width': '90%'}),
      dbc.Button("SUBMIT", id="w2v-submit-button-1", color="primary", className="mr-1", n_clicks=0),
      html.Div(id="w2v-output-1", children=[])
    ])),
    dbc.Col(html.Div([
      dcc.Dropdown(id="w2v-selection-2", 
                  options=get_dropdown_list_w2v(),
                  style={'width': '90%'},
                  placeholder='Start typing to search...'),
      dbc.Input(id='w2v-text-bar-2',
                placeholder="Enter text to see what words are used in similar contexts", 
                type="text", 
                n_submit=0,
                style={'width': '90%'}),
      dbc.Button("SUBMIT", id="w2v-submit-button-2", color="primary", className="mr-1", n_clicks=0),
      html.Div(id="w2v-output-2", children=[])
    ])),
    dbc.Col(html.Div([
      dcc.Dropdown(id="w2v-selection-3", 
                  options=get_dropdown_list_w2v(),
                  style={'width': '90%'},
                  placeholder='Start typing to search...'),
      dbc.Input(id='w2v-text-bar-3',
                placeholder="Enter text to see what words are used in similar contexts", 
                type="text", 
                n_submit=0,
                style={'width': '90%'}),
      dbc.Button("SUBMIT", id="w2v-submit-button-3", color="primary", className="mr-1", n_clicks=0),
      html.Div(id="w2v-output-3", children=[])
    ]))
  ])
])

@app.callback(Output(component_id="w2v-output-1", component_property="children"),
              [Input(component_id="w2v-submit-button-1", component_property="n_clicks"),
              Input(component_id="w2v-text-bar-1", component_property="n_submit"),
              Input(component_id='w2v-selection-1', component_property='value')],
              [State(component_id="w2v-text-bar-1", component_property="value")])
def generate_similarity_1(n_clicks, n_submit, source_selection, word):
    if n_clicks < 1 and n_submit < 1:
      return None
    else:
      try:
        similar_words = w2v_dict[source_selection].most_similar(word.lower())
        heading = f'Words Most Similar to {word.title()}  '
        formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
        head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
        return head_and_list
      except:
        return 'Sorry, that word or phrase is not in the vocabulary'

@app.callback(Output(component_id="w2v-output-2", component_property="children"),
              [Input(component_id="w2v-submit-button-2", component_property="n_clicks"),
              Input(component_id="w2v-text-bar-2", component_property="n_submit"),
              Input(component_id='w2v-selection-2', component_property='value')],
              [State(component_id="w2v-text-bar-2", component_property="value")])
def generate_similarity_1(n_clicks, n_submit, source_selection, word):
    if n_clicks < 1 and n_submit < 1:
      return None
    else:
      try:
        similar_words = w2v_dict[source_selection].most_similar(word.lower())
        heading = f'Words Most Similar to {word.title()}  '
        formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
        head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
        return head_and_list
      except:
        return 'Sorry, that word or phrase is not in the vocabulary'

@app.callback(Output(component_id="w2v-output-3", component_property="children"),
              [Input(component_id="w2v-submit-button-3", component_property="n_clicks"),
              Input(component_id="w2v-text-bar-3", component_property="n_submit"),
              Input(component_id='w2v-selection-3', component_property='value')],
              [State(component_id="w2v-text-bar-3", component_property="value")])
def generate_similarity_1(n_clicks, n_submit, source_selection, word):
    if n_clicks < 1 and n_submit < 1:
      return None
    else:
      try:
        similar_words = w2v_dict[source_selection].most_similar(word.lower())
        heading = f'Words Most Similar to {word.title()}  '
        formatted = [f'{x[0].title()} - {round(x[1], 3)}  ' for x in similar_words]
        head_and_list = [dcc.Markdown([heading]), dcc.Markdown(formatted)]
        return head_and_list
      except:
        return 'Sorry, that word or phrase is not in the vocabulary'