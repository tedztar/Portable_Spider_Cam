#this contolls the movement of the platfom (not the gimbal)
import MATH
import CONFIG
import COMMUNICATION

class cam:
    #inisiates all variables relating to a spisific motor
     def __init__(self):
          step = int()
          self.x = int()
          self.y = int()
          self.z = int()

camera=cam()

def move_up(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x),(camera.y),(camera.z-step))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x),(camera.y),(camera.z-step))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x),(camera.y),(camera.z-step))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x),(camera.y),(camera.z-step))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x),(camera.y),(camera.z-step),(speed),(speed),(speed))
    camera.z += step
def move_down(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x),(camera.y),(camera.z+step))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x),(camera.y),(camera.z+step))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x),(camera.y),(camera.z+step))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x),(camera.y),(camera.z+step))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x),(camera.y),(camera.z+step),(speed),(speed),(speed))
    camera.z -= step
def move_left(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x + step),(camera.y),(camera.z))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x + step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x + step),(camera.y),(camera.z))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x + step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x + step),(camera.y),(camera.z))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x + step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x + step),(camera.y),(camera.z))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x + step),(camera.y),(camera.z),(speed),(speed),(speed))
    camera.z += step
def move_right(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x - step),(camera.y),(camera.z))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x - step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x - step),(camera.y),(camera.z))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x - step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x - step),(camera.y),(camera.z))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x - step),(camera.y),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x - step),(camera.y),(camera.z))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x - step),(camera.y),(camera.z),(speed),(speed),(speed))
    camera.x -= step
def move_forward(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x),(camera.y - step),(camera.z))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x),(camera.y - step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x),(camera.y - step),(camera.z))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x),(camera.y - step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x),(camera.y - step),(camera.z))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x),(camera.y - step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x),(camera.y - step),(camera.z))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x),(camera.y - step),(camera.z),(speed),(speed),(speed))
    camera.y -= step
def move_backward(speed):
    COMMUNICATION.mode = "r"
    step = CONFIG.information["run_speed"]/speed
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(camera.x),(camera.y + step),(camera.z))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(camera.x),(camera.y + step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(camera.x),(camera.y + step),(camera.z))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(camera.x),(camera.y + step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(camera.x),(camera.y + step),(camera.z))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(camera.x),(camera.y + step),(camera.z),(speed),(speed),(speed))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(camera.x),(camera.y + step),(camera.z))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(camera.x),(camera.y + step),(camera.z),(speed),(speed),(speed))
    camera.y += step
