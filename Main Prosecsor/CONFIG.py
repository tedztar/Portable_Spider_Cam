#Import external library.
from configparser import ConfigParser



#Does the file exist? If we can read it then it does exist.
def read_file():

   #Give reading the program a try.
   try:
      #File name, read.
      open(file, "r")

      #This creates a reference list which we will use to check for any updates in changes.
      create_file(reference)

      #Is the file ready for running.
      valid = True



      #Create a category reference list based off the default list.
      info = reference.sections()

      #Set the file categories to the config functions.
      config.read(file)

      #Split the categories from the file.
      for category in config.sections():

         #Do all categories exist in the file. 
         if category in info:
            info.remove(category)

         #If the category doesn't exist, remove it.
         else:
            config.remove_section(category)

      #If there isn't a category, create the missing categories.
      for category in info:
         config.add_section(category)
      
      write_file()

    

      #Create a sub_category reference list.
      info = []

      #Take each category and turn all the sub categories into one list.
      for category in reference.sections():
         
         sub_category = reference.options(str(category))
         
         #Add the sub category list into the main list. 
         info.append(sub_category)

      #With the list inside a list reference, it also needs an index.
      index = int(0)

      #Loop each category to check if the sub_categories exist.
      for category in config.sections():

            #This chooses the sub_categories to check against.
            task = info[index]

            #This is to help prevent errors as subcategories lowercase automatically.
            work = [ sub_category.lower() for sub_category in task] 

            #Loop each sub_category to check if the sub_categories is equal.
            for sub_category in config.options(category):

               #Do all sub_categories exist in the category.
               if sub_category in work:
                  work.remove(sub_category)

               #If the sub_category doesn't exist, remove it.
               else:
                  config.remove_option(category, sub_category)

            #If the sub categories don't exist then create them.
            for sub_category in work:
                config.set(category, sub_category, reference.get(category, sub_category))

            #Once it is done, add one to the index for the next list.
            index += 1

      write_file()

            

      #Check if the values are integers.
      for category in config.sections():
         for sub_category in config.options(category):

            result = True

            #If the values are not integers then it will send an error "ValueError".
            try:
               check_value = int(config.get(category, sub_category))

               #If the value is a positive integer or 0 then allow it to pass.
               if check_value >= 0:
                  pass

               #If the value does not get accepted as greater or equal to 0, then set result as False.
               else:
                  result = False

            #Send feedback if a value needs to be changed.
            except ValueError:
               result = False

            #If the value does not meet the requirements, inform the user to configure the config file.
            if not result:

               #The exact line that needs to be configured.
               print("{} in {} needs to be configured.".format(str(sub_category).capitalize(), category))
               valid = False

      write_file()  
      return valid



   #If it cannot find the file it will return an Error "FileNotFound".
   except FileNotFoundError:
      create_file(config)

      write_file()
      read_file()

   return



#This file does not exist. Create the factory default file.
def create_file(file):

   #Create the category and set the sub_catergories.
   file["General"] = {
      "run_speed" : "value", #Put higher if computer is slow, movement will be less smooth. Put lower if computer is not laging, movement will be smother.
      "max_x" : "value", #Set as the width (in cm) of the "box" that the camera can fly in.
      "max_y" : "value", #Set as the length (in cm) of the "box" that the camera can fly in.
      "max_z" : "value", #Set as the hight (in cm) of the "box" that the camera can fly in.
      "camera_a" : "value", #Set as half the width (in cm) of the mount connected to the wires.
      "max_movement_speed" : "value", #Set as the speed (in cm/s) of the camera.
      }

   file["Motor"] = {
      "drum_radious" : "value", #Set as the radious (in cm) of the drum for the winch stations.
      "drum_gears" : "value", #Set as the number of gears that the drum of the winch has (set to 1 if direct drive.)
      "motor_gears" : "value", #Set as the number of gears that the motor of the winch has (set to 1 if direct drive.)
      }

   return



# This recovers and returns information.
def import_file():

    #Check if the config files exist and setup.
    valid = read_file()



    #Information to return.
    information = {}



    #Recovers the information from the file into the two Information lists.
    for category in config.sections():
        for sub_category in config.options(category):

            value_str = (sub_category)
            value_int = (config.get(category, sub_category))

            information[value_str] = value_int



    return (information, valid)



#Writes to the file.
def export_file(information):

   
    #Opens the dictionary.
    for (key, value) in information.items():

        #Go through each constant.
        for category in config.sections():
            for sub_category in config.options(category):

                #Checks if any constants are changed.
                if information[key] == sub_category:
                    config.set(category, sub_category, str(information[value]))

                else:
                    pass


    #Updates the file with the new values.
    write_file()
    return()



#Write information to the config file.
def write_file():

  #Create a file to set the catergories and sub_catergories in.
  with open(file, "w") as file_name:
      
      #Write the factory default file.
      config.write(file_name)

  return



#This sets up the file.
name = "config"
extension = ".ini"
file = name + extension

#This allows you to create class/object orientated storage files.
config = ConfigParser(allow_no_value=True)
reference = ConfigParser(allow_no_value=True)
