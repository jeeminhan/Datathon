# Datathon
## Texas A&amp;M Datathon Repository

Write-Up:#
Process
Describes team's approach to problem.
Includes
Visualization Interpretability
Explains what it means/portrays.
Reflection (optional)
What gave your team the most problems during this challenge?
What would your team do differently if you were given more than 24 hours?


## Our approach
Our appriach to the problem was multi-faceted. When we first started our problem we tried to approach things in a top down fashion, by having some idea of what the data would look like and creating our models based on thhat. We realized as we kept going that a lot of what we had in mind wasn't working out. We expected to find certain things in the data but it was hard for us to find those correlations in the data. That's why we turned to a more bottom-up approached where collecting data became our top priority.

The first data we scraped was the depression dataset which came from the CDC (https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2007). We used Python's BeautifulSoup and Requests libraries. Data collected was the proportion of all respondants that chose the option of "Several days", "More than half of the days", and Nearly evey day". 

The same process was used to collect data on drug use in the United States. 

Data about songs was collected in multiple different places but eventually cleaned and aggregated together. The top 50 songs of the year was found from Billboard's top 100 list. Taking the artist and title of the song, the genius API was employed to return the lyrics for each song. This data was manipulated through NLTK's sentiment analysis to determine the positive, negative, neutral, and compound values. Finally, the Spotify Web API was used to determine more attributes of the top songs of each year. 


## Analysis
The main idea of the project was to see if popular song's and their possible message would affect the general population's mental health. The average depression rate was compared to the average positive and negative sentiment rating on top songs.

### Depression vs Song

![image](https://user-images.githubusercontent.com/72060730/137621202-66802374-b25f-4cb5-bf79-73cc67ec8ed0.png)

Although, nothing is conclusive, there may be some correation between depression and positive songs. One hypothesis our group establised was that as people were stuggling more with their mental health (2008), they turned to happier music which raised the overall score (as seen in 2010). 






### Drug usage vs song

A similar compairison was made with drug usage as well. However, there is not much correlation found between drug usage and song sentiment. 

![image](https://user-images.githubusercontent.com/72060730/137621126-f4fb3e47-a24e-4103-a145-af7d2585eafa.png)


### Regression Model

With the data collected from the spotify API, we wanted to see if different factors (such as tempo, energy, key) would also have a direct relationship with negative sentiment. A regression model was created. The model was split 0.67-0.33 training/testing and had a root mean squared error of 0.0036. The result of the prediction is shown below

![image](https://user-images.githubusercontent.com/72060730/137621145-caa1177c-6bfb-499c-a4c6-10d11f3575e2.png)


### Word Clouds
Most commonly used words in the 25 most "negative" songs are:

![image](https://user-images.githubusercontent.com/72060730/137620645-2f4d5d47-69a2-4393-846d-d131b3229c68.png)


Most commonly used words in the 25 most "positive" songs are"

![image](https://user-images.githubusercontent.com/72060730/137620654-21d91a86-58eb-47c6-9c09-586a0c747521.png)

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



## Reflection


#### Bonus star


![image](https://user-images.githubusercontent.com/72060730/137617470-ec425abc-802d-406d-9688-de485173b69e.png)
