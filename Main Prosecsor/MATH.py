#The general Math is in this file
#importing used libraries
import math
import CONFIG


class motor:
    #inisiates all variables relating to a spisific motor
     def __init__(self):
          self.length = int()
          self.equation = []
          self.wirespeed = int()
          self.rotaionneeded = int()
          self.barrelrotationspeed = int()
          self.motorspeed = int()

def leng_update(x,y,z):
    motor1.equation = [(x-CONFIG.camera_a), (CONFIG.max_y-y-CONFIG.camera_a),(CONFIG.max_z-z)]
    motor2.equation = [(CONFIG.max_x-x-CONFIG.camera_a), (CONFIG.max_y-y-CONFIG.camera_a),(CONFIG.max_z-z)]
    motor3.equation = [(x-CONFIG.camera_a), (y-CONFIG.camera_a),(CONFIG.max_z-z)]
    motor4.equation = [(CONFIG.max_x-x-CONFIG.camera_a), (y-CONFIG.camera_a),(CONFIG.max_z-z)]

def getlength(motornum,x,y,z): #Motor you want (i.e motor1), x, y, z
    leng_update(x,y,z)
    length = math.sqrt((motornum.equation[0]**2)+(motornum.equation[1]**2)+(motornum.equation[2]**2))
    return(length)

def getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed):
    leng_update(x,y,z) #required to make sure the callculations are current and accurate
    wirespeed= ((motornum.equation[0]*xspeed) + (motornum.equation[1]*yspeed) + (motornum.equation[2]*zspeed))/getlength(motornum,x,y,z)
    return(wirespeed)

def motorangle(motornum,x,y,z):
    length = getlength(motornum,x,y,z)
    drumbangle = length/CONFIG.radious
    motorangle = drumbangle*(CONFIG.motorgears/CONFIG.drumbgears)
    return(motorangle)

def motorspeed(motornum,x,y,z,xspeed,yspeed,zspeed):
    wirespeed=getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed)
    drumbspeed=wirespeed/CONFIG.drumbradious()
    motorspeed=drumbspeed*(CONFIG.motorgears/CONFIG.drumgears)
    return(motorspeed)

#Set up stuff
motor1=motor() 
motor2=motor()
motor3=motor()
motor4=motor()
