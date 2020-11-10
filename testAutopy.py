import autopy


#autopy.mouse.move(1,1)
#autopy.mouse.move(1,1)
#autopy.mouse.smooth_move(1000,500)
#autopy.mouse.click()
#autopy.key.type_string("Hello World")

#autopy.bitmap.capture_screen().save('screen.png')

screen = autopy.bitmap.capture_screen()
#debug = autopy.bitmap.Bitmap.open('bug.png')
#pos = screen.find_bitmap(debug)
#if pos:
#    autopy.mouse.smooth_move(pos[0],pos[1])
#    autopy.mouse.click()
#else:
#    print("can not find bitmap")

while True: 
    mousePos = autopy.mouse.location ()   
    #color = autopy.color.hex_to_rgb(screen.get_color(mousePos[0],mousePos[1]))
    print(mousePos)

# #colorPos = screen.find_color((186,89,87),0.1)
# color = autopy.color.rgb_to_hex(0, 0, 0)
# print(color)
# colorPos = screen.find_color(color)
# print (colorPos)