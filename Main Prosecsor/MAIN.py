#this is the main script that contols everything
from COMMUNICATION import *
from CONFIG import *
from GUI import *
from MATH import *
from MOVEMENT import *

#setup code (stuff that is run during startup



#This gathers the key pieces of information inside the program.
#(information, valid) = import_file()
(valid) = import_file()
#Does the user need to update the values.

#This creates the GUI and sends the information to setup the GUI up.
app = SampleApp(information)



#If you wish to add more frames, put the name in here, then create a new object.
#This also allows you to recover information from each frame.

#Sets up the frames.
def setup_frame(frame_name):

    frame = frame_name(app.container, app, information)
    app.frames[frame_name] = frame
    frame.grid(row=0, column=0, sticky="nsew")

    return frame

#These are the Frames.
start = setup_frame(StartPage)
second = setup_frame(SecondPage)
config = setup_frame(ConfigPage)






#We can have a setup screen if needed.
if valid:
    
    app.show_frame(StartPage)

#The user can configurate the values.
else:
    
    app.show_frame(ConfigPage)


    
    #It takes the dictionary. Key is the string reference. value is the product of the key.
    for (key, value) in information.items():
        
        #Makes changes to the file.
        if information[str(key)] != config.stuff[str(key)]:
            information[key] = config.stuff[key]
        
        #If there is no changes then don't rewrite the value.
        else:
            pass



    #This writes to the file knowing the file exists.
    export_file(information)

app.mainloop()
