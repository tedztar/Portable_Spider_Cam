#The general Math is in this file
#importing used libraries
import math
import CONFIG
setup = False

class motor:
    #quite literly just because I cant be bothered changing the rest of the code
     def __init__(self):
          self.equation = []

def leng_update(x,y,z):  #Updates the releive X,Y,Z for each motor
    motor1.equation = [(x-CONFIG.information["camera_a"]), (CONFIG.information["max_y"]-y-CONFIG.information["camera_a"]),(CONFIG.information["max_z"]-z)]
    motor2.equation = [(CONFIG.information["max_x"]-x-CONFIG.information["camera_a"]), (CONFIG.information["max_y"]-y-CONFIG.information["camera_a"]),(CONFIG.information["max_z"])]
    motor3.equation = [(x-CONFIG.information["camera_a"]), (y-CONFIG.information["camera_a"]),(CONFIG.information["max_z"]-z)]
    motor4.equation = [(CONFIG.information["max_x"]-x-CONFIG.information["camera_a"]), (y-CONFIG.information["camera_a"]),(CONFIG.information["max_z"]-z)]

def getlength(motornum,x,y,z): #Motor you want (i.e motor1), x, y, z.  #gets the length of the wire
    leng_update(x,y,z)
    length = math.sqrt((motornum.equation[0]**2)+(motornum.equation[1]**2)+(motornum.equation[2]**2))
    return(length)

def getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed): #gets the rate of change of the length of a given wire
    leng_update(x,y,z) #required to make sure the callculations are current and accurate
    wirespeed= ((motornum.equation[0]*xspeed) + (motornum.equation[1]*yspeed) + (motornum.equation[2]*zspeed))/getlength(motornum,x,y,z)
    return(wirespeed)

def motorangle(motornum,x,y,z): #calculates the angle that the motor needs to be in to be at a given position
    length = getlength(motornum,x,y,z)
    drumbangle = length/CONFIG.information["drum_radious"]
    motorangle = drumbangle*(CONFIG.information["motor_gears"]/CONFIG.information["drum_gears"])
    return(motorangle)

def motorspeed(motornum,x,y,z,xspeed,yspeed,zspeed): #calculates the speed that the motor needs to move at
    wirespeed=getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed)
    drumbspeed=wirespeed/CONFIG.information["drum_radious"]
    motorspeed=drumbspeed*(CONFIG.information["motor_gears"]/CONFIG.information["drum_gears"])
    return(motorspeed)

#Set up stuff
motor1=motor() 
motor2=motor()
motor3=motor()
motor4=motor()

#CONFIG.import_file()
#print(getwirespeed(motor1, 5, 5, 0, 1000, 1000, 1000))
#print(getwirespeed(motor2, 5, 5, 0, 1000, 1000, 1000))
#print(getwirespeed(motor3, 5, 5, 0, 1000, 1000, 1000))
#print(getwirespeed(motor4, 5, 5, 0, 1000, 1000, 1000))
#print("done")