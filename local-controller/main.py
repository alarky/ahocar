import pygame
from pygame.locals import *
import pigpio

LSTICK_X = 0
LSTICK_Y = 1
RSTICK_X = 2
RSTICK_Y = 3
L2 = 4
R2 = 5

SPEED_GPIO = 12
STEER_GPIO = 13
FREQUENCY = 50

pygame.joystick.init()
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print('Joystick Name:', joystick.get_name())
    print('Number of Buttons :', joystick.get_numbuttons())
    print("Number of Axis : " + str(joystick.get_numaxes()))
    print("Number of Hats : " + str(joystick.get_numhats()))
except pygame.error:
    print('Joystick Not Found')
    exit(1)
except Exception as e:
    print(e)
    exit(1)

pi = pigpio.pi()
pi.set_mode(SPEED_GPIO, pigpio.OUTPUT)
pi.set_mode(STEER_GPIO, pigpio.OUTPUT)

pygame.init()

steer = 0
speed = 0
brake = 0
accel = 0

while True:
    try:
        for e in pygame.event.get():
            if e.type == JOYAXISMOTION:
                steer = joystick.get_axis(LSTICK_X)
                brake = joystick.get_axis(L2)
                accel = joystick.get_axis(R2)
                break

        if brake > -0.9:
            if speed > 0:
                speed = 0
            else:
                speed = -(brake + 1.0) / 4
        elif ((accel + 1.0) / 2) >= speed:
            speed = (accel + 1.0) / 2
        elif speed > 0:
            speed -= 1
            if speed < 0:
                speed = 0

        print(f"steer: {steer}, brake: {brake}, accel: {accel}, speed: {speed}")
        pi.hardware_PWM(STEER_GPIO, FREQUENCY, 75000 + int(steer * 25000))
        pi.hardware_PWM(SPEED_GPIO, FREQUENCY, 75000 + int(-speed * 25000))
    except KeyboardInterrupt:
        break
