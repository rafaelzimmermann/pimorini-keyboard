import time
from rgb_keyboard import RGBKeyboard, NUM_PADS

GREEN = [0x00, 0x20, 0x00]
ORANGE = [0x20, 0x20, 0x00]
RED = [0x20, 0x00, 0x00]
PURPLE = [0x20, 0x00, 0x20]
BLUE = [0x00, 0x00, 0x20]
BLUE_GREEN = [0x00, 0x20, 0x20]
COLOR_OFF = [0x05, 0x05, 0x05]


class Rainbow:

    def __init__(self, rgb_keyboard: RGBKeyboard):
        self.keyboard = rgb_keyboard

    def color_loop(self, color=ORANGE):
        for i in range(0, NUM_PADS):
            self.keyboard.set_button_color(i, *color)
            time.sleep(0.1)
            self.keyboard.update()

    def arrow_right(self, loop=1):
        o = ORANGE
        p = PURPLE
        empty = [o, o, o, o]
        states = [
            empty + empty + empty + empty,
            [o, p, p, o] + empty + empty + empty,
            [p, o, o, p] + [o, p, p, o] + empty + empty,
            empty + [p, o, o, p] + [o, p, p, o] + empty,
            empty + empty + [p, o, o, p] + [o, p, p, o],
            empty + empty + empty + [p, o, o, p],
            empty + empty + empty + empty
        ]
        for i in range(0, loop):
            for state in states:
                for j in range(0, NUM_PADS):
                    self.keyboard.set_button_color(j, *state[j])
                    time.sleep(0.1)
                    self.keyboard.update()
