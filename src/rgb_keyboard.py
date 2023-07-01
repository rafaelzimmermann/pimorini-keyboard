import board
import busio
import digitalio
import usb_hid
import random
import time

from key_parser import parse
from adafruit_hid.keyboard import Keyboard
from config import DEFAULT_COLOR
from passwd import PASS


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
R_INDEX = 3
G_INDEX = 2
B_INDEX = 1

KEYPAD_ADDRESS = 32

KEYS_PER_MINUTE = 1000
KEY_DELAY = (1 / float(KEYS_PER_MINUTE / 60)) / 2

BTN_0 = 12
BTN_1 = 8
BTN_2 = 4
BTN_3 = 0
BTN_4 = 13
BTN_5 = 9
BTN_6 = 5
BTN_7 = 1
BTN_8 = 14
BTN_9 = 10
BTN_A = 6
BTN_B = 2
BTN_C = 15
BTN_D = 11
BTN_E = 7
BTN_F = 3

BTN_VALUE = {}
BTN_VALUE[BTN_0] = 0
BTN_VALUE[BTN_1] = 1
BTN_VALUE[BTN_2] = 2
BTN_VALUE[BTN_3] = 3
BTN_VALUE[BTN_4] = 4
BTN_VALUE[BTN_5] = 5
BTN_VALUE[BTN_6] = 6
BTN_VALUE[BTN_7] = 7
BTN_VALUE[BTN_8] = 8
BTN_VALUE[BTN_9] = 9
BTN_VALUE[BTN_A] = "A"
BTN_VALUE[BTN_B] = "B"
BTN_VALUE[BTN_C] = "C"
BTN_VALUE[BTN_D] = "D"
BTN_VALUE[BTN_E] = "E"
BTN_VALUE[BTN_F] = "F"


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
        self._button_action = [lambda x: x for i in range(0, NUM_PADS)]
        self.update()
        time.sleep(1)
        self.clear()
        self.update()
        self.keyboard = Keyboard(usb_hid.devices)

        self._read_input_mode = False
        self._input_state = []
        self._read_input_callback = None

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

    def on_button_press(self, button_index, action):
        self._button_action[button_index] = action

    def execute_action(self, button_index):
        if self._read_input_mode:
            time.sleep(KEY_DELAY)
            if button_index != BTN_F and button_index != BTN_E:
                self._input_state.append(BTN_VALUE[button_index])
            elif button_index == BTN_F:
                self._input_state = []
                self._read_input_mode = False
            else:
                self._read_input_mode = False
                self._read_input_callback()
                self._input_state = []
        else:
            action = self._button_action[button_index]
            if action is not None:
                action(self, button_index)
    
    @property
    def input_state(self):
        return self._input_state

    @input_state.setter
    def input_state(self, value):
        self._input_state = value

    @property
    def read_input_mode(self):
        return self._read_input_mode

    def read_input(self, callback):
        self._read_input_mode = True
        [self.set_button_color(b, 0x20, 0x20, 0x20) for b in range(0, NUM_PADS + 1)]
        self.set_button_color(BTN_A, *DEFAULT_COLOR)
        self.set_button_color(BTN_B, *DEFAULT_COLOR)
        self.set_button_color(BTN_C, *DEFAULT_COLOR)
        self.set_button_color(BTN_D, *DEFAULT_COLOR)
        self.set_button_color(BTN_E, 0x0, 0x20, 0x0)
        self.set_button_color(BTN_F, 0x20, 0x0, 0x0)
        self._read_input_callback = callback

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

    def type(self, text: str):
        key_combo = parse(text)
        for keys in key_combo:
            self._press_and_release(keys)

    def _press_and_release(self, keys):
        for key in keys:
            self.keyboard.press(key)
            time.sleep(KEY_DELAY)
        for key in keys:
            self.keyboard.release(key)
        time.sleep(KEY_DELAY)

    @property
    def led_data_bytes(self) -> bytes:
        result = []
        for x in self._led_data:
            for y in x:
                result.append(y)
        return bytes(result)

def random_color():
    return [hex(random.randint(0,254)), hex(random.randint(0,254)), hex(random.randint(0,254))]


