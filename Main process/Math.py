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
        self.A=int()  # A=half the width of the camera mount

#Class to store all information regarting indavidual motors
class motor:
     def __init__(self):
          self.length = int()
          self.equation=[]
     def getlength(self):
         leng_update()
         self.length = math.sqrt((self.equation[0]**2)+(self.equation[1]**2)+(self.equation[2]**2))\

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
cam.x=0
cam.y=0
cam.z=0
cam.maxx=10
cam.maxy=10
cam.maxz=10
cam.A=0

motor1.getlength()
print(motor1.length)
motor2.getlength()
print(motor2.length)
motor3.getlength()
print(motor3.length)
motor4.getlength()
print(motor4.length)


