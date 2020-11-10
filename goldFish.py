import autopy

def findGameArea():
    for i in range(50):
        screen = autopy.bitmap.capture_screen()
        s = autopy.bitmap.Bitmap.open('gamearea.png')
        gamePos = screen.find_bitmap(s)
        if gamePos:
            print ("found game area at ", gamePos)
            return gamePos
        else:
            print ("can not find game ara" + str(i+1) + "/50")
    exit()        
    
 

def grabAndSave(gamePos):
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    autopy.mouse.move(gamePos[0]+616,gamePos[1]+114)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)
    

def findFish(gamePos):
    screen = autopy.bitmap.capture_screen()
    #color = autopy.color.rgb_to_hex(252, 102, 19)
    fishPos = screen.find_color((autopy.color.rgb_to_hex(254,57,11)),0.05,((gamePos[0]+18,gamePos[1]+154),(416,242)))
    if not fishPos:
        #fishPos = screen.find_color((autopy.color.rgb_to_hex(252,102,19)),0.05)
        fishPos = screen.find_color((autopy.color.rgb_to_hex(252,102,19)),0.05,((gamePos[0]+18,gamePos[1]+154),(416,242)))
    #print ("fish at : " + str(fishPos))
    if fishPos:
        autopy.mouse.move(fishPos[0]+20,fishPos[1])
        grabAndSave(gamePos)

def startGame():
    gamePos = findGameArea()
    while True:
        findFish(gamePos)

startGame()

#findGameArea()