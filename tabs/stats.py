from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
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
from tabs.stats_functions import *

df = pd.read_csv('model_data/phil_nlp.csv')

search_bar = html.Div(id="w2v-bar-container", children=
    [
        dcc.Dropdown(id="stats-option", 
                    options=get_dropdown_list_stats())
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

layout = html.Div(
    [
      html.H1("Text Statistics"),
      html.H3("Enter the School, Author, or Text you'd like to analyze"),
        dbc.Row(
            [
                dbc.Col(html.Div([
                      dcc.Dropdown(id="stats-selection_1", 
                                  options=get_dropdown_list_stats(),
                                  style={'width': '90%'},
                                  placeholder='Start typing to search...'),  
                      dcc.Checklist(id='stats-options_1',
                                  options=get_checkbox_list(),
                                  value=['AWL', 'ASL', 'NUW',
                                        'FREQ', 'BGRAM', 'TXTS'],
                                  labelStyle={'display': 'inline-block', 
                                              'border-spacing': '2px'}),  
                      html.Div(id="stats-output_1", children=[])
                      ])),
                dbc.Col(html.Div([
                      dcc.Dropdown(id="stats-selection_2", 
                                  options=get_dropdown_list_stats(),
                                  style={'width': '90%'},
                                  placeholder='Start typing to search...'),  
                      dcc.Checklist(id='stats-options_2',
                                  options=get_checkbox_list(),
                                  value=['AWL', 'ASL', 'NUW',
                                        'FREQ', 'BGRAM', 'TXTS'],
                                  labelStyle={'display': 'inline-block'}),  
                      html.Div(id="stats-output_2", children=[])
                      ]))
            ]
        ),
    ]
)



@app.callback(Output(component_id="stats-output_1", component_property="children"),
              [Input(component_id="stats-selection_1", component_property="value"),
              Input(component_id='stats-options_1', component_property="value")])
def generate_stats_1(selection_value, checkbox_values, df=df, classifier_dict=classifier_dict):
  output_list = []
  if 'ASL' in checkbox_values and selection_value:
    average_sentence_length = get_average_sentence_length(selection_value, df, classifier_dict)
    output_statement = f'Average Sentence Length: {round(average_sentence_length, 2)} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    average_word_length = get_average_word_length(selection_value, df, classifier_dict)
    output_statement = f'Average Word Length: {round(average_word_length, 2)} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    num_unique, total_num = get_num_unique_words(selection_value, df, classifier_dict)
    output_statement = f'{num_unique} unique words out of {total_num} total words.'
    output_list.append(dcc.Markdown(output_statement))


  return output_list

@app.callback(Output(component_id="stats-output_2", component_property="children"),
              [Input(component_id="stats-selection_2", component_property="value"),
              Input(component_id='stats-options_2', component_property="value")])
def generate_stats_2(selection_value, checkbox_values, df=df, classifier_dict=classifier_dict):
  output_list = []
  if 'ASL' in checkbox_values and selection_value:
    average_sentence_length = get_average_sentence_length(selection_value, df, classifier_dict)
    output_statement = f'Average Sentence Length: {round(average_sentence_length, 2)} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    average_word_length = get_average_word_length(selection_value, df, classifier_dict)
    output_statement = f'Average Word Length: {round(average_word_length, 2)} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    num_unique, total_num = get_num_unique_words(selection_value, df, classifier_dict)
    output_statement = f'{num_unique} unique words out of {total_num} total words.'
    output_list.append(dcc.Markdown(output_statement))


  return output_list
# @app.callback(Output(component_id="AWL-output", component_property="children"),
#               [Input(component_id="stats-selection", component_property="value"),
#               Input(component_id='stats-options', component_property="value")])
# def generate_AWL(selection_value, checkbox_values, df=df, classifier_dict=classifier_dict):
    
  # try:
  #     cloud = make_word_cloud(input=text, 
  #                                   df=df, 
  #                                   classifier=classifier_dict, 
  #                                   stopwords=custom_stopwords).to_image()
  #     return html.Img(cloud.to_img())
  # except:
  #   return 'Sorry, something went wrong.'