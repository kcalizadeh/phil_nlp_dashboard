from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State
import matplotlib.pyplot as plt
import wordcloud
import nltk 
nltk.download('stopwords')
from nltk import FreqDist
from nltk.corpus import stopwords
import string
import plotly.express as px


from app import app
from tabs.stats_functions import make_word_cloud

def make_word_cloud(input, df, classifier, stopwords=stopwords.words('english')):
    text = ''
    for sentence in df[df[classifier[input]]==input]['sentence_str']:
      text += sentence
    cloud = wordcloud.WordCloud(width=500, 
                            height=400, 
                            background_color='#D1D1D1', 
                            max_words=30, 
                            stopwords=stopwords, 
                            color_func=lambda *args, **kwargs: (95,95,95)).generate(text)
    return cloud

df = pd.read_csv('model_data/phil_nlp.csv')

search_bar = html.Div(id="w2v-bar-container", children=
    [
        dbc.Input(id="stats-text-bar", placeholder="", type="text", n_submit=0),
        dbc.Button("SUBMIT", id="stats-submit-button", color="primary", className="mr-1", n_clicks=0)
    ])

classifier_dict = {}
for author in df['author'].unique():
  classifier_dict[author] = 'author'
for title in df['title'].unique():
  classifier_dict[title] = 'title'
for school in df['school'].unique():
  classifier_dict[school] = 'school'

stopwords_list = stopwords.words('english') + list(string.punctuation) 
stopwords_list += ['“','”','...',"''",'’','``', "'", "‘"]
custom_stopwords = ['–', 'also', 'something', 'cf', 'thus', 'two', 'now', 'would', 
                    'make', 'eb', 'u', 'well', 'even', 'said', 'eg', 'us',
                    'n', 'sein', 'e', 'da', 'therefore', 'however', 'would', 
                    'thing', 'must', 'merely', 'way', 'since', 'latter', 'first',
                    'B', 'mean', 'upon', 'yet', 'cannot', 'c', 'C', 'let', 'may', 
                    'might', "'s", 'b', 'ofthe', 'p.', '_', '-', 'eg', 'e.g.',
                    'ie', 'i.e.', 'f', 'l', "n't", 'e.g', 'i.e', '—', '--', 
                    'hyl', 'phil', 'one', 'another', 'could', 'come'] + stopwords_list

layout = html.Div([
    html.H1("Text Statistics"),
    html.H3("Enter the School, Author, or Text you'd like to analyze"),
    search_bar,
    html.Div(id="stats-output", children=[])
])

# callback for search bar
@app.callback(Output(component_id="stats-output", component_property="children"),
              [Input(component_id="stats-submit-button", component_property="n_clicks"),
              Input(component_id="stats-text-bar", component_property="n_submit")],
              [State(component_id="stats-text-bar", component_property="value")])
def generate_stats(n_clicks, n_submit, text, df=df, classifier_dict=classifier_dict):
    if n_clicks < 1 and n_submit < 1:
      return None
    else:
      try:
          cloud = make_word_cloud(input=text, 
                                        df=df, 
                                        classifier=classifier_dict, 
                                        stopwords=custom_stopwords).to_image()
          return html.Img(cloud.to_img())
      except:
        return 'Sorry, something went wrong.'