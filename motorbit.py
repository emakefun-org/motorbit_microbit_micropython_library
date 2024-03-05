from pca9685 import PCA9685


class MotorBit:
    M1 = 0
    M2 = 1
    M3 = 2
    M4 = 3

    S1 = 8
    S2 = 9
    S3 = 10
    S4 = 11
    S5 = 12
    S6 = 13
    S7 = 14
    S8 = 15

    def __init__(self) -> None:
        self._pca9685 = PCA9685()

    @property
    def pca9685(self) -> PCA9685:
        return self._pca9685

    def dc_speed(self, port, speed):
        if port < MotorBit.M1 or port > MotorBit.M4:
            raise ValueError("{} is out of range for port ({} - {})".format(
                port, MotorBit.M1, MotorBit.M4))

        if speed < -4095 or speed > 4095:
            raise ValueError(
                "{} is out of range for speed (-4095 - 4095)".format(speed))

        if speed >= 0:
            self._pca9685.pwm(port << 1, 0, abs(speed))
            self._pca9685.pwm((port << 1) + 1, 0, 0)
        else:
            self._pca9685.pwm((port << 1) + 1, 0, abs(speed))
            self._pca9685.pwm(port << 1, 0, 0)

    def servo_degree(self, port, degree):
        if port < MotorBit.S1 or port > MotorBit.S8:
            raise ValueError("{} is out of range for port ({} - {})".format(
                port, MotorBit.S1, MotorBit.S8))

        if degree < 0 or degree > 180:
            raise ValueError(
                "{} is out of range for degree (0 - 180)".format(degree))

        self._pca9685.pwm(port, 0, int((degree / 90 + 0.5) / 20 * 4095))

    def geek_servo_degree(self, port, degree):
        if port < MotorBit.S1 or port > MotorBit.S8:
            raise ValueError("{} is out of range for port ({} - {})".format(
                port, MotorBit.S1, MotorBit.S8))

        if degree < 0 or degree > 180:
            raise ValueError(
                "{} is out of range for degree (0 - 180)".format(degree))

        duty = (0.9 + (degree / 180) * (2.2 - 0.9)) / 20 * 4095

        self._pca9685.pwm(port, 0, int(duty))
