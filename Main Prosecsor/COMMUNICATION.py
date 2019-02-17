#this is the code for communicating to the motor moduals

import serial

com = serial.Serial('/dev/ttyAMAo',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=sirial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

M1_Position = int()
M1_Speed = int()
M2_Position = int()
M2_Speed = int()
M3_Position = int()
M3_Speed = int()
M4_Position = int()
M4_Speed = int()

if __name__ == COMMUNICATION:
    if M1_Position != 0 and M1_Speed != 0 and M2_Position != 0 and M2_Speed != 0 and M3_Position != 0 and M3_Speed != 0 and M4_Position != 0 and M4_Speed != 0:
        serial.