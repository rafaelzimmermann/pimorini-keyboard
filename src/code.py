import time
from rainbow import Rainbow
from rgb_keyboard import RGBKeyboard, NUM_PADS
from config import key_action, DEFAULT_COLOR


class Keyboard:

    def __init__(self):
        self.keyboard = RGBKeyboard()
        self.rainbow = Rainbow(self.keyboard)
        self.rainbow.color_loop(DEFAULT_COLOR)
        self.color_state = [DEFAULT_COLOR for _ in range(0, NUM_PADS)]
        for i in range(0, 16):
            self.keyboard.on_button_press(i, key_action[i])

    def run(self):
        while True:
            state = self.button_states()
            if any(state):
                for i in range(0, NUM_PADS):
                    if state[i]:
                        self.keyboard.execute_action(i)

                self.keyboard.update()
            time.sleep(0.1)

    def button_states(self):
        state = []
        bin_state = self.keyboard.button_state
        for _ in range(0, NUM_PADS):
            state.append(bin_state & 0x01 > 0)
            bin_state >>= 1
        return state


if __name__ == '__main__':
    Keyboard().run()
