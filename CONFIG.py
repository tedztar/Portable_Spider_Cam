# Import external libraries.
from configparser import ConfigParser

# Does the file exist? If we can read it then it does exist.
def read_file():

   # Give reading the program a try.
   try:
      # File name, read.
      open("file_name.ini", "r")

      

      # Create a catergory Reference List.
      info = ["catergory1", "catergory2"]

      # Set the file catergories to the config functions.
      config.read("file_name.ini")

      # Split the catergories from the file.
      for catergory in config.sections():

         # Do all catergories exist in the file. 
         if catergory in info:
            info.remove(catergory)

         # If the catergory doesn't exist, remove it.
         else:
            config.remove_section(catergory)

      # If there isn't a catergory, create the missing catergories.
      for catergory in info:
         config.add_section(catergory)

      write_file()

    

      # Create a sub_catergory reference list.
      info = [
         ["sub_catergory1", "sub_catergory2"],
         ["sub_catergory1"],
         ]

      # With the list inside a list reference, it also needs an index.
      index = int(0)

      # Loop each catergory to check if the sub_catergories exist.
      for catergory in config.sections():

            # This chooses the sub_catergories to check against.
            task = info[index]

            # Loop each sub_catergory to check if the sub_catergories is equal.
            for sub_catergory in config.options(catergory):

               # Do all sub_catergories exist in the catergory.
               if sub_catergory in task:
                  task.remove(sub_catergory)

               # If the sub_catergory doesn't exist, remove it.
               else:
                  config.remove_option(catergory, sub_catergory)

            # If the sub catergories don't exist then create them.
            for sub_catergory in task:
               config.set(catergory, sub_catergory, "value")

            # Once it is done, add one to the index for the next list.
            index += 1

      write_file()



   # If it cannot find the file it will return an Error "FileNotFound".
   except FileNotFoundError:
      create_file()



# This file does not exist. Create the factory default file.
def create_file():

   # Create the catergory and set the sub_catergories.
   config["catergory1"] = {
      "sub_catergory1" : "value",
      "sub_catergory2" : "value",
      }

   config["catergory2"] = {
      "sub_catergory1" : "value",
      }

   write_file()
   read_file()



# Write information to the config file.
def write_file():

   # Create a file to set the catergories and sub_catergories in.
   with open("file_name.ini", "w") as file_name:
      # Write the factory default file.
      config.write(file_name)
      


# If this program is the main module. Run this code.
if __name__ == "__main__":

   #This allows you to create class/object orientated storage files.
   config = ConfigParser(allow_no_value=True)

   # 1.Step one, check if the config files exist.
   read_file()
