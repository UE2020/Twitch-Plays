import pyautogui, time
class counter:
    c = int(0)
counter1 = counter()
#Create Main Function
def main():
    skippy = 0
    chatlog = open('chat.log', 'r')
    for twitchmessage in chatlog:
        skippy = skippy+1
        if counter1.c > skippy:
            continue
        best = 0
        for x in range(0, len(twitchmessage)):
            if twitchmessage[x:x + 1] == ':':
                best = x
        ChangedMessage = twitchmessage[best+1:]
        print(ChangedMessage)
        if ChangedMessage == "w 1" or "w 2" or "w 3" or "w 4" or "w 5":
            pyautogui.keyDown('w')
            try: 
                delay = int(ChangedMessage[:1])
            except:
                print("Did not work!")
            try:
                time.sleep(delay)
            except:
                print("\nw")
            pyautogui.keyUp('w')
        elif ChangedMessage == "a 1" or "a 2" or "a 3" or "a 4" or "a 5":
            pyautogui.keyDown('a')
            try: 
                delay = int(ChangedMessage[:1])
            except:
                print("Did not work!")
            try:
                time.sleep(delay)
            except:
                print("\n")
            pyautogui.keyUp('a')
        elif ChangedMessage == "s 1" or "s 2" or "s 3" or "s 4" or "s 5":
            pyautogui.keyDown('s')
            try: 
                delay = int(ChangedMessage[:1])
            except:
                print("Did not work!")
            try:
                time.sleep(delay)
            except:
                print("\n")
            pyautogui.keyUp('s')
        elif ChangedMessage == "d 1" or "d 2" or "d 3" or "d 4" or "d 5":
            pyautogui.keyDown('d')
            try: 
                delay = int(ChangedMessage[:1])
            except:
                print("Did not work!")
            try:
                time.sleep(delay)
            except:
                print("\n")
            pyautogui.keyUp('d')
        counter1.c += 1
print("Main Function Made")
#Main Loop
while True:
    main()
