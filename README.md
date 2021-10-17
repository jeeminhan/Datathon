# MuSentiment
## Texas A&amp;M Datathon Repository


## Our approach
Our approach to the problem was multi-faceted. When we first started our problem we tried to approach things in a top-down fashion, by having some idea of what the data would look like and creating our models based on that. We realized as we kept going that a lot of what we had in mind wasn't working out. We expected to find certain things in the data but it was hard for us to find those correlations in the data. That's why we turned to a more bottom-up approach where collecting data became our top priority.

The first data we scraped was the depression dataset which came from the CDC (https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2007). We used Python's BeautifulSoup and Requests libraries. Data collected was the proportion of all respondents that chose the option of "Several days", "More than half of the days", and Nearly every day". 

The same process was used to collect data on drug use in the United States. 

Data about songs were collected in multiple different places but eventually cleaned and aggregated together. The top songs of the year were found from Billboard's top 100 list. Taking the artist and title of the song, the genius API was employed to return the lyrics for each song. This data was manipulated through NLTK's sentiment analysis to determine the positive, negative, neutral, and compound values. Finally, the Spotify Web API was used to determine more attributes of the top songs of each year. 

## Description of Data Collected

 * [Master-Song-Dataset.csv](https://github.com/jeeminhan/MuSentiment/blob/main/Master_Song_Dataset.csv) - Collection of Billboard Songs, Lyrics, Spotify Features, and Sentiment Analysis
 * [depression-data.csv](https://github.com/jeeminhan/MuSentiment/blob/main/depression_data.csv) - 
 * [drug_datacsv.csv](https://github.com/jeeminhan/MuSentiment/blob/main/drug_datacsv.csv) - 
 * [Lyrics](https://github.com/jeeminhan/MuSentiment/tree/main/Lyrics) - Lyrics collected into individual textfiles for each song

## Analysis
The main idea of the project was to see if popular songs and their possible message would affect the general population's mental health. The average depression rate was compared to the average positive and negative sentiment rating on top songs.

### Depression vs Song

![image](https://user-images.githubusercontent.com/72060730/137621202-66802374-b25f-4cb5-bf79-73cc67ec8ed0.png)

Although nothing is conclusive, there may be some correlation between depression and positive songs. One hypothesis our group established was that as people were struggling more with their mental health (2008), they turned to happier music which raised the overall score (as seen in 2010). 






### Drug usage vs song

A similar comparison was made with drug usage as well. However, there is not much correlation found between drug usage and song sentiment. 

![image](https://user-images.githubusercontent.com/72060730/137621126-f4fb3e47-a24e-4103-a145-af7d2585eafa.png)


### Regression Model

With the data collected from the Spotify API, we wanted to see if different factors (such as tempo, energy, key) would also have a direct relationship with negative sentiment. A regression model was created. The model was split 0.67-0.33 training/testing and had a root mean squared error of 0.0036. The result of the prediction is shown below

![image](https://user-images.githubusercontent.com/72060730/137621145-caa1177c-6bfb-499c-a4c6-10d11f3575e2.png)


### Word Clouds
The most commonly used words in the 25 most "negative" songs are:

![image](https://user-images.githubusercontent.com/72060730/137620645-2f4d5d47-69a2-4393-846d-d131b3229c68.png)

*A profanity filter had to be run as profane words were heavily used


The most commonly used words in the 25 most "positive" songs are:

![image](https://user-images.githubusercontent.com/72060730/137621983-522b5bfc-0d33-474d-8dcf-7395dd8b90d0.png)

These word clouds helped us understand better specific words that were the most influential on sentiment. 

### Yearly Trends
Additionally, we were able to look at the trend of the percentage of positive, negative, and neutral tendencies of songs per year.

![image](https://user-images.githubusercontent.com/72060730/137620684-f21e7832-9edf-418f-b4bb-26e41006f7b4.png)

![image](https://user-images.githubusercontent.com/72060730/137620690-7d447b37-8080-4c39-930f-a8df44fce3e7.png)

![image](https://user-images.githubusercontent.com/72060730/137620692-d98aa578-c3ab-4aec-b46d-598bbca29f84.png)

![image](https://user-images.githubusercontent.com/72060730/137620695-38e53ee8-2180-4e00-856f-76525fe3c884.png)

![image](https://user-images.githubusercontent.com/72060730/137620696-43fa7c4b-9f53-4cfb-aa0b-2a70fef1c2b5.png)

![image](https://user-images.githubusercontent.com/72060730/137620698-838060e9-8197-4375-a42f-a7953c0c2c39.png)

![image](https://user-images.githubusercontent.com/72060730/137620700-a77db526-6ca0-4ce4-8c3e-421dc02c345c.png)

![image](https://user-images.githubusercontent.com/72060730/137620701-7519db31-36b6-45e6-9e51-e93754a37d93.png)


The sporadic nature of the graphs made it hard to really analyze trends. This is possibly due to the fact that humans are so different that their song choice will not always go by a pattern. Our moods/weather/time of day plays a big role in what kind of music we listen to. 


## Reflection

There were a lot of challenges that we had to face, but we think one of the biggest ones was definitely analyzing the data that we scraped and trying to find the relationships or lack thereof between them. One of the things that made it hard to find relationships between the data was the fact that a lot of census data on depression and drug usage was collected every two years. That’s a lot of time between each of the points and so analyzing any relationships was not as accurate as we would like. There was not much we could do about this as we wanted to work with the CDC’s data and so had to make do with what we had. If we had more time we would have liked to look for more data and try to look through different relationships to see if there were any more important findings in the various datasets we created.


#### Bonus star


![image](https://user-images.githubusercontent.com/72060730/137617470-ec425abc-802d-406d-9688-de485173b69e.png)
