import board
import busio
import digitalio
import time

SDA = board.GP4
SCL = board.GP5
CS = board.GP17
SCK = board.GP18
MOSI = board.GP19

FREQUENCY = 400000
SCK_CLOCK_RATE = 4 * 1024 * 1024

WIDTH = 4
HEIGHT = 4
NUM_PADS = WIDTH * HEIGHT
DEFAULT_BRIGHTNESS = 0.5

BRIGHTNESS_INDEX = 0
R_INDEX = 1
G_INDEX = 2
B_INDEX = 3

KEYPAD_ADDRESS = 32


def float_to_brightness(value):
    return 0b11100000 | int((value * 0b11111))


class RGBKeyboard:

    def __init__(self):
        self.cs = digitalio.DigitalInOut(CS)
        self.cs.direction = digitalio.Direction.OUTPUT
        self.cs.value = 0

        self.spi = busio.SPI(SCK, MOSI=MOSI)
        self.i2c = busio.I2C(SCL, SDA)

        self._led_data = [[float_to_brightness(DEFAULT_BRIGHTNESS), 0, i, 32] for i in range(0, NUM_PADS + 1)]
        self.update()
        time.sleep(1)
        self.clear()
        self.update()

    def update(self):
        while not self.spi.try_lock():
            pass
        try:
            self.spi.configure(baudrate=SCK_CLOCK_RATE)
            self.cs.value = 0
            buffer = self.led_data_bytes
            read_buffer = bytearray(len(buffer))
            self.spi.readinto(read_buffer)
            self.spi.write(buffer)
        finally:
            self.spi.unlock()
            self.cs.value = 1

    def set_brightness(self, value: float):
        for i in range(0, NUM_PADS + 1):
            self.set_button_brightness(i, value)

    def set_button_brightness(self, button_index: int, value: float):
        self._led_data[button_index][BRIGHTNESS_INDEX] = float_to_brightness(value)

    def set_button_color(self, button_index: int, r: int, g: int, b: int):
        self._led_data[button_index][R_INDEX] = r
        self._led_data[button_index][G_INDEX] = g
        self._led_data[button_index][B_INDEX] = b

    def clear(self):
        self._led_data = [[float_to_brightness(DEFAULT_BRIGHTNESS), 0, 0, 0] for _ in range(0, NUM_PADS + 1)]

    @property
    def button_state(self):

        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(KEYPAD_ADDRESS, bytes(1))
            buffer = bytearray(2)
            self.i2c.readfrom_into(KEYPAD_ADDRESS, buffer)
            result = ~((buffer[0]) | (buffer[1] << 8))
            return result
        finally:
            self.i2c.unlock()

    @property
    def led_data_bytes(self) -> bytes:
        result = []
        for x in self._led_data:
            for y in x:
                result.append(y)
        return bytes(result)
