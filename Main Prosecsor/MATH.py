#The general Math is in this file
import MAIN
#importing used libraries
import math

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
    motor1.equation = [(x-const.camera_a), (const.max_y-y-const.camera_a),(const.max_z-z)]
    motor2.equation = [(const.max_x-x-const.camera_a), (const.max_y-y-const.camera_a),(const.max_z-z)]
    motor3.equation = [(x-const.camera_a), (y-const.camera_a),(const.max_z-z)]
    motor4.equation = [(const.max_x-x-const.camera_a), (y-const.camera_a),(const.max_z-z)]

def getlength(motornum,x,y,z): #Motor you want (i.e motor1), x, y, z
    leng_update(x,y,z)
    length = math.sqrt((motornum.equation[0]**2)+(motornum.equation[1]**2)+(motornum.equation[2]**2))
    return(length)

def getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed):
    leng_update(x,y,z) #required to make sure the callculations are current and accurate
    wirespeed= ((motornum.equation[0]*xspeed) + (motornum.equation[1]*yspeed) + (motornum.equation[2]*zspeed))/getlength(motornum,x,y,z)
    return(wirespeed)

def motorrotation():
    print()

def motorspeed():
    print()

#runs if this program is called by another file
if __name__ == "__MATH__":
    motor1=motor() 
    motor2=motor()
    motor3=motor()
    motor4=motor()
