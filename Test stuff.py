from threading import Thread
from configparser import ConfigParser

import Calculate
import GUI

config = ConfigParser()

config["stuff 1"] = {
   "Dashing" : "True",
   "Awesome" : "123",
   "Key" : "dsasda"
}

config["stuff 2"] = {
   "Dashing" : "False",
   "pi" : "3.141",
   "Key" : "This Works"
}


class coordinate:

   def __init__(self):

      self.x = int(0)
      self.y = int(0)
      self.z = int(0)
      self.xx = int(0)
      self.yy = int(0)
      self.zz = int(0)
      self.A = int(0)
      
      self.xyz = [self.x, self.y, self.z, self.xx, self.yy, self.zz, self.A]


class motor:

   def __init__(self):
      
      self.length = int(0)

position = coordinate()
motor1 = motor()
motor2 = motor()
motor3 = motor()
motor4 = motor()

def this(ah, oh):
   while x == 0:
      print(ah)
      print(oh)
      

def Main():
   thread1 = Thread(target= this, args=("Something", "Something 2"))
   thread1.start()


def key_pressed(event):
   print("Yah Like Jazz?")


motor1.length = Calculate.calculation.find_length1(position.xyz)

if __name__ == "__main__":

   x = 0
   #Main()

   with open("./store.ini", "w") as f:
      config.write(f)

   config.read("./store.ini")

   print(motor1.length)

   print(config.sections())
   print(config.options("stuff 1"))
   print(config.get("stuff 1", "key"))
   print(config.options("stuff 2"))

   app = GUI.SampleApp()

   app.bind("<Key>", key_pressed)
   
   app.mainloop()



