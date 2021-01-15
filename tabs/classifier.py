from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
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

from app import app

class TextsToSequences(BaseEstimator, TransformerMixin):
    def __init__(self,  tokenizer):
        self.tokenizer = tokenizer
        
    def fit(self, texts, y=None):
        return self
    
    def transform(self, texts, y=None):
        return np.array(self.tokenizer.texts_to_sequences(texts))


class Padder(BaseEstimator, TransformerMixin):
    def __init__(self, maxlen=500):
        self.maxlen = maxlen
        self.max_index = None
        
    def fit(self, X, y=None):
        self.max_index = pad_sequences(X, maxlen=self.maxlen).max()
        return self
    
    def transform(self, X, y=None):
        X = pad_sequences(X, maxlen=self.maxlen)
        return X

model_path = 'model_data\\NN_weights_epoch_09_0.7928.hdf5'
model = load_model(model_path)

with open('model_data\gru_tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# set up classification explanation pipeline
padder = Padder(450)
sequencer = TextsToSequences(tokenizer)
pipeline = make_pipeline(sequencer, padder, model)

# set up labels
school_label_dict = {'analytic': 0,
 'aristotle': 1,
 'capitalism': 2,
 'communism': 3,
 'continental': 4,
 'empiricism': 5,
 'german_idealism': 6,
 'phenomenology': 7,
 'plato': 8,
 'rationalism': 9}

# search bar object
search_bar = html.Div(id="search-bar-container", children=
    [
        dbc.Input(id="search-bar", placeholder="enter text to classify", type="text"),
        dbc.Button("SUBMIT", id="search-bar-submit-button", color="primary", className="mr-1", n_clicks=0)
    ])


layout = html.Div([
    html.H1("Text Classification"),
    search_bar,
    html.Div(id="search-bar-output", children=[])  
])

# callback for search bar
@app.callback(Output(component_id="search-bar-output", component_property="children"),
              [Input(component_id="search-bar-submit-button", component_property="n_clicks")],
              [State(component_id="search-bar", component_property="value")])
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
        class_names = [name.replace('_', ' ').title() for name in list(school_label_dict.keys())]
        explainer = lime_text.LimeTextExplainer(class_names=class_names)
        exp = explainer.explain_instance(text, 
                                        pipeline.predict, 
                                        num_features=10, 
                                        labels=[0,1,2,3,4,5,6,7,8,9],
                                        top_labels=3)
        obj = html.Iframe(
            srcDoc=exp.as_html(),
            width='100%',
            height='800px'
            style={'border': '2px #d3d3d3 solid'},
        )
        return obj
