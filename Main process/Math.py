#Imported used library's
import math

#Class to store all information relating to the camera
class platform:
     def __init__(self):
        self.x=int()
        self.y=int()
        self.z=int()
        self.maxx=int()
        self.maxy=int()
        self.maxz=int()
        self.A=int() # A=half the width of the camera mount
        self.speed=int()
        self.xspeed=int()
        self.yspeed=int()
        self.zspeed=int()

#Class to store all information regarting indavidual motors
class motor:
    #inisiates all variables relating to a spisific motor
     def __init__(self):
          self.length = int()
          self.equation=[]
          self.wirespeed=int()
     
    #calculates the lenght of the wire for any given motor
     def getlength(self):
         leng_update()
         self.length = math.sqrt((self.equation[0]**2)+(self.equation[1]**2)+(self.equation[2]**2))\
     
     #calculates the rate that the wire is changing at any point
     def getwirespeed(self,xspeed,yspeed,zspeed):
         self.getlength() #required to make sure the callculations are current and accurate
         self.wirespeed= ((self.equation[0]*xspeed) + (self.equation[1]*yspeed) + (self.equation[2]*zspeed))/self.length
     
    #calculates the number of rotations the motor needs to preform
    def motorrotation(self):
        """Calculate howmany rotations of the barrel from length of wire
        Calculate the number of rotationstions of motor from the number of rotations of the barrel
        """
        print()

    #calculates the rate that the motor needs to be spinning at to give the required wire speed
     def motorspeed(self):
         """calculate the rotational speed of the barel from the speed required of the wire
         calculate the speed of the motor from the speed of the barrel
         """
         print()

#this is to update the formula for finding the length
def leng_update():
    motor1.equation = [(cam.x-cam.A), (cam.maxy-cam.y-cam.A),(cam.maxz-cam.z)]
    motor2.equation = [(cam.maxx-cam.x-cam.A), (cam.maxy-cam.y-cam.A),(cam.maxz-cam.z)]
    motor3.equation = [(cam.x-cam.A), (cam.y-cam.A),(cam.maxz-cam.z)]
    motor4.equation = [(cam.maxx-cam.x-cam.A), (cam.y-cam.A),(cam.maxz-cam.z)]

#Inisiation objects
cam=platform()
motor1=motor()
motor2=motor()
motor3=motor()
motor4=motor()

#seting test numbers
cam.x=5
cam.y=5
cam.z=10
cam.maxx=10
cam.maxy=10
cam.maxz=10
cam.A=0
cam.xspeed=1
cam.yspeed=1
cam.zspeed=1

motor1.getlength()
print(motor1.length)
motor2.getlength()
print(motor2.length)
motor3.getlength()
print(motor3.length)
motor4.getlength()
print(motor4.length)

motor1.getwirespeed(cam.xspeed,cam.yspeed,cam.xspeed)
print(motor1.wirespeed)
motor2.getwirespeed(cam.xspeed,cam.yspeed,cam.xspeed)
print(motor2.wirespeed)
motor3.getwirespeed(cam.xspeed,cam.yspeed,cam.xspeed)
print(motor3.wirespeed)
motor4.getwirespeed(cam.xspeed,cam.yspeed,cam.xspeed)
print(motor4.wirespeed)

