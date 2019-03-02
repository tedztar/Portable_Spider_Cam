#This is the GUI that controlls the spidercam. #repetinterval
from tkinter import *
import CONFIG
import MOVEMENT
interval = int(1000 / int(CONFIG.information["run_speed"]))
#Creates a window as an object.
class SampleApp(Tk):

   #Sets up the window.
    def __init__(self, information):
      
        Tk.__init__(self)  #SampleApp = Tk()
        container = Frame(self) #Window = Frame(SampleApp)


        #Screen Adjustment.
        screen_width = (self.winfo_screenwidth())
        screen_height = (self.winfo_screenheight()/1.1)

        default_xposition = -10
        default_yposition = 2

        self.geometry("%dx%d+%d+%d" % (screen_width, screen_height, default_xposition, default_yposition))

        self.resizable(width=False, height=False)
        self.title("...")

      

        container.pack(side ="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.container = container

      
        #Empty list of useable frames.
        self.frames = {}



    #Show a certain Frame.
    def show_frame(self, cont):
      
        frame = self.frames[cont]
        frame.tkraise()


#First Page. Self is the Frame itself. Parent is the container. Controller is the SampleApp.
class StartPage(Frame):

   def __init__(self, parent, controller, information):
      
      Frame.__init__(self, parent)

      screen_width = (self.winfo_screenwidth())
      screen_height = (self.winfo_screenheight()/1.1)

      font = int(screen_height/30)
      font_type = ("Arial", font)

      max_movement_speed = information["max_movement_speed"]


      Label(self,
            width = int(screen_width/180),
            height = int(screen_height/300)
      ).grid(row = 1, column = 1, sticky="nsew")

      Run = Button(self,
                   text = " Run ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300),
                   bg = "green")
      Run.grid(row = 1, column = 2, columnspan = 2, sticky="nsew")

      AutoPilot = Button(self,
                   text = " Computer\n Auto Pilot ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300))
      AutoPilot.grid(row = 1, column = 4, columnspan = 2, sticky="nsew")

      Manual = Button(self,
                   text = " Full Manual ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300),
                   command = lambda: controller.show_frame(SecondPage))
      Manual.grid(row = 1, column = 6, columnspan = 2, sticky="nsew")

      Calibration = Button(self,
                   text = " \"Auto\"\n Calibration ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300))
      Calibration.grid(row = 1, column = 8, columnspan = 2, sticky="nsew")

      Label(self,
            width = int(screen_width/150),
            height = int(screen_height/300)
      ).grid(row = 2, column = 1, columnspan = 9,sticky="nsew")

      PanLeft = Button(self,
                   text = " Pan ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      PanLeft.grid(row = 3, column = 2, sticky="nsew")

      PanRight = Button(self,
                   text = " -Pan ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      PanRight.grid(row = 3, column = 3, sticky="nsew")

      TiltLeft = Button(self,
                   text = " Tilt ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      TiltLeft.grid(row = 4, column = 2, sticky="nsew")

      TiltRight = Button(self,
                   text = " -Tilt ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      TiltRight.grid(row = 4, column = 3, sticky="nsew")

      YawLeft = Button(self,
                   text = " Yaw ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      YawLeft.grid(row = 5, column = 2, sticky="nsew")

      YawRight = Button(self,
                   text = " -Yaw ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   state = DISABLED)
      YawRight.grid(row = 5, column = 3, sticky="nsew")

      SpeedScale = Scale(self,
                         orient=HORIZONTAL,
                         from_=0.1,
                         to=max_movement_speed,
                         resolution=0.1)
      SpeedScale.grid(row = 4, column = 8, sticky="nsew")

      Forward = Button(self,
                   text = " Forward ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_forward(SpeedScale.get()))
      Forward.grid(row = 3, column = 5, sticky="nsew")

      Backward = Button(self,
                   text = " Backward ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_backward(SpeedScale.get()))
      Backward.grid(row = 5, column = 5, sticky="nsew")

      Left = Button(self,
                   text = " Left ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_left(SpeedScale.get()))
      Left.grid(row = 4, column = 4, sticky="nsew")

      Right = Button(self,
                   text = " Right ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_right(SpeedScale.get()))
      Right.grid(row = 4, column = 6, sticky="nsew")

      Up = Button(self,
                   text = " Up ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_up(SpeedScale.get()))
      Up.grid(row = 3, column = 7, sticky="nsew")

      Down = Button(self,
                   text = " Down ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200),
                   repeatdelay=1,
                   repeatinterval = interval,
                   command = lambda: MOVEMENT.move_down(SpeedScale.get()))
      Down.grid(row = 5, column = 7, sticky="nsew")

      result = Label(self,
                  text = "Current Speed:\n %d cm/s" % ((SpeedScale.get())),
                  font = (font_type),
                  width = int(screen_width/80),
                  height = int(screen_height/200))
      result.grid(row = 3, column = 8, sticky="nsew")



      #Changes the speed on the display and then updates it every 1 milliseconds or every 0.001 second.
      def update():
         result.config(text = "Current Speed:\n %d m/s" % ((SpeedScale.get())))
         self.update()
         self.after(1, update)

      #Updates the frame.
      self.after(1, update)



#Second Page.
class SecondPage(Frame):
   
   def __init__(self, parent, controller, information):
      
      Frame.__init__(self, parent)

      screen_width = (self.winfo_screenwidth())
      screen_height = (self.winfo_screenheight()/1.1)

      font = int(screen_height/30)
      font_type = ("Arial", font)

      Label(self,
            width = int(screen_width/180),
            height = int(screen_height/300)
      ).grid(row = 1, column = 1, sticky="nsew")

      Label(self,
            width = int(screen_width/180),
            height = int(screen_height/50)
      ).grid(row = 6, column = 1, sticky="nsew")

      Run = Button(self,
                   text = " Run ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300),
                   command = lambda: controller.show_frame(StartPage))
      Run.grid(row = 1, column = 2, columnspan = 2, sticky="nsew")

      AutoPilot = Button(self,
                   text = " Computer\n Auto Pilot ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300))
      AutoPilot.grid(row = 1, column = 4, columnspan = 2, sticky="nsew")

      Manual = Button(self,
                   text = " Full Manual ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300),
                   bg = "green")
      Manual.grid(row = 1, column = 6, columnspan = 2, sticky="nsew")

      Calibration = Button(self,
                   text = " \"Auto\"\n Calibration ",
                   font = (font_type),
                   width = int(screen_width/150),
                   height = int(screen_height/300))
      Calibration.grid(row = 1, column = 8, columnspan = 2, sticky="nsew")

      Label(self,
            width = int(screen_width/150),
            height = int(screen_height/300)
      ).grid(row = 2, column = 1, columnspan = 9,sticky="nsew")

      Motor1 = Button(self,
                   text = " Tighten ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor1.grid(row = 3, column = 2, sticky="nsew")

      result = Label(self,
                  text = "Motor1",
                  font = (font_type),
                  width = int(screen_width/190),
                  height = int(screen_height/200))
      result.grid(row = 4, column = 2, sticky="nsew")

      Motor1 = Button(self,
                   text = " Loosen ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor1.grid(row = 5, column = 2, sticky="nsew")

      Motor2 = Button(self,
                   text = " Tighten ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor2.grid(row = 3, column = 3, sticky="nsew")

      result = Label(self,
                  text = "Motor2",
                  font = (font_type),
                  width = int(screen_width/190),
                  height = int(screen_height/200))
      result.grid(row = 4, column = 3, sticky="nsew")

      Motor2 = Button(self,
                   text = " Loosen ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor2.grid(row = 5, column = 3, sticky="nsew")

      Motor3 = Button(self,
                   text = " Tighten ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor3.grid(row = 3, column = 4, sticky="nsew")

      result = Label(self,
                  text = "Motor3",
                  font = (font_type),
                  width = int(screen_width/190),
                  height = int(screen_height/200))
      result.grid(row = 4, column = 4, sticky="nsew")

      Motor3 = Button(self,
                   text = " Loosen ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor3.grid(row = 5, column = 4, sticky="nsew")

      Motor4 = Button(self,
                   text = " Tighten ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor4.grid(row = 3, column = 5, sticky="nsew")

      result = Label(self,
                  text = "Motor4",
                  font = (font_type),
                  width = int(screen_width/190),
                  height = int(screen_height/200))
      result.grid(row = 4, column = 5, sticky="nsew")

      Motor4 = Button(self,
                   text = " Loosen ",
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Motor4.grid(row = 5, column = 5, sticky="nsew")

      Blank1 = Button(self,
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Blank1.grid(row = 7, column = 6, sticky="nsew")

      Blank2= Button(self,
                   font = (font_type),
                   width = int(screen_width/190),
                   height = int(screen_height/200))
      Blank2.grid(row = 7, column = 7, sticky="nsew")

      SpeedIncrease = Button(self,
                     font = (font_type),
                     text = " Speed + ",
                     width = int(screen_width/190),
                     height = int(screen_height/200))
      SpeedIncrease.grid(row = 3, column = 8, columnspan = 2, sticky="nsew")

      result = Label(self,
                     text = "Motor Adjust Speed",
                     font = (font_type),
                     width = int(screen_width/80),
                     height = int(screen_height/200))
      result.grid(row = 4, column = 8, sticky="nsew")

      SpeedDecrease = Button(self,
                      text = " Speed - ",
                      font = (font_type),
                      width = int(screen_width/190),
                      height = int(screen_height/200))
      SpeedDecrease.grid(row = 5, column = 8, columnspan = 2, sticky="nsew")


#Configure Page.
class ConfigPage(Frame):
   
    def __init__(self, parent, controller, information):
      
        Frame.__init__(self, parent)

        screen_width = (self.winfo_screenwidth())
        screen_height = (self.winfo_screenheight()/1.1)

        font = int(screen_height/30)
        font_type = ("Arial", font)

        #Configurable Constants.
        self.stuff = information
         
        Run = Button(self,
                     text = " Default ",
                     font = (font_type),
                     width = int(screen_width/150),
                     height = int(screen_height/300),
                     command = lambda: controller.show_frame(StartPage))
        Run.grid(row = 1, column = 2, columnspan = 2, sticky="nsew")
