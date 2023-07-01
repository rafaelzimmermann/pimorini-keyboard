import time
from rainbow import Rainbow
from rgb_keyboard import RGBKeyboard
from config import DEFAULT_COLOR, NUM_PADS
from passwd import PASS

def btn_0(k: RGBKeyboard, index: int):
    k.set_button_color(index, 0x20, 0, 0)
    k.update()
    k.type("btn 0")
    k.set_button_color(index, *DEFAULT_COLOR)

def btn_1(k: RGBKeyboard, index: int):
    import secret
    def type_password():
        encrypted_data = bytearray(PASS)
        password = "".join([str(x) for x in k.input_state])
        data = secret.decrypt(password, encrypted_data).decode()
        k.type(data)
        [k.set_button_color(b, *DEFAULT_COLOR) for b in range(0, NUM_PADS + 1)]

    k.read_input(type_password)


def no_action(k: RGBKeyboard, index: int):
    k.set_button_color(index, 0x20, 0, 0)
    k.update()
    k.type(str(index))
    k.set_button_color(index, *DEFAULT_COLOR)
    
    # k.set_button_color(index, *DEFAULT_COLOR)

key_action = [
    no_action,  # 3
    no_action,  # 7
    no_action,  # B
    no_action,  # F
    no_action,  # 2
    no_action,  # 6
    no_action,  # A
    no_action,  # E
    btn_1,  # 1
    no_action,  # 5
    no_action,  # 9
    no_action,  # D
    no_action,  # 0
    no_action,  # 4
    no_action,  # 8
    no_action,  # C
]

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
            try:
                state = self.button_states()
                if any(state):
                    for i in range(0, NUM_PADS):
                        if state[i]:
                            self.keyboard.execute_action(i)

                    self.keyboard.update()
                time.sleep(0.1)
            except Exception as e:
                self.keyboard.type(str(type(e)))
                self.keyboard.type("\n")
                self.keyboard.type(str(e))
                self.keyboard.type("\n")
                continue

    def button_states(self):
        state = []
        bin_state = self.keyboard.button_state
        for _ in range(0, NUM_PADS):
            state.append(bin_state & 0x01 > 0)
            bin_state >>= 1
        return state



if __name__ == '__main__':
    Keyboard().run()
