# import wordcloud
# import nltk 
# nltk.download('stopwords')
# from nltk import FreqDist
# from nltk.corpus import stopwords
# import string
# import re
# import plotly.express as px 
# import pandas as pd
# from nltk.collocations import BigramCollocationFinder


# stopwords_list = stopwords.words('english') + list(string.punctuation) 
# stopwords_list += ['“','”','...',"''",'’','``', "'", "‘"]
# custom_stopwords = ['–', 'also', 'something', 'cf', 'thus', 'two', 'now', 'would', 
                    # 'make', 'eb', 'u', 'well', 'even', 'said', 'eg', 'us',
                    # 'n', 'sein', 'e', 'da', 'therefore', 'however', 'would', 
                    # 'thing', 'must', 'merely', 'way', 'since', 'latter', 'first',
                    # 'B', 'mean', 'upon', 'yet', 'cannot', 'c', 'C', 'let', 'may', 
                    # 'might', "'s", 'b', 'ofthe', 'p.', '_', '-', 'eg', 'e.g.',
                    # 'ie', 'i.e.', 'f', 'l', "n't", 'e.g', 'i.e', '—', '--', 
                    # 'hyl', 'phil', 'one', 'another', 'could', 'come', 'things', 'thing',
                    # 'else', 'every'] + stopwords_list

def get_dropdown_list_stats():
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
      {'label': 'Capitalism', 'value': 'capitalism'},
      {'label': 'Aristotle - Complete Works',
        'value': 'Aristotle - Complete Works'},
      {'label': 'Second Treatise On Government',
        'value': 'Second Treatise On Government'},
      {'label': 'Essay Concerning Human Understanding',
        'value': 'Essay Concerning Human Understanding'},
      {'label': 'A Treatise Of Human Nature',
        'value': 'A Treatise Of Human Nature'},
      {'label': 'Dialogues Concerning Natural Religion',
        'value': 'Dialogues Concerning Natural Religion'},
      {'label': 'Three Dialogues', 'value': 'Three Dialogues'},
      {'label': 'A Treatise Concerning The Principles Of Human Knowledge',
        'value': 'A Treatise Concerning The Principles Of Human Knowledge'},
      {'label': 'Ethics', 'value': 'Ethics'},
      {'label': 'On The Improvement Of Understanding',
        'value': 'On The Improvement Of Understanding'},
      {'label': 'Theodicy', 'value': 'Theodicy'},
      {'label': 'Discourse On Method', 'value': 'Discourse On Method'},
      {'label': 'Meditations', 'value': 'Meditations'},
      {'label': 'The Search After Truth', 'value': 'The Search After Truth'},
      {'label': 'The Analysis Of Mind', 'value': 'The Analysis Of Mind'},
      {'label': 'The Problems Of Philosophy',
        'value': 'The Problems Of Philosophy'},
      {'label': 'Philosophical Studies', 'value': 'Philosophical Studies'},
      {'label': 'Philosophical Investigations',
        'value': 'Philosophical Investigations'},
      {'label': 'Tractatus Logico-Philosophicus',
        'value': 'Tractatus Logico-Philosophicus'},
      {'label': 'Lewis - Papers', 'value': 'Lewis - Papers'},
      {'label': 'Quintessence', 'value': 'Quintessence'},
      {'label': 'The Logic Of Scientific Discovery',
        'value': 'The Logic Of Scientific Discovery'},
      {'label': 'Naming And Necessity', 'value': 'Naming And Necessity'},
      {'label': 'Philosophical Troubles', 'value': 'Philosophical Troubles'},
      {'label': 'The Birth Of The Clinic', 'value': 'The Birth Of The Clinic'},
      {'label': 'Madness And Civilization', 'value': 'Madness And Civilization'},
      {'label': 'The Order Of Things', 'value': 'The Order Of Things'},
      {'label': 'Writing And Difference', 'value': 'Writing And Difference'},
      {'label': 'Difference And Repetition', 'value': 'Difference And Repetition'},
      {'label': 'Anti-Oedipus', 'value': 'Anti-Oedipus'},
      {'label': 'The Phenomenology Of Perception',
        'value': 'The Phenomenology Of Perception'},
      {'label': 'The Crisis Of The European Sciences And Phenomenology',
        'value': 'The Crisis Of The European Sciences And Phenomenology'},
      {'label': 'The Idea Of Phenomenology', 'value': 'The Idea Of Phenomenology'},
      {'label': 'Being And Time', 'value': 'Being And Time'},
      {'label': 'Off The Beaten Track', 'value': 'Off The Beaten Track'},
      {'label': 'Critique Of Practical Reason',
        'value': 'Critique Of Practical Reason'},
      {'label': 'Critique Of Judgement', 'value': 'Critique Of Judgement'},
      {'label': 'Critique Of Pure Reason', 'value': 'Critique Of Pure Reason'},
      {'label': 'The System Of Ethics', 'value': 'The System Of Ethics'},
      {'label': 'The Science Of Logic', 'value': 'Science Of Logic'},
      {'label': 'The Phenomenology Of Spirit',
        'value': 'The Phenomenology Of Spirit'},
      {'label': 'Elements Of The Philosophy Of Right',
        'value': 'Elements Of The Philosophy Of Right'},
      {'label': 'Marx - Capital', 'value': 'Kapital'},
      {'label': 'The Communist Manifesto', 'value': 'The Communist Manifesto'},
      {'label': 'Essential Works Of Lenin', 'value': 'Essential Works Of Lenin'},
      {'label': 'The Wealth Of Nations', 'value': 'The Wealth Of Nations'},
      {'label': 'On The Principles Of Political Economy And Taxation',
        'value': 'On The Principles Of Political Economy And Taxation'},
      {'label': 'A General Theory Of Employment, Interest, And Money',
        'value': 'A General Theory Of Employment, Interest, And Money'}
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

# def get_average_word_length(input, df, classifier_dict):
#   punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', '[']
#   num_words = 0
#   sum_word_lengths = 0
#   for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
#     sentence_list = sentence.split()
#     sentence_list = [re.sub("[',]", '', word) for word in sentence_list]
#     no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
#     no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
#     for word in no_punctuation_tokens:
#       num_words += 1
#       sum_word_lengths += len(word)
#   return sum_word_lengths / num_words

# def get_average_sentence_length(input, df, classifier_dict):
#   punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', ']']
#   num_sentences = 0
#   sum_sentence_lengths = 0
#   for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
#     sentence_list = sentence.split()
#     no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
#     no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
#     num_sentences += 1
#     sum_sentence_lengths += len(no_punctuation_tokens)
#   return sum_sentence_lengths / num_sentences

# def make_word_cloud(input, df, classifier, stopwords=stopwords.words('english')):
#     text = ''
#     for sentence in df[df[classifier[input]]==input]['sentence_str']:
#       text += sentence
#     cloud = wordcloud.WordCloud(width=500, 
#                             height=400, 
#                             background_color='#D1D1D1', 
#                             max_words=30, 
#                             stopwords=stopwords, 
#                             color_func=lambda *args, **kwargs: (95,95,95)).generate(text)
#     return cloud

# def get_num_unique_words(input, df, classifier_dict):
#   punctuations = list(string.punctuation) + ['“','”','...',"''",'’','``', "'", "‘", '[', ']']
#   word_list = []
#   num_words = 0
#   for sentence in df[df[classifier_dict[input]]==input]['tokenized_txt']:
#     sentence_list = sentence.split()
#     no_punctuation_tokens = [word for word in sentence_list if word not in punctuations]
#     no_punctuation_tokens = [word for word in no_punctuation_tokens if len(word) > 0]
#     num_words += len(no_punctuation_tokens)
#     for word in no_punctuation_tokens:
#       word_list.append(word)
#   num_unique_words = len(set(word_list))
#   return num_unique_words, num_words

# def plot_word_frequency(input, df, classifier_dict, stopwords):
#   word_list = []
#   for sentence in df[df[classifier_dict[input]]==input]['gensim_tokenized'][:50]:
#     for word in sentence:
#       word_list.append(word)
#   cleaned_words = [x.lower() for x in word_list if x.lower() not in stopwords]
#   freq_dist = FreqDist(cleaned_words)
#   freq_dict = {'words': [x[0] for x in freq_dist.most_common(7)], 
#               'frequency': [x[1] for x in freq_dist.most_common(7)]}
#   freq_df = pd.DataFrame(freq_dict)
#   fig = px.bar(freq_df,
#               x='words',
#               y='frequency')
#   fig.update_xaxes(title_text='Words')
#   fig.update_yaxes(title_text='Count')
#   fig.update_layout(title_text=f'{input.title()} Word Frequency Chart', title_x=0.5)
#   return fig

# def plot_ngram_frequency(input, df, classifier_dict, stopwords): 
#   word_list = []
#   for sent in df[df[classifier_dict[input]]==input]['gensim_tokenized']:
#     for word in sent:
#       word_list.append(word)
#   cleaned = [word.lower() for word in word_list if word not in custom_stopwords]
#   bigram_finder = BigramCollocationFinder.from_words(cleaned, window_size=3)
#   top_10 = sorted(bigram_finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:7]
#   bigram_df = pd.DataFrame(top_10, columns=['bigram', 'frequency'])
#   bigram_df['bigram'] = bigram_df['bigram'].apply(lambda x: ', '.join(x))
#   fig = px.bar(bigram_df,
#               x='bigram',
#               y='frequency')
#   fig.update_xaxes(title_text='Phrases')
#   fig.update_yaxes(title_text='Count')
#   fig.update_layout(title_text=f'{input.title()} N-gram Frequency Chart', title_x=0.5)
#   return fig

# def get_title_list(input, df, classifier_dict):
  title_list = list(df[df[classifier_dict[input]]==input]['title'].unique())
  title_list = [title.title() for title in title_list] 
  return ', '.join(title_list)