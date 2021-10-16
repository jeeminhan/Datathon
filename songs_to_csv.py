from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import json

URLHEAD = "https://www.billboard.com/charts/year-end/"
YEARS = list(range(2020, 2005, -2)) # Create list [2020, 2018, ... 2006]
URLTAIL = "/hot-100-songs"

# Print song params for debugging
def print_song(title, artist, year, rank):
    print("#---------------------#")
    print("Title:\t", title)
    print("Artist:\t", artist)
    print("Year:\t", year)
    print("Rank:\t", rank)

def get_songs():
    song_table = []
    for year in YEARS:
        # Setup soup
        url = URLHEAD + str(year) + URLTAIL
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
        articles = soup("article")
        
        # Get song params
        for j in range(50):
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
    
    return song_table

def write_to_csv():
    col_names = ['Title', 'Artist', 'Year', 'Rank']
    song_table = get_songs()
    songs = pd.DataFrame(song_table, columns=col_names)
    songs.to_csv('songs.csv', index=False)
    # print("Done")
