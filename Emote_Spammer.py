import pyautogui     # import the Python Auto Gui
import time          # import the time for the sleep line


counter = 0
while counter <3:

    time.sleep(5)                   # Sleep for 5 Sec So i have time to go to the chat, before it Start entering Words
    f = open("Why Do This", "r")    # Open text File Name ( "insert file Name Here" )
    for word in f:                  # search for f line and Execute it
        pyautogui.typewrite(word)   # grab the Word in the Text Files called Why do this
        time.sleep(0.5)
        print("TRT")
        time.sleep(15)
        pyautogui.press("enter") # Press a Key in this case it enter
        print("Done")
        time.sleep(47)              # Sleep for 70 sec and Start the code again
        print("TheRinger")

    counter = counter + 1
else:
    print("inside out")



# this code is excute the !russian in Twitch.tv/Norikittea chat every 70 sec

