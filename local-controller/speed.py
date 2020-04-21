import pigpio
pi = pigpio.pi()
pi.set_mode(12, pigpio.OUTPUT)

freq = 50

# 1000us
duty_forward = 50000
# 1500us
duty_neutral = 75000
# 1750us
duty_reverse = 87500

pi.hardware_PWM(12, freq, duty_neutral)