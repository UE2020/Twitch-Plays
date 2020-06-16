import pyautogui, time 
class counter:
    c = int(0) #Just a counter
counter1 = counter() #Counter
#Create Main Function
def main():
    skippy = 0 #Skiping 
    chatlog = open('chat.log', 'r') #Open the chatlog
    for twitchmessage in chatlog:
        skippy = skippy+1 #Add to skip count
        if counter1.c > skippy:
            continue #Continue the loop
        best = 0 #Best placeholder variable
        for x in range(0, len(twitchmessage)):
            if twitchmessage[x:x + 1] == ':': #Remove the extra information
                best = x #Make best the twitch message
        ChangedMessage = twitchmessage[best+1:] #Fix best and make it so it is that
        print(ChangedMessage) #Print when done this is pureley for debuging purposes
        if ChangedMessage == "w 1" or "w 2" or "w 3" or "w 4" or "w 5": #You can change this later
            pyautogui.keyDown('w') #Put w down
            try: #Try so the code does not explode
                delay = int(ChangedMessage[:1]) #Made a delay that is in the thing eg: w 2 means 2 seccond delay
            except:
                print("Did not work!")
            try: #Same thing as line 21
                time.sleep(delay) #Stop for the delay
            except:
                print("\nw") #Print on a new line "W"
            pyautogui.keyUp('w') #Put the keyup after the delay is over
        elif ChangedMessage == "a 1" or "a 2" or "a 3" or "a 4" or "a 5": #THIS IS ALL THE EXACT SAME THING ACCEPT WITH DIFFRENT LETTERS REFRENCE THE PREFIOUS IF STATEMENT
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
        elif ChangedMessage == "d 1" or "d 2" or "d 3" or "d 4" or "d 5": #THIS IS ALL THE EXACT SAME THING ACCEPT WITH DIFFRENT LINES 19-29
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
print("Main Function Made") #When main is made print that it is done
#Main Loop
while True: 
    main()
