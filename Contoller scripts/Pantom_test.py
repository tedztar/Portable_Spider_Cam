import socket
import struct
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.1", 2345))

def word(b0, b1):
    return (b0 << 8) | b1

def conv(w):
    return (w / 8 - 128) & 0xff

while True:
    data = bytearray(s.recv(1024))
    if len(data) == 26:
#       rightX = word(data[12], data[11])
#        rightY = word(data[14], data[13]) 
#        leftY = word(data[16], data[15]) 
#        leftX = word(data[18], data[17]) 
#        cam = word(data[20], data[19]) 
#        print("leftX: %4i, leftY: %4i, rightX: %4i, rightY: %4i, cam: %4i" % (
#           leftX, leftY, rightX, rightY, cam))
        #(data[23]>>3)&31=data[23]
        #print("{0:b}".format(data[23]))
        #time.sleep(3)
        buttons = [bool(int(x)) for x in bin((data[23] >> 3)&31)[2:].zfill(5)]
        print(buttons)