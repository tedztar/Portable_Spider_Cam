#The general Math is in this file

#Constants set up in the config file
camA = 0
cammaxx = 10
cammaxy = 10
cammaxz = 10

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
    motor1.equation = [(x-camA), (cammaxy-y-camA),(cammaxz-z)]
    motor2.equation = [(cammaxx-x-camA), (cammaxy-y-camA),(cammaxz-z)]
    motor3.equation = [(x-camA), (y-camA),(cammaxz-z)]
    motor4.equation = [(cammaxx-x-camA), (y-camA),(cammaxz-z)]

def getlength(motornum,x,y,z): #Motor you want (i.e motor1), x, y, z
    leng_update(x,y,z)
    length = math.sqrt((motornum.equation[0]**2)+(motornum.equation[1]**2)+(motornum.equation[2]**2))
    return(length)

def getwirespeed(motornum,x,y,z,xspeed,yspeed,zspeed):
    leng_update(x,y,z) #required to make sure the callculations are current and accurate
    wirespeed= ((motornum.equation[0]*xspeed) + (motornum.equation[1]*yspeed) + (motornum.equation[2]*zspeed))/motornum.getlength(motornum,x,y,z)
    return(wirespeed)

def motorrotation():
    print()

def motorspeed():
    print()

#Inisiation objects
motor1=motor() 
motor2=motor()
motor3=motor()
motor4=motor()

print(getlength(motor1, 5, 5, 5))
print(getlength(motor2, 5, 5, 5))
print(getlength(motor3, 5, 5, 5))
print(getlength(motor4, 5, 5, 5))

