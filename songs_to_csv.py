from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json

URLHEAD = "https://www.billboard.com/charts/year-end/"
YEARS = list(range(2020, 2005, -1)) # Create list [2020, 2019, ... 2006]
URLTAIL = "/hot-100-songs"

# Print song params for debugging
def print_song(title, artist, year, rank):
    print("#---------------------#")
    print("Title:\t", title)
    print("Artist:\t", artist)
    print("Year:\t", year)
    print("Rank:\t", rank)

# Get all song params in 2D array
def get_songs():
    song_table = []
    count = 0
    for year in YEARS:
        # Setup soup
        url = URLHEAD + str(year) + URLTAIL
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
        articles = soup("article")
        
        # Get song params
        for j in range(99):
            title = articles[j].find("div", class_="ye-chart-item__title").string.strip()
            try:
                artist = articles[j].find("div", class_="ye-chart-item__artist").contents[1].string.strip()
            except:
                artist = articles[j].find("div", class_="ye-chart-item__artist").contents[0].strip()
            rank = j + 1

            song_params = [title, artist, year, rank]
            song_table.append(song_params)

            # Print song for debugging
            # print_song(title, artist, year, rank)
            count += 1
            print("Count: ", count)
    
    return song_table

# Write data to csv file
def write_to_csv():
    col_names = ['Title', 'Artist', 'Year', 'Rank']
    song_table = get_songs()
    songs = pd.DataFrame(song_table, columns=col_names)
    songs.to_csv('songs.csv', index=False)

write_to_csv()