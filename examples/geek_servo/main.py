from motorbit import MotorBit
import time

motorbit = MotorBit()

motorbit.pca9685.frequency = 50

while True:
    degree = 0
    motorbit.geek_servo_degree(MotorBit.S1, degree)
    motorbit.geek_servo_degree(MotorBit.S2, degree)
    motorbit.geek_servo_degree(MotorBit.S3, degree)
    motorbit.geek_servo_degree(MotorBit.S4, degree)
    motorbit.geek_servo_degree(MotorBit.S5, degree)
    motorbit.geek_servo_degree(MotorBit.S6, degree)
    motorbit.geek_servo_degree(MotorBit.S7, degree)
    motorbit.geek_servo_degree(MotorBit.S8, degree)
    print('degree:', degree)
    time.sleep(1)

    degree = 90
    motorbit.geek_servo_degree(MotorBit.S1, degree)
    motorbit.geek_servo_degree(MotorBit.S2, degree)
    motorbit.geek_servo_degree(MotorBit.S3, degree)
    motorbit.geek_servo_degree(MotorBit.S4, degree)
    motorbit.geek_servo_degree(MotorBit.S5, degree)
    motorbit.geek_servo_degree(MotorBit.S6, degree)
    motorbit.geek_servo_degree(MotorBit.S7, degree)
    motorbit.geek_servo_degree(MotorBit.S8, degree)
    print('degree:', degree)
    time.sleep(1)

    degree = 180
    motorbit.geek_servo_degree(MotorBit.S1, degree)
    motorbit.geek_servo_degree(MotorBit.S2, degree)
    motorbit.geek_servo_degree(MotorBit.S3, degree)
    motorbit.geek_servo_degree(MotorBit.S4, degree)
    motorbit.geek_servo_degree(MotorBit.S5, degree)
    motorbit.geek_servo_degree(MotorBit.S6, degree)
    motorbit.geek_servo_degree(MotorBit.S7, degree)
    motorbit.geek_servo_degree(MotorBit.S8, degree)
    print('degree:', degree)
    time.sleep(1)
