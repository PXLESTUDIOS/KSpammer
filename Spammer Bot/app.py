###############################
# IMPORTS
###############################
import pyautogui
import time


songList = "Rick Roll" #enter all the songs you have added


whatSong = input(f"What song would you like? {songList}\n")
##########################################
# SONG PLAYER
##########################################
if whatSong.lower() == 'rick roll':
    time.sleep(5)
    import assets.Crab_Rave
else:
    print("Sorry, we do not have that song in the playlist!")