import pyautogui
import time


def play(filename):
    lyr = open(filename)
    for each_line in lyr:
        pyautogui.write(each_line)
        pyautogui.press('enter')



def imports():
    print("""
    The text below this shows what you put in the IMPORTS section:
    import assets.program_name as program_name
    The text below this shows what you put in the SONG PLAYER section:
    if whatSong == \'song name\':
        program_name.starter()
    """)




    

