#this is the code for communicating to the motor moduals
import CONFIG
import serial
import time

#com = serial.Serial('/dev/ttyAMAo',   # '/dev/ttyAMAo' is for a raspberry pi, if using a windoes computer with a sutible converter use the com pror ie 'COM3'
#                    baudrate=9600,
#                    parity=serial.PARITY_NONE,
#                    stopbits=serial.STOPBITS_ONE,
#                    bytesize=serial.EIGHTBITS
#                    )

M1_Position = int()
M1_Speed = int()
M2_Position = int()
M2_Speed = int()
M3_Position = int()
M3_Speed = int()
M4_Position = int()
M4_Speed = int()
mode = "r"

def comstart():
    global M1_Position
    global M1_Speed
    global M2_Position
    global M2_Speed
    global M3_Position
    global M3_Speed
    global M4_Position
    global M4_Speed
    global mode
    while True:
        if M1_Position != 0 and M1_Speed != 0 and M2_Position != 0 and M2_Speed != 0 and M3_Position != 0 and M3_Speed != 0 and M4_Position != 0 and M4_Speed != 0:
            serial.write("1"+mode+ " {1:d} {2:d}").format(m1_position,m1_speed)
            serial.write("2r"+mode+ " {1:d} {2:d}").format(m2_position,m2_speed)
            serial.write("3r"+mode+ " {1:d} {2:d}").format(m3_position,m3_speed)
            serial.write("4r"+mode+ " {1:d} {2:d}").format(m4_position,m4_speed)
            serial.write("@")
#            print(str(M1_Position)  + "" + str(M1_Speed)  + "" + str(M2_Position)  + "" + str(M2_Speed) + "" + str(M3_Position)  + "" + str(M3_Speed)  + "" + str(M4_Position)  + "" + str(M4_Speed))
            M1_Position = 0
            M1_Speed = 0
            M2_Position = 0
            M2_Speed = 0
            M3_Position = 0
            M3_Speed = 0
            M4_Position = 0
            M4_Speed = 0