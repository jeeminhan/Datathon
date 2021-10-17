import pandas as pd
import time
import os
import azapi # https://github.com/elmoiv/azapi


def main():
    API = azapi.AZlyrics('google', accuracy=0.5)
    songs_list = pd.read_csv('songs.csv')
    azlyrics_names = open("AZLyrics_Names.txt", "w")

    count = 0
    song_num = 0

    # Iterate for each row in csv file
    for index, row in songs_list.iterrows():
        if count < 60:
            count += 1
            print("Skipped " + count)
            continue

        # Get song title and artist from AZLyrics
        API.title = row[0]
        API.artist = row[1]

        # Get song lyrics
        API.getLyrics()

        # Write lyrics to file
        file_name = str(row[2]) + "-" + str(row[3]) + "_" + row[0] + "--" + row[1] + ".txt"
        song_file = open(file_name, "w")
        song_file.write(API.lyrics)
        song_file.close()


        # Save AZLyrics song title and artist
        song_info = str(row[2]) + "-" + str(row[3]) + "_" + API.title + "--" + API.artist + '\n'
        azlyrics_names.write(song_info)

        # Wait 7 seconds every 10 calls
        if count == 10:
            time.sleep(10)
            count = 0
        else:
            count += 1

        # Log program progress
        song_num += 1
        percent = song_num //4
        print("Completed song", song_num, "out of 400\t>> ", percent, "% done")
    
    azlyrics_names.close()

main()
