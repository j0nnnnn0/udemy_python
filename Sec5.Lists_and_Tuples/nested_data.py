# Python Programming Class - Udemy 18.10.2021

# Tuples - Nested data

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

# ---

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
# commenting out so the data can be used in jukebox_menu.py

# for name, artist, year, songs in albums:
#     for track, song in songs:
#         print("Album: {}, Artist: {}, Year: {}, Track: {}, Song: {}"
#           .format(name, artist, year, track, song))
# print()

# album = albums[2]
# print(album)
# print()

# songs = album[3]
# print(songs)
# print()

# song = songs[1]
# print(song) # prints the tuple of song
# print(song[1]) # prints the tile as string

# mayhem = albums[3][3][2][1]
# print(mayhem)

# print(albums[3]) # list of album 
# print(albums[3][3]) # list of songs
# print(albums[3][3][2]) # tuple of song
# print(albums[3][3][2][1]) # string of song title

