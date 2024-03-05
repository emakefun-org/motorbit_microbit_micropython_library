import math
import time
import struct
from microbit import i2c


class PCA9685:
    MODE1 = 0x00
    MODE2 = 0x01
    SUBADR1 = 0x02
    SUBADR2 = 0x03
    SUBADR3 = 0x04
    PRESCALE = 0xFE
    LED0_ON_L = 0x06
    LED0_ON_H = 0x07
    LED0_OFF_L = 0x08
    LED0_OFF_H = 0x09
    ALL_LED_ON_L = 0xFA
    ALL_LED_ON_H = 0xFB
    ALL_LED_OFF_L = 0xFC
    ALL_LED_OFF_H = 0xFD

    def __init__(self, i2c_address=0x40) -> None:
        self._i2c_address = i2c_address
        i2c.write(self._i2c_address, bytes([PCA9685.MODE1, 0x00]))
        self.frequency = 50
        for i in range(16):
            self.pwm(i, 0, 0)

    @property
    def frequency() -> None:
        return None

    @frequency.setter
    def frequency(self, frequency_hz) -> None:
        prescaler = 25000000.0  # 25MHz
        prescaler /= 4096.0  # 12-bit
        prescaler /= float(frequency_hz)
        prescaler -= 1.0
        prescaler = int(math.floor(prescaler + 0.5))
        i2c.write(self._i2c_address, bytes([PCA9685.MODE1]))
        old_mode = i2c.read(self._i2c_address, 1)[0]
        new_mode = (old_mode & 0x7F) | 0x10  # sleep
        i2c.write(self._i2c_address, bytes([PCA9685.MODE1, new_mode]))
        i2c.write(self._i2c_address, bytes([PCA9685.PRESCALE, prescaler]))
        i2c.write(self._i2c_address, bytes([PCA9685.MODE1, old_mode]))
        time.sleep(0.005)
        i2c.write(self._i2c_address, bytes([PCA9685.MODE1, old_mode | 0xA1]))

    def pwm(self, channel, on, off):
        if channel < 0 or channel > 15:
            raise ValueError(
                "{} is out of range for channel (0-15)".format(channel))

        if on < 0 or on > 4095:
            raise ValueError("{} is out of range for on (0-4095)".format(on))

        if off < 0 or off > 4095:
            raise ValueError("{} is out of range for off (0-4095)".format(off))

        i2c.write(
            self._i2c_address,
            bytes([(channel << 2) + PCA9685.LED0_ON_L]) +
            struct.pack("<HH", on, off))
