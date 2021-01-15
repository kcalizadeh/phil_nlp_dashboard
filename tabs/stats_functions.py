import wordcloud
import nltk 
nltk.download('stopwords')
from nltk import FreqDist
from nltk.corpus import stopwords
import string
import re

def get_dropdown_list():
    dropdown_list = [
      {'label': 'Plato', 'value': 'plato'},
      {'label': 'Aristotle', 'value': 'aristotle'},
      {'label': 'Locke', 'value': 'Locke'},
      {'label': 'Hume', 'value': 'Hume'},
      {'label': 'Berkeley', 'value': 'Berkeley'},
      {'label': 'Spinoza', 'value': 'Spinoza'},
      {'label': 'Leibniz', 'value': 'Leibniz'},
      {'label': 'Descartes', 'value': 'Descartes'},
      {'label': 'Malebranche', 'value': 'Malebranche'},
      {'label': 'Russell', 'value': 'Russell'},
      {'label': 'Moore', 'value': 'Moore'},
      {'label': 'Wittgenstein', 'value': 'Wittgenstein'},
      {'label': 'Lewis', 'value': 'Lewis'},
      {'label': 'Quine', 'value': 'Quine'},
      {'label': 'Popper', 'value': 'Popper'},
      {'label': 'Kripke', 'value': 'Kripke'},
      {'label': 'Foucault', 'value': 'Foucault'},
      {'label': 'Derrida', 'value': 'Derrida'},
      {'label': 'Deleuze', 'value': 'Deleuze'},
      {'label': 'Merleau-Ponty', 'value': 'Merleau-Ponty'},
      {'label': 'Husserl', 'value': 'Husserl'},
      {'label': 'Heidegger', 'value': 'Heidegger'},
      {'label': 'Kant', 'value': 'Kant'},
      {'label': 'Fichte', 'value': 'Fichte'},
      {'label': 'Hegel', 'value': 'Hegel'},
      {'label': 'Karl Marx', 'value': 'Marx'},
      {'label': 'Lenin', 'value': 'Lenin'},
      {'label': 'Adam Smith', 'value': 'Smith'},
      {'label': 'Ricardo', 'value': 'Ricardo'},
      {'label': 'Keynes', 'value': 'Keynes'},
      {'label': 'Empiricism', 'value': 'empiricism'},
      {'label': 'Rationalism', 'value': 'rationalism'},
      {'label': 'Analytic', 'value': 'analytic'},
      {'label': 'Continental', 'value': 'continental'},
      {'label': 'Phenomenology', 'value': 'phenomenology'},
      {'label': 'German Idealism', 'value': 'german_idealism'},
      {'label': 'Communism', 'value': 'communism'},
      {'label': 'Capitalism', 'value': 'capitalism'}
      ]
    return dropdown_list

def get_checkbox_list():
  checkboxes = [
    {'label': 'Average Word Length', 'value': 'AWL'},
    {'label': 'Average Sentence Length', 'value': 'ASL'},
    {'label': 'Number of Unique Words', 'value': 'NUW'},
    {'label': 'Most Common Words', 'value': 'FREQ'},
    {'label': 'Most Common Phrases', 'value': 'BGRAM'},
    {'label': 'Show Texts in Corpus', 'value': 'TXTS'}
  ]
  return checkboxes

def get_average_word_length(input, df, classifier_dict):
  punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', '[']
  num_words = 0
  sum_word_lengths = 0
  for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
    sentence_list = sentence.split()
    sentence_list = [re.sub("[',]", '', word) for word in sentence_list]
    no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
    no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
    for word in no_punctuation_tokens:
      num_words += 1
      sum_word_lengths += len(word)
  return sum_word_lengths / num_words

def get_average_sentence_length(input, df, classifier_dict):
  punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', ']']
  num_sentences = 0
  sum_sentence_lengths = 0
  for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
    sentence_list = sentence.split()
    no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
    no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
    num_sentences += 1
    sum_sentence_lengths += len(no_punctuation_tokens)
  return sum_sentence_lengths / num_sentences

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

def get_num_unique_words(input, df, classifier_dict):
  punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', ']']
  word_list = []
  num_words = 0
  for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
    sentence_list = sentence.split()
    no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
    no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
    num_words += len(no_punctuation_tokens)
    for word in no_punctuation_tokens:
      word_list.append(word)
  num_unique_words = len(set(word_list))
  return num_unique_words, num_words