from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State
import matplotlib.pyplot as plt
import wordcloud
import pickle
# from nltk.corpus import stopwords
import string
import plotly.express as px
from gensim.utils import simple_preprocess

from app import app
from tabs.stats_functions import *

# df = pd.read_csv('model_data/phil_nlp.csv')
# df['gensim_tokenized'] = df['sentence_str'].map(lambda x: simple_preprocess(x.lower(),deacc=True,
#                                                         max_len=250))
with open('model_data/stats_dict.pkl', 'rb') as st_dict:
  stats_dict = pickle.load(st_dict)

with open('model_data/classifier.pkl', 'rb') as class_dict:
  classifier_dict = pickle.load(class_dict)

search_bar = html.Div(id="w2v-bar-container", children=
    [
        dcc.Dropdown(id="stats-option", 
                    options=get_dropdown_list_stats())
    ])

# classifier_dict = {}
# for author in df['author'].unique():
#   classifier_dict[author] = 'author'
# for title in df['title'].unique():
#   classifier_dict[title] = 'title'
# for school in df['school'].unique():
#   classifier_dict[school] = 'school'

# stopwords_list = ['i',
#  'me',
#  'my',
#  'myself',
#  'we',
#  'our',
#  'ours',
#  'ourselves',
#  'you',
#  "you're",
#  "you've",
#  "you'll",
#  "you'd",
#  'your',
#  'yours',
#  'yourself',
#  'yourselves',
#  'he',
#  'him',
#  'his',
#  'himself',
#  'she',
#  "she's",
#  'her',
#  'hers',
#  'herself',
#  'it',
#  "it's",
#  'its',
#  'itself',
#  'they',
#  'them',
#  'their',
#  'theirs',
#  'themselves',
#  'what',
#  'which',
#  'who',
#  'whom',
#  'this',
#  'that',
#  "that'll",
#  'these',
#  'those',
#  'am',
#  'is',
#  'are',
#  'was',
#  'were',
#  'be',
#  'been',
#  'being',
#  'have',
#  'has',
#  'had',
#  'having',
#  'do',
#  'does',
#  'did',
#  'doing',
#  'a',
#  'an',
#  'the',
#  'and',
#  'but',
#  'if',
#  'or',
#  'because',
#  'as',
#  'until',
#  'while',
#  'of',
#  'at',
#  'by',
#  'for',
#  'with',
#  'about',
#  'against',
#  'between',
#  'into',
#  'through',
#  'during',
#  'before',
#  'after',
#  'above',
#  'below',
#  'to',
#  'from',
#  'up',
#  'down',
#  'in',
#  'out',
#  'on',
#  'off',
#  'over',
#  'under',
#  'again',
#  'further',
#  'then',
#  'once',
#  'here',
#  'there',
#  'when',
#  'where',
#  'why',
#  'how',
#  'all',
#  'any',
#  'both',
#  'each',
#  'few',
#  'more',
#  'most',
#  'other',
#  'some',
#  'such',
#  'no',
#  'nor',
#  'not',
#  'only',
#  'own',
#  'same',
#  'so',
#  'than',
#  'too',
#  'very',
#  's',
#  't',
#  'can',
#  'will',
#  'just',
#  'don',
#  "don't",
#  'should',
#  "should've",
#  'now',
#  'd',
#  'll',
#  'm',
#  'o',
#  're',
#  've',
#  'y',
#  'ain',
#  'aren',
#  "aren't",
#  'couldn',
#  "couldn't",
#  'didn',
#  "didn't",
#  'doesn',
#  "doesn't",
#  'hadn',
#  "hadn't",
#  'hasn',
#  "hasn't",
#  'haven',
#  "haven't",
#  'isn',
#  "isn't",
#  'ma',
#  'mightn',
#  "mightn't",
#  'mustn',
#  "mustn't",
#  'needn',
#  "needn't",
#  'shan',
#  "shan't",
#  'shouldn',
#  "shouldn't",
#  'wasn',
#  "wasn't",
#  'weren',
#  "weren't",
#  'won',
#  "won't",
#  'wouldn',
#  "wouldn't"] + list(string.punctuation) 
# stopwords_list += ['“','”','...',"''",'’','``', "'", "‘"]
# custom_stopwords = ['–', 'also', 'something', 'cf', 'thus', 'two', 'now', 'would', 
#                     'make', 'eb', 'u', 'well', 'even', 'said', 'eg', 'us',
#                     'n', 'sein', 'e', 'da', 'therefore', 'however', 'would', 
#                     'thing', 'must', 'merely', 'way', 'since', 'latter', 'first',
#                     'B', 'mean', 'upon', 'yet', 'cannot', 'c', 'C', 'let', 'may', 
#                     'might', "'s", 'b', 'ofthe', 'p.', '_', '-', 'eg', 'e.g.',
#                     'ie', 'i.e.', 'f', 'l', "n't", 'e.g', 'i.e', '—', '--', 
#                     'hyl', 'phil', 'one', 'another', 'could', 'come', 'things', 'thing',
#                     'else', 'edition'] + stopwords_list

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
                      html.Div(id="stats-output-1", children=[])
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
                      html.Div(id="stats-output-2", children=[])
                      ]))
            ]
        ),
    ]
)



@app.callback(Output(component_id="stats-output-1", component_property="children"),
              [Input(component_id="stats-selection_1", component_property="value"),
              Input(component_id='stats-options_1', component_property="value")])
def generate_stats_1(selection_value, checkbox_values):#, df=df, classifier_dict=classifier_dict):
  output_list = [html.Br()]
  if 'TXTS' in checkbox_values and selection_value:
    # if classifier_dict[selection_value] != 'title':
      # title_list = get_title_list(selection_value, df, classifier_dict)
    title_list = stats_dict[selection_value]['title_list']
    output_statement = f'**Titles in the Corpus:** {title_list}.'
    output_list.append(dcc.Markdown(output_statement))
  if 'ASL' in checkbox_values and selection_value:
    # average_sentence_length = get_average_sentence_length(selection_value, df, classifier_dict)
    average_sentence_length = stats_dict[selection_value]['mean_sent_length']
    output_statement = f'**Average Sentence Length:** {round(average_sentence_length, 2)} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    # average_word_length = get_average_word_length(selection_value, df, classifier_dict)
    average_word_length = stats_dict[selection_value]['mean_word_length']
    output_statement = f'**Average Word Length:** {round(average_word_length, 2)} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    # num_unique, total_num = get_num_unique_words(selection_value, df, classifier_dict)
    num_unique, total_num = stats_dict[selection_value]['num_unique']
    output_statement = f'**{num_unique}** unique words out of **{total_num}** total words.'
    output_list.append(dcc.Markdown(output_statement))
  if 'FREQ' in checkbox_values and selection_value:
    output_list.append(dcc.Graph(figure=stats_dict[selection_value]['word_freq_chart']))
  if 'BGRAM' in checkbox_values and selection_value:
    # output_list.append(dcc.Graph(figure=plot_ngram_frequency(selection_value, df, classifier_dict, custom_stopwords)))
    output_list.append(dcc.Graph(figure=stats_dict[selection_value]['ngram_chart']))
    output_list.append(html.Center("Note that word pairs here could be connected by any number of stopwords such as 'of' or 'the.'"))
  return output_list



@app.callback(Output(component_id="stats-output-2", component_property="children"),
              [Input(component_id="stats-selection_2", component_property="value"),
              Input(component_id='stats-options_2', component_property="value")])
def generate_stats_2(selection_value, checkbox_values):#, df=df, classifier_dict=classifier_dict):
  output_list = [html.Br()]
  if 'TXTS' in checkbox_values and selection_value:
    # if classifier_dict[selection_value] != 'title':
      # title_list = get_title_list(selection_value, df, classifier_dict)
    title_list = stats_dict[selection_value]['title_list']
    output_statement = f'**Titles in the Corpus:** {title_list}.'
    output_list.append(dcc.Markdown(output_statement))
  if 'ASL' in checkbox_values and selection_value:
    # average_sentence_length = get_average_sentence_length(selection_value, df, classifier_dict)
    average_sentence_length = stats_dict[selection_value]['mean_sent_length']
    output_statement = f'**Average Sentence Length:** {round(average_sentence_length, 2)} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    # average_word_length = get_average_word_length(selection_value, df, classifier_dict)
    average_word_length = stats_dict[selection_value]['mean_word_length']
    output_statement = f'**Average Word Length:** {round(average_word_length, 2)} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    # num_unique, total_num = get_num_unique_words(selection_value, df, classifier_dict)
    num_unique, total_num = stats_dict[selection_value]['num_unique']
    output_statement = f'**{num_unique}** unique words out of **{total_num}** total words.'
    output_list.append(dcc.Markdown(output_statement))
  if 'FREQ' in checkbox_values and selection_value:
    # output_list.append(dcc.Graph(figure=plot_word_frequency(selection_value, df, classifier_dict, custom_stopwords)))
    output_list.append(dcc.Graph(figure=stats_dict[selection_value]['word_freq_chart']))
  if 'BGRAM' in checkbox_values and selection_value:
    # output_list.append(dcc.Graph(figure=plot_ngram_frequency(selection_value, df, classifier_dict, custom_stopwords)))
    output_list.append(dcc.Graph(figure=stats_dict[selection_value]['ngram_chart']))
    output_list.append(html.Center("Note that word pairs here could be connected by any number of stopwords such as 'of' or 'the.'"))
  return output_list