from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px
import pickle
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from tensorflow.keras.models import load_model
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import make_pipeline

from keras.preprocessing.sequence import pad_sequences

import lime
from lime import lime_text
from lime.lime_text import LimeTextExplainer

from app import app, server
from tabs import about, bibliography, classifier, contact, stats, w2v

style = {'maxWidth': '90%', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# Philosophy Text Analysis'),
    dcc.Tabs(id='tabs', value='tab-about', children=[
        dcc.Tab(label='About', value='tab-about'),
        dcc.Tab(label='Classifier', value='tab-classifier'),
        dcc.Tab(label='Text Stats', value='tab-stats'),
        dcc.Tab(label='Word Meanings', value='tab-w2v'),
        dcc.Tab(label='Bibliography', value='tab-bibliography'),
        dcc.Tab(label='Contact', value='tab-contact')
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-about': return about.layout
    elif tab == 'tab-bibliography': return bibliography.layout
    elif tab == 'tab-contact': return contact.layout
    elif tab == 'tab-stats': return stats.layout
    elif tab == 'tab-classifier': return classifier.layout
    elif tab == 'tab-w2v': return w2v.layout

if __name__ == '__main__':
    app.run_server(debug=True)