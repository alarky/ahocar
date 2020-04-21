import pigpio
pi = pigpio.pi()
pi.set_mode(13, pigpio.OUTPUT)

freq = 50

# 1000us
duty_left = 50000
# 1500us
duty_center = 75000
# 2000us
duty_right = 100000

pi.hardware_PWM(13, freq, duty_center)
