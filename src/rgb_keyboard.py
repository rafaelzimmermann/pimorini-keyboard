import time
from machine import I2C, Pin, SPI

SDA = 4
SCL = 5
CS = 17
SCK = 18
MOSI = 19
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
        self.cs = Pin(CS, mode=Pin.OUT, value=1)
        self.spi = SPI(0, baudrate=SCK_CLOCK_RATE, sck=Pin(SCK), mosi=Pin(MOSI))
        self._led_data = [[float_to_brightness(DEFAULT_BRIGHTNESS), 0, i, 32] for i in range(0, NUM_PADS + 1)]
        self.update()
        time.sleep(1)
        self.clear()
        self.update()

    def update(self):
        print(self._led_data)
        try:
            self.cs(0)
            buffer = self.led_data_bytes
            self.spi.read(len(buffer))
            self.spi.write(buffer)
        finally:
            self.cs(1)

    def set_brightness(self, value: float):
        for i in range(0, NUM_PADS + 1):
            self.set_button_brightness(i, value)

    def set_button_brightness(self, button_index: int, value: float):
        self._led_data[button_index][BRIGHTNESS_INDEX] = float_to_brightness(value)

    def set_button_color(self, button_index: int, r: int, g: int, b: int):
        print(f"Button {button_index}: R({r}) G({g}) B({b})")
        self._led_data[button_index][R_INDEX] = r
        self._led_data[button_index][G_INDEX] = g
        self._led_data[button_index][B_INDEX] = b

    def clear(self):
        self._led_data = [[float_to_brightness(DEFAULT_BRIGHTNESS), 0, 0, 0] for _ in range(0, NUM_PADS + 1)]

    @property
    def button_state(self):
        i2c = I2C(0, freq=FREQUENCY, sda=Pin(SDA), scl=Pin(SCL))
        try:
            i2c.writeto(KEYPAD_ADDRESS, bytes(1))
            buffer = i2c.readfrom(KEYPAD_ADDRESS, 2, False)
            result = ~((buffer[0]) | (buffer[1] << 8))
            print(result)
            return result
        except Exception as e:
            print(e)

    @property
    def led_data_bytes(self) -> bytes:
        result = []
        for x in self._led_data:
            for y in x:
                result.append(y)
        return bytes(result)
