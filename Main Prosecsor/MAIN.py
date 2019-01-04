#this is the main script that contols everything
from COMMUNICATION import *
from CONFIG import *
from GUI import *
from MATH import *
from MOVEMENT import *

#setup code (stuff that is run during startup
if __name__ == "__main__":

   app = SampleApp()
   app.mainloop()
