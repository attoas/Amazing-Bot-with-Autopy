import autopy
import time


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
    time.sleep(0.5)
    

def findFish(gamePos):
    screen = autopy.bitmap.capture_screen()
    #color = autopy.color.rgb_to_hex(252, 102, 19)
    fishPos = screen.find_color((autopy.color.rgb_to_hex(254,57,11)),0.05,((gamePos[0]+18,gamePos[1]+154),(416,242)))
    if not fishPos:
        #fishPos = screen.find_color((autopy.color.rgb_to_hex(252,102,19)),0.05)
        fishPos = screen.find_color((autopy.color.rgb_to_hex(252,102,19)),0.05,((gamePos[0]+18,gamePos[1]+154),(416,242)))
    print ("fish at : " + str(fishPos))
    if fishPos:
        autopy.mouse.move(fishPos[0]+20,fishPos[1])
        grabAndSave(gamePos)
        return True
    else:
        return False
    
    

def startGame():
    gamePos = findGameArea()
    count = 1
    while True:
        if findFish(gamePos):
            count =1
        else:
            count += 1
            if count >= 50:
                endGame(gamePos)
                count = 1

def endGame(gamePos):
    screen = autopy.bitmap.capture_screen()
    ok = autopy.bitmap.Bitmap.open('endgame.png')
    okPos = screen.find_bitmap(ok,0.05)
    #okPos = screen.find_bitmap(ok,0.05,((gamePos[0]+18,gamePos[1]+154),(416,600)))
    if okPos: 
         print("Game Over")
         exit()
        
        
startGame()

#findGameArea()