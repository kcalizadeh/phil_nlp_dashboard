import wordcloud
import nltk 
nltk.download('stopwords')
from nltk import FreqDist
from nltk.corpus import stopwords
import string

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

