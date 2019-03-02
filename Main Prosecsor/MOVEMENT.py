#this contolls the movement of the platfom (not the gimbal)
import MATH
import CONFIG

class camera:
    #inisiates all variables relating to a spisific motor
     def __init__(self):
          step = int()
          self.x = int()
          self.y = int()
          self.z = int()


def move_up(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z-step))
    M1_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x),(camera.y),(camera.z-step))
    M2_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x),(camera.y),(camera.z-step))
    M3_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x),(camera.y),(camera.z-step))
    M4_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
def move_down(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z+step))
    M1_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x),(camera.y),(camera.z+step))
    M2_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x),(camera.y),(camera.z+step))
    M3_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x),(camera.y),(camera.z+step))
    M4_Speed = MATH.motorangle(motor1,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
def move_left(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x+step),(camera.y),(camera.z))
    M1_Speed = MATH.motorangle(motor1,(camera.x+step),(camera.y),(camera.z),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x+step),(camera.y),(camera.z))
    M2_Speed = MATH.motorangle(motor1,(camera.x+step),(camera.y),(camera.z),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x+step),(camera.y),(camera.z))
    M3_Speed = MATH.motorangle(motor1,(camera.x+step),(camera.y),(camera.z),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x+step),(camera.y),(camera.z))
    M4_Speed = MATH.motorangle(motor1,(camera.x+step),(camera.y),(camera.z),(speed),(speed),(speed))
def move_right(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x-step),(camera.y),(camera.z))
    M1_Speed = MATH.motorangle(motor1,(camera.x-step),(camera.y),(camera.z),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x-step),(camera.y),(camera.z))
    M2_Speed = MATH.motorangle(motor1,(camera.x-step),(camera.y),(camera.z),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x-step),(camera.y),(camera.z))
    M3_Speed = MATH.motorangle(motor1,(camera.x-step),(camera.y),(camera.z),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x-step),(camera.y),(camera.z))
    M4_Speed = MATH.motorangle(motor1,(camera.x-step),(camera.y),(camera.z),(speed),(speed),(speed))
def move_forward(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x),(camera.y-step),(camera.z))
    M1_Speed = MATH.motorangle(motor1,(camera.x),(camera.y-step),(camera.z),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x),(camera.y-step),(camera.z))
    M2_Speed = MATH.motorangle(motor1,(camera.x),(camera.y-step),(camera.z),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x),(camera.y-step),(camera.z))
    M3_Speed = MATH.motorangle(motor1,(camera.x),(camera.y-step),(camera.z),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x),(camera.y-step),(camera.z))
    M4_Speed = MATH.motorangle(motor1,(camera.x),(camera.y-step),(camera.z),(speed),(speed),(speed)) 
def move_backward(speed):
    step = CONFIG.information["run_speed"]/speed
    M1_Position = MATH.motorangle(motor1,(camera.x),(camera.y+step),(camera.z))
    M1_Speed = MATH.motorangle(motor1,(camera.x),(camera.y+step),(camera.z),(speed),(speed),(speed))
    M2_Position = MATH.motorangle(motor2,(camera.x),(camera.y+step),(camera.z))
    M2_Speed = MATH.motorangle(motor1,(camera.x),(camera.y+step),(camera.z),(speed),(speed),(speed))
    M3_Position = MATH.motorangle(motor3,(camera.x),(camera.y+step),(camera.z))
    M3_Speed = MATH.motorangle(motor1,(camera.x),(camera.y+step),(camera.z),(speed),(speed),(speed))
    M4_Position = MATH.motorangle(motor4,(camera.x),(camera.y+step),(camera.z))
    M4_Speed = MATH.motorangle(motor1,(camera.x),(camera.y+step),(camera.z),(speed),(speed),(speed))
