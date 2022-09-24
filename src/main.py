import time
import picokeypad as keypad

NUM_PADS = keypad.get_num_pads()
COLORS = [
    [0x00, 0x20, 0x00],
    [0x20, 0x20, 0x00],
    [0x20, 0x00, 0x00],
    [0x20, 0x00, 0x20],
    [0x00, 0x00, 0x20],
    [0x00, 0x20, 0x20],
]
COLOR_OFF = [0x05, 0x05, 0x05]


class Keyboard:

    def __init__(self):
        keypad.init()
        keypad.set_brightness(1.0)
        self.color_state = [COLOR_OFF for _ in range(0, NUM_PADS)]
        for i in range(0, NUM_PADS):
            keypad.illuminate(*([i] + COLOR_OFF))
            keypad.update()

    def run(self):
        while True:
            state = self.button_states()
            if any(state):
                for i in range(0, NUM_PADS):
                    if state[i] and self.color_state[i] == COLOR_OFF:
                        self.lit(i, COLORS[i % 5])
                    else:
                        self.unlit(i)

            keypad.update()
            time.sleep(0.1)

    def button_states(self):
        state = []
        bin_state = keypad.get_button_states()
        for _ in range(0, NUM_PADS):
            state.append(bin_state & 0x01 > 0)
            bin_state >>= 1
        return state

    def lit(self, button, color):
        keypad.illuminate(*([button] + color))

    def unlit(self, button):
        keypad.illuminate(*([button] + COLOR_OFF))

    def unlit_all(self):
        for i in range(0, NUM_PADS):
            keypad.illuminate(*([i] + COLOR_OFF))
            keypad.update()


if __name__ == '__main__':
    Keyboard().run()