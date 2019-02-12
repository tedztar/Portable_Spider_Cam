#this is the main script that contols everything
from COMMUNICATION import *
from CONFIG import *
from GUI import *
from MATH import *
from MOVEMENT import *

#setup code (stuff that is run during startup



#This gathers the key pieces of information inside the program.
information = import_file()

#Does the user need to update the values.
valid = information[2]

#This creates the GUI and sends the information to setup the GUI up.
app = SampleApp(information)


#If you wish to add more frames, put the name in here, then create a new object.
#This also allows you to recover information from each frame.

#Would like to loop this if there is any way you can create a list of just variable names not strings.
start = StartPage(app.container, app, app.information)
app.frames[StartPage] = start
start.grid(row=0, column=0, sticky="nsew")

second = SecondPage(app.container, app, app.information)
app.frames[SecondPage] = second
second.grid(row=0, column=0, sticky="nsew")

config = ConfigPage(app.container, app, app.information)
app.frames[ConfigPage] = config
config.grid(row=0, column=0, sticky="nsew")



#We can have a setup screen if needed.
if valid:
    app.show_frame(StartPage)

#The user can configurate the values.
else:
    app.show_frame(ConfigPage)

    value_int = information[1]
    
    #I'll add something to check the values then pass them if they are correct.
    #Plus if there is a way we can convert string to variables that would be great here to loop.

    value_int[0] = config.run_speed
    value_int[1] = config.max_x
    value_int[2] = config.max_y
    value_int[3] = config.max_z
    value_int[4] = config.camera_a
    value_int[5] = config.max_movement_speed
    value_int[6] = config.drum_radious
    value_int[7] = config.drum_gears
    value_int[8] = config.motor_gears

    #This writes to the file knowing the file exists.
    export_file(value_int)

app.mainloop()
