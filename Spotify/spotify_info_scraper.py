import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID='472a3e1b8ae3465b9578a52e0938a8e2'
SECRET_ID='c3286274af334b4b8fc2400f067e6b0d'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET_ID)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# def getURIs_logging():
#     songs_list = pd.read_csv('songs.csv')
#     uri_list = []
#     count = 0
#     found = 0
#     not_found = 0
#     file_name = open("out.txt", "w")


#     for index, row in songs_list.iterrows():
#         query = row[0] + " " + row[1]
#         try:
#             index = query.find("Featuring")
#             if index != -1:
#                 query = query[:index]

#             index = query.lower().find(" x ")
#             if index != -1:
#                 query = query[:index]

#             result = sp.search(query, limit=1)
#             uri = result["tracks"]["items"][0]["uri"]
#             uri_list.append(uri)
#             found += 1
#         except:
#             file_name.write(query + "\n")
#             not_found += 1

#         count += 1

#     file_name.write("\nFound: " + str(found))
#     file_name.write("\nNot found: " + str(not_found))
#     file_name.write("\nTotal count: " + str(count))
#     file_name.close()

def getInfo():
    song_table = []
    songs_list = pd.read_csv('songs.csv')
    count = 0

    for index, row in songs_list.iterrows():
        query = row[0] + " " + row[1]

        index = query.find("Featuring")
        if index != -1:
            query = query[:index]

        index = query.lower().find(" x ")
        if index != -1:
            query = query[:index]

        result = sp.search(query, limit=1)
        uri = result["tracks"]["items"][0]["uri"]
        features = sp.audio_features(uri)[0]
        
        song_info = [row[2],
                    row[3],
                    features["danceability"],
                    features["energy"],
                    features["key"],
                    features["loudness"],
                    features["mode"],
                    features["speechiness"],
                    features["acousticness"],
                    features["instrumentalness"],
                    features["liveness"],
                    features["valence"],
                    features["tempo"]]
        
        song_table.append(song_info)

        count += 1
        print("Count: ", count)
    
    return song_table


def featuresToCSV():
    col_names = ['Year',
                'Rank',
                'Danceability',
                'Energy',
                'Key',
                'Loudness',
                'Mode',
                'Speechiness',
                'Acousticness',
                'Instrumentalness',
                'Liveness',
                'Valence',
                'Tempo']

    
    song_table = getInfo()
    song_features = pd.DataFrame(song_table, columns=col_names)
    song_features.to_csv('song_features.csv', index=False)


featuresToCSV()


