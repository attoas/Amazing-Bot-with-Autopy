import autopy
screen = autopy.bitmap.capture_screen()
color = autopy.color.rgb_to_hex(34,166,241)
colorPos = screen.find_color(color,0.1)	
print (colorPos)