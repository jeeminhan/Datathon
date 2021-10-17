import pandas as pd
import lyricsgenius

GENIUS_ACCESS_TOKEN="hnCMgtuIHBu51UGj7VbNiFH12olQqp6_cNCmNGw1IX4w8QRyzfw1FQNBYygXtcn4"

def cleanLyrics(lyrics):
    index = lyrics.find('URLCopyEmbedCopy')
    while (index != -1):
        index = lyrics.find('URLCopyEmbedCopy') - 11
        i = 1
        num = lyrics[index - i]
        while num.isnumeric():
            i += 1
            num = lyrics[index - i]

        start = index - i + 1
        end = index + 27

        lyrics = lyrics[:start] + lyrics[end:]
        index = lyrics.find('URLCopyEmbedCopy')
    
    return lyrics


def main():
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

    songs_list = pd.read_csv('songs.csv')
    count = 0

    for index, row in songs_list.iterrows():
        song_name = row[0]
        artist_name = row[1]

        song = genius.search_song(song_name, artist_name)
        try:
            lyrics = cleanLyrics(song.lyrics)
            file_name = str(row[2]) + "-" + str(row[3]) + "_" + row[0] + "--" + row[1] + ".txt"
            song_file = open(file_name, "w")
            song_file.write(lyrics)
            song_file.close()
        except:
            print("Didn't work")

        
        # Log program progress
        count += 1
        percent = count //4
        print("Completed song", count, "out of 400\t>> ", percent, "% done")

main()