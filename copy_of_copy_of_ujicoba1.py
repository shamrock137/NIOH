# -*- coding: utf-8 -*-
"""Copy of Copy of ujicoba1.ipynb

"""

import pandas as pd
import csv
import tweepy
def load_data():
  data= pd.read_csv("/content/sample_data/UU ITE.csv")
  return data

tweet_df=load_data()
tweet_df.columns=['tanggal','id','username','tweet']
tweet_df

df_prepro=tweet_df.copy()
df_prepro=df_prepro.drop(columns=['id','username'])
df_prepro.head()

import string, re
def cleansing(data):
  #case folding
  data=data.lower()

  #remove punctuation
  remove=string.punctuation
  translator=str.maketrans(remove, ' '*len(remove))
  data=data.translate(translator)

  #remove ASCII & unicode
  data=data.encode('ascii','ignore').decode('utf-8')
  data=re.sub(r'[^\x00-\x7f]',r' ',data)

  #remove new line
  data=data.replace('\n',' ')

  return data

#memulai clean data
review=[]
for index, row in df_prepro.iterrows():
  review.append(cleansing(row["tweet"]))

df_prepro["tweet"]=review
df_prepro.head()

!pip install sastrawi

#import library ely
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory=StopWordRemoverFactory()
stopword=factory.create_stop_word_remover()

review=[]
for index, row in df_prepro.iterrows():
  review.append(stopword.remove(row["tweet"]))

df_prepro["tweet"]=review
df_prepro.head()

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory=StemmerFactory()
Stemmer=factory.create_stemmer()

#implementasi stemming anyng
review=[]
for index, row in df_prepro.iterrows():
  review.append(Stemmer.stem(row["tweet"]))

df_prepro["tweet"]=review
df_prepro.head()
