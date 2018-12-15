import math

class calculation:

   def find_length1(var):
      
      length = int(math.sqrt( ( var[0]-var[6] )**2 + ( var[4]-var[1]-var[6] )**2 + ( var[5]-var[2] )**2 ))
      
      return length

   def find_length2(var):
      
      length = int(math.sqrt( ( var[3]-var[0]-var[6] )**2 + ( var[4]-var[1]-var[6] )**2 + ( var[5]-var[2] )**2 ))
      
      return length

   def find_length3(var):
      
      length = int(math.sqrt( ( var[0]-var[6] )**2 + ( var[1]-var[6] )**2 + ( var[5]-var[2] )**2 ))
      
      return length

   def find_length4(var):
      
      length = int(math.sqrt( ( var[3]-var[0]-var[6] )**2 + ( var[1]-var[6] )**2 + ( var[5]-var[2] )**2 ))
      
      return length
