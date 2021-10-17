# Datathon
Texas A&amp;M Datathon Repository

Write-Up:#
Process
Describes team's approach to problem.
Includes
Visualization Interpretability
Explains what it means/portrays.
Reflection (optional)
What gave your team the most problems during this challenge?
What would your team do differently if you were given more than 24 hours?

Our appriach to the problem was multi-faceted. When we first started our problem we tried to approach things in a top down fashion, by having some idea of what the data would look like and creating our models based on thhat. We realized as we kept going that a lot of what we had in mind wasn't working out. We expected to find certain things in the data but it was hard for us to find those correlations in the data. That's why we turned to a more bottom-up approached where collecting data became our top priority.

The first data we scraped was the depression dataset which came from the CDC (https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2007). We used Python's BeautifulSoup and Requests libraries. Data collected was the proportion of all respondants that chose the option of "Several days", "More than half of the days", and Nearly evey day". 

The same process was used to collect data on drug use in the United States. 

Data about songs was collected in multiple different places but eventually cleaned and aggregated together. The top 50 songs of the year was found from Billboard's top 100 list. Taking the artist and title of the song, the genius API was employed to return the lyrics for each song. This data was manipulated through NLTK's sentiment analysis to determine the positive, negative, neutral, and compound values. Finally, the Spotify Web API was used to determine more attributes of the top 50 songs of each year. 


Here are some of the things that we learned through our data:
Most commonly used words in the 25 most "negative" songs

![image](https://user-images.githubusercontent.com/72060730/137617413-6b4e9681-336a-4daa-9647-edc77a9fd44a.png)

Most commonly used words in the 25 most "positive" songs

![image](https://user-images.githubusercontent.com/72060730/137617451-14684a34-db92-45f0-9bff-3751a38eb745.png)





Bonus star


![image](https://user-images.githubusercontent.com/72060730/137617470-ec425abc-802d-406d-9688-de485173b69e.png)
