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

#this is used for homing the 0 position of the camera and set the variables on the aurduinos to the correct value
def zero_reset():
    COMMUNICATION.mode = "s"
    COMMUNICATION.M1_Position = MATH.motorangle(MATH.motor1,(0),(0),(0))
    COMMUNICATION.M1_Speed = MATH.motorspeed(MATH.motor1,(0),(0),(0),(1),(1),(1))
    COMMUNICATION.M2_Position = MATH.motorangle(MATH.motor2,(0),(0),(0))
    COMMUNICATION.M2_Speed = MATH.motorspeed(MATH.motor2,(0),(0),(0),(1),(1),(1))
    COMMUNICATION.M3_Position = MATH.motorangle(MATH.motor3,(0),(0),(0))
    COMMUNICATION.M3_Speed = MATH.motorspeed(MATH.motor3,(0),(0),(0),(1),(1),(1))
    COMMUNICATION.M4_Position = MATH.motorangle(MATH.motor4,(0),(0),(0))
    COMMUNICATION.M4_Speed = MATH.motorspeed(MATH.motor4,(0),(0),(0),(1),(1),(1))
    COMMUNICATION.mode = "r" #thought just in case

#move the camera up (towards -Z)
def move_up(speed):
    if camera.z > 0:
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

#move the camera down (towards +z)
def move_down(speed):
    if camera.z < config.intormation["max_z"]:
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

#moce the camera left (towards +x)
def move_left(speed):
    if camera.x < config.intormation["max_x"]:
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

#move the camera right (towards -x)
def move_right(speed):
    if camera.x> 0:
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

#move camera foward (towards -y)
def move_forward(speed):
    if camera.y> 0:
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

#move camera back (towards +y)
def move_backward(speed):
    if camera.y < config.intormation["max_y"]:
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
