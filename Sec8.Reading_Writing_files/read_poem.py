# Python Programming Class - Udemy 09.04.2023

#IO - read from a text file

import os
from typing import ValuesView

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# ----------

jabber = open("./TextFiles/Jabberwocky.txt", 'r')

for line in jabber:
    print(line, end='')

jabber.close()