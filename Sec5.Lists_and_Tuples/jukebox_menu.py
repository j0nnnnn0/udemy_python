# Python Programming Class - Udemy 17.10.2021

# Jukebox demo

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# import (share) the albums list from nested_data.py 
from nested_data import albums


# constants (in capital letters as per pep8)
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
# Select an album
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print ("{}: {} by {}".format(index + 1, title, artist))
    
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX] # print(songs_list)
    else:
        print("Bye")
        break

# Select a song from the album
    print("Please choose your song (invalid choice exits):")
    for index, (track, song) in enumerate(songs_list):
        print(" Track: {}, Song: {}".format(index + 1, song))

    choice_song = int(input())
    if 1 <= choice_song <=len(songs_list):
        song = songs_list[choice_song -1][SONG_TITLE_INDEX]
    # Print the song to play
        print()
        print("Playing {} ".format(song))

    print("=" * 40)




