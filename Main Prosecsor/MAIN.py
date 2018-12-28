#this is the main script that contols everything
from COMMUNICATION import *
from CONFIG import *
from GUI import *
from MATH import *
from MOVEMENT import *

from configparser import ConfigParser

#grabs the config from the file using CONFIG.py
class const:
   def __init__(self):
       #general config
       self.runspeed = int()
       self.max_x = int()
       self.max_y = int()
       self.max_z = int()
       self.camera_a = int()

       #motor config
       self.drum_radious = int()
       self.drum_gears = int()
       self.motor_gears = int()

   #updates the config Vars
def update_config(self):
    read_file()
        
    #general config
    self.runspeed = config.get(general, run_speed)
    self.max_x = config.get(general, max_x)
    self.max_y = config.get(general, max_y)
    self.max_z = config.get(general, max_z)
    self.camera_a = config.get(general, camera_a)

    #motor config
    self.drum_radious = config.get(motor, drum_radious)
    self.drum_gears = config.get(motor, drum_gears)
    self.motor_gears = iconfig.get(motor, motor_gears) 

#setup code (stuff that is run during startup
print(config.get("general", "run_speed"))