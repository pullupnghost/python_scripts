# Bot message_sender
'''
    * Instructions:
        1. Check the imports and install the missing ones
        2. Open the dir of the python file in cmd
        3. Run the code : python {bot-name}.py -msg 'XXX' -n Y
               /// "XXX" - text of choice; "Y" - number of choice
        4. (Optional) Change the keyboard.on_press() to the key you want to stop the script
        5. Start the Script
        6. Open the app of choice after starting
        7. Message Box should be active or wont work. 
        8. Wait for the messages to send or press Esc by default to stop
'''

import argparse
import random    #? pip install random
import pyautogui #? pip install pyautogui
import time      #? pip install time
import keyboard  #? pip install keyboard

parser = argparse.ArgumentParser(description='joao')

parser.add_argument('-msg', '--message', help='message', required=True)
parser.add_argument('-n', '--limit', help='limit', required=True)

limit = int(parser.parse_args().limit)
message = parser.parse_args().message

is_stopped = False

def __stop(event):           #? Function to stop the script
    global is_stopped
    if event.name == 'esc':  #? Change to any key you want
        is_stopped = True

keyboard.on_press(__stop)    #? On key press, calls __stop function

time.sleep(5)                #? Time to open app of choice

print('[+] Script Started!')
# Message Loop
for i in range(limit):
    if is_stopped:
        print('[-] Script Ended!')
        break

    #? Message Box should be Active on start

    pyautogui.typewrite(message)
    pyautogui.press('enter')

    print('[+] Message sent!')

    #* Time to send another message(optional)
    time.sleep(random.uniform(0.5, 1.5))

keyboard.unhook_all() 
print('[-] Script Ended!')
