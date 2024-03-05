from motorbit import MotorBit
import time

motorbit = MotorBit()
motorbit.pca9685.frequency = 50

while True:
    speed = 2048
    motorbit.dc_speed(MotorBit.M1, speed)
    motorbit.dc_speed(MotorBit.M2, speed)
    motorbit.dc_speed(MotorBit.M3, speed)
    motorbit.dc_speed(MotorBit.M4, speed)
    print('speed:', speed)
    time.sleep(1)

    speed = -2048
    motorbit.dc_speed(MotorBit.M1, speed)
    motorbit.dc_speed(MotorBit.M2, speed)
    motorbit.dc_speed(MotorBit.M3, speed)
    motorbit.dc_speed(MotorBit.M4, speed)
    print('speed:', speed)
    time.sleep(1)
