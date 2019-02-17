import socket
import struct
#this is for the Phantom 3 Pro controller, If you have a diffrent controller, please modify the scrip and upload for others
#button[1] = 
#button[2] = 
#button[3] = 
#button[4] = 
#button[5] = 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.1", 2345))

ratio = 2

def word(b0, b1):
    global ratio
    x = (b0 << 8) | b1
    return int((x - 1024)/(ratio))


while True:
    data = bytearray(s.recv(1024))
    if len(data) == 26:
        rightX = word(data[12], data[11])
        rightY = word(data[14], data[13]) 
        leftY = word(data[16], data[15]) 
        leftX = word(data[18], data[17]) 
        cam = word(data[20], data[19]) 
        buttons = [bool(int(x)) for x in bin((data[23] >> 3)&31)[2:].zfill(5)]
#        print("leftX: %4i, leftY: %4i, rightX: %4i, rightY: %4i, cam: %4i" % (
#           leftX, leftY, rightX, rightY, cam))
#        print(buttons)
        if buttons[0] == True:
           print("Video")
        if buttons[1] == True:
           print("Menu")
        if buttons[2] == True:
           print("Photo")
        if buttons[3] == True:
           print("C1")
        if buttons[4] == True:
           print("C2")
        if rightX > 0:
            print("rightx up")
        if rightX < 0:
            print("rightx down")
        if rightY > 0:
            print("righty up")
        if rightY < 0:
            print("righty down")
        if leftX > 0:
            print("leftx up")
        if leftX < 0:
            print("leftx down")
        if leftY > 0:
            print("lefty up")
        if leftY < 0:
            print("lefty down")
        if cam > 0:
            print("cam up")
        if cam < 0:
            print("cam down")