# !pip install twython  
import pandas as pd
import nltk
import os
from os.path import exists

nltk.download([
     "names",
     "stopwords",
     "state_union",
     "twitter_samples",
     "movie_reviews",
     "averaged_perceptron_tagger",
     "vader_lexicon",
     "punkt",
])

from nltk.sentiment import SentimentIntensityAnalyzer

song_data = pd.read_csv("songs.csv")


def lyric_analysis(filename, year, rank, title, artist):
  result_list = []
  try:
    f = open(filename, 'r')
  except:
    print(filename)
  content = f.read()

  sia = SentimentIntensityAnalyzer()
  result = sia.polarity_scores(content)

  result_list.append(year)
  result_list.append(rank)
  result_list.append(title)
  result_list.append(artist)
  result_list.append(result['compound'])
  result_list.append(result['pos'])
  result_list.append(result['neg'])
  result_list.append(result['neu'])
  f.close()
  return result_list    


big_df = []
counter = 1
for row in song_data.iterrows():
  title = row[1]['Title']
  artist = row[1]['Artist']
  year = row[1]['Year']
  rank = row[1]['Rank']
  filename = f"{year}-{rank}_{title}--{artist}.txt"

  if (os.path.exists(filename) == False):
    print(counter, filename)
    counter += 1
  try:
    big_df.append(lyric_analysis(filename, year, rank, title, artist))
  except:
    pass

df = pd.DataFrame(big_df, columns = ['Year','Rank','Title','Artist','compound','pos','neg','neu'])
df.to_csv("nlp.csv")

