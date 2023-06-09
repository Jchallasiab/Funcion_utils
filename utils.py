# -*- coding: utf-8 -*-
"""utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11vec_XKQ-a-psTTUBJVtfQm1D8C3k5Nl
"""

import nltk                               
from nltk.corpus import twitter_samples  
import matplotlib.pyplot as plt           
import random 
import re                                  # library for regular expression operations
import string                              # for string operations

from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

def process_tweet(tweet):
#eliminacion de hipervinculos, tags, hashtags y numeros
  # remove old style retweet text "RT"
  tweet5 = re.sub(r'^RT[\s]+', '', tweet)
  # remove tags
  tweet5 = re.sub(r'@[a-zA-Z_]+', '', tweet5)
  # remove hyperlinks
  tweet5 = re.sub(r'https?://[^\s\n\r]+', '', tweet5)
   # remove numbers
  tweet5 = re.sub(r'[0-9]+', '', tweet5)
  # remove hashtags
  # only removing the hash # sign from the word
  tweet5 = re.sub(r'#', '', tweet5)

#tokenización
  # instantiate tokenizer class
  tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
  # tokenize tweets
  tweet_tokens = tokenizer.tokenize(tweet5)

#Eliminar stop words y puntuacion
  #Import the english stop words list from NLTK
  stopwords_english = stopwords.words('english') 
  tweets_clean = []

  for word in tweet_tokens: # Go through every word in your tokens list
      if (word not in stopwords_english and  # remove stopwords
          word not in string.punctuation):  # remove punctuation
          tweets_clean.append(word)
  tweet5 = " ".join(tweets_clean)
#Lematizacion
  # Instantiate stemming class
  stemmer = PorterStemmer() 

  # Create an empty list to store the stems
  tweets_stem = [] 

  for word in tweets_clean:
      stem_word = stemmer.stem(word)  # stemming word
      tweets_stem.append(stem_word)  # append to the list
  tweet5 = " ".join(tweets_stem) 
     
  return tweet5