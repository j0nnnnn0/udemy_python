# Python Programming Class - Udemy 17.10.2021

# Nested Indexing Exercise

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

# ---

# print the following
# - the title of the song "the way I choose" from Bad company
# - the year of album "Nightflight"
# - the track number of the song "Kentish Town Walz" from Album "More" from Imelday May
# - the tuple representing the song "Keeping up a Rendezvous" from Budgie Album "Nightflight"


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
 
for album, artist, year, songs in albums:
    for track, song in songs:
        pass
# - the title of the song "the way I choose" from Bad company
print(albums[1][3][5][1])
# - the year of album "Nightflight"
print(albums[2][2])
# - the track number of the song "Kentish Town Walz" from Album "More Mayhem" from Imelday May
print(albums[3][3][3][0])
# - the tuple representing the song "Keeping up a Rendezvous" 
# from Budgie Album "Nightflight"
print(albums[2][3][1])