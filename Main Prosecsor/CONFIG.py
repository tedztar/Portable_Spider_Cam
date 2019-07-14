#Import external library.
from configparser import ConfigParser

#This recovers and returns data from the file. Return (Object.)
def ImportFile():
    if FileDoesNotExist():
        SetAsDefaultObject(temporaryData)
        ExportDataToFile()

    #Collect data from the file into temporary data. Then get it checked before using it.
    temporaryData.read(fileName)     
    CheckFileCategories()
    
    return temporaryData.read(fileName) 

#Does the file exist? If we can read it then it does exist. Return (Boolean.)
def FileDoesNotExist():
    try:
        OpenFileTo(read)
        return False

    except FileNotFoundError:
        return True

#Access the file to write/read data.
def OpenFileTo(option):
    return open(fileName, str(option))

#This is the default data structure if an object has no data structure in it.
def SetAsDefaultObject(thisObject):
    thisObject["General"]= {
      "run_speed" : "value", #Put higher if computer is slow, movement will be less smooth. Put lower if computer is not lagging, movement will be more smooth.
      "max_x" : "value", #Set as the width (in cm) of the "box" that the camera can fly in.
      "max_y" : "value", #Set as the length (in cm) of the "box" that the camera can fly in.
      "max_z" : "value", #Set as the hight (in cm) of the "box" that the camera can fly in.
      "camera_a" : "value", #Set as half the width (in cm) of the mount connected to the wires.
      "max_movement_speed" : "value", #Set as the speed (in cm/s) of the camera.
    }

    thisObject["Motor"] = {
      "drum_radious" : "value", #Set as the radious (in cm) of the drum for the winch stations.
      "drum_gears" : "value", #Set as the number of gears that the drum of the winch has (set to 1 if direct drive.)
      "motor_gears" : "value", #Set as the number of gears that the motor of the winch has (set to 1 if direct drive.)
    }

    return

#Export the data and write it into the file. 
def ExportDataToFile():
    with OpenFileTo(write) as dataIntoFile:
        temporaryData.write(dataIntoFile)

def CheckFileCategories():
    categoryList = referenceData.sections()

    #Does the category exist.
    for selectedCategory in temporaryData:
        if selectedCategory in categoryList:
            CheckFileSubcategories(selectedCategory)
            categoryList.remove(selectedCategory)

        else:
            #This category should not exist and will be removed.
            temporaryData.remove_section(selectedCategory)
            
    #Add missing categories.
    for missingCategory in categoryList:
        temporaryData.add_section(missingCategory)
        CheckFileSubcategories(missingCategory)
        categoryList.remove(missingCategory)

    ExportDataToFile()
    
    return

def CheckFileSubcategories(selectedCategory):
    subcategoryList = referenceData.options(selectedCategory)

    #Does the subcategory exist.
    for selectedSubcategory in temporaryData.options(selectedCategory):
        if selectedSubcategory in subcategoryList:
            CheckValue(selectedCategory, selectedSubcategory)
            subcategoryList.remove(str(selectedSubcategory))

        else:
            #This subcategory should not exist and will be removed.
            temporaryData.remove_option(selectedCategory, selectedSubcategory)

    #Add missing subcategories.
    for missingSubcategory in subcategoryList:
        temporaryData.set(selectedCategory, missingSubcategory,
                          referenceData.get(selectedCategory, missingSubcategory))
        CheckValue(selectedCategory, missingSubcategory)
        referenceData.remove_option(selectedCategory, missingSubcategory)

    return

#Check if the value is a integer.
def CheckValue(selectedCategory, selectedSubcategory):
    valueNotValid = True
    
    try:
        #If the values are not integers then it will send an error "ValueError".
        valueRetrieved = int(temporaryData.get(selectedCategory, selectedSubcategory))

        #If the value is a positive integer or 0 then allow it to pass.
        if valueRetrieved >= 0:
            valueNotValid = False

    except ValueError:
        pass

    if valueNotValid:
        #Send feedback that this value needs to be changed in the file.
        print("{} in {} needs to be configured.".format(selectedSubcategory, selectedCategory))

    return

#This saves the data to the file.
def ExportFile(exportData):
        temporaryData = exportData
        ExportDataToFile()

        return

#This allows you to create class/object orientated storage files.
def IntoStorableObject():
    return ConfigParser(allow_no_value=True)

#This will carry temporary data between the file and reference.
temporaryData = IntoStorableObject()

#This will be a reference to ensure the data structure is correct.
referenceData = IntoStorableObject()
SetAsDefaultObject(referenceData)

fileName = "config.ini"

#Options to access the file.
write = "w"
read = "r"
