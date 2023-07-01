import collections
from adafruit_hid.keycode import Keycode


class Key:

    def __init__(self, char, code):
        self.char = char
        self.code = code

    def __getitem__(self, item):
        return self.code[item]

    def __repr__(self):
        return f"[{self.char}: {self.code}]"


key_map = {
    'A': Key('A', (Keycode.SHIFT, Keycode.A,)),
    'a': Key('a', (Keycode.A,)),
    'B': Key('B', (Keycode.SHIFT, Keycode.B,)),
    'b': Key('b', (Keycode.B,)),
    'C': Key('C', (Keycode.SHIFT, Keycode.C,)),
    'c': Key('c', (Keycode.C,)),
    'D': Key('D', (Keycode.SHIFT, Keycode.D,)),
    'd': Key('d', (Keycode.D,)),
    'E': Key('E', (Keycode.SHIFT, Keycode.E,)),
    'e': Key('e', (Keycode.E,)),
    'F': Key('F', (Keycode.SHIFT, Keycode.F,)),
    'f': Key('f', (Keycode.F,)),
    'G': Key('G', (Keycode.SHIFT, Keycode.G,)),
    'g': Key('g', (Keycode.G,)),
    'H': Key('H', (Keycode.SHIFT, Keycode.H,)),
    'h': Key('h', (Keycode.H,)),
    'I': Key('I', (Keycode.SHIFT, Keycode.I,)),
    'i': Key('i', (Keycode.I,)),
    'J': Key('J', (Keycode.SHIFT, Keycode.J,)),
    'j': Key('j', (Keycode.J,)),
    'K': Key('K', (Keycode.SHIFT, Keycode.K,)),
    'k': Key('k', (Keycode.K,)),
    'L': Key('L', (Keycode.SHIFT, Keycode.L,)),
    'l': Key('l', (Keycode.L,)),
    'M': Key('M', (Keycode.SHIFT, Keycode.M,)),
    'm': Key('m', (Keycode.M,)),
    'N': Key('N', (Keycode.SHIFT, Keycode.N,)),
    'n': Key('n', (Keycode.N,)),
    'O': Key('O', (Keycode.SHIFT, Keycode.O,)),
    'o': Key('o', (Keycode.O,)),
    'P': Key('P', (Keycode.SHIFT, Keycode.P,)),
    'p': Key('p', (Keycode.P,)),
    'Q': Key('Q', (Keycode.SHIFT, Keycode.Q,)),
    'q': Key('q', (Keycode.Q,)),
    'R': Key('R', (Keycode.SHIFT, Keycode.R,)),
    'r': Key('r', (Keycode.R,)),
    'S': Key('S', (Keycode.SHIFT, Keycode.S,)),
    's': Key('s', (Keycode.S,)),
    'T': Key('T', (Keycode.SHIFT, Keycode.T,)),
    't': Key('t', (Keycode.T,)),
    'U': Key('U', (Keycode.SHIFT, Keycode.U,)),
    'u': Key('u', (Keycode.U,)),
    'V': Key('V', (Keycode.SHIFT, Keycode.V,)),
    'v': Key('v', (Keycode.V,)),
    'W': Key('W', (Keycode.SHIFT, Keycode.W,)),
    'w': Key('w', (Keycode.W,)),
    'X': Key('X', (Keycode.SHIFT, Keycode.X,)),
    'x': Key('x', (Keycode.X,)),
    'Y': Key('Y', (Keycode.SHIFT, Keycode.Y,)),
    'y': Key('y', (Keycode.Y,)),
    'Z': Key('Z', (Keycode.SHIFT, Keycode.Z,)),
    'z': Key('z', (Keycode.Z,)),
    ' ': Key(' ', (Keycode.SPACE,)),
    '1': Key('1', (Keycode.ONE,)),
    '!': Key('!', (Keycode.SHIFT, Keycode.ONE,)),
    '2': Key('2', (Keycode.TWO,)),
    '@': Key('@', (Keycode.SHIFT, Keycode.TWO,)),
    '3': Key('3', (Keycode.THREE,)),
    '#': Key('#', (Keycode.SHIFT, Keycode.THREE,)),
    '4': Key('4', (Keycode.FOUR,)),
    '$': Key('$', (Keycode.SHIFT, Keycode.FOUR,)),
    '5': Key('5', (Keycode.FIVE,)),
    '%': Key('%', (Keycode.SHIFT, Keycode.FIVE,)),
    '6': Key('6', (Keycode.SIX,)),
    '^': Key('^', (Keycode.SHIFT, Keycode.SIX,)),
    '7': Key('7', (Keycode.SEVEN,)),
    '&': Key('&', (Keycode.SHIFT, Keycode.SEVEN,)),
    '8': Key('8', (Keycode.EIGHT,)),
    '*': Key('*', (Keycode.SHIFT, Keycode.EIGHT,)),
    '9': Key('9', (Keycode.NINE,)),
    '(': Key('(', (Keycode.SHIFT, Keycode.NINE,)),
    '0': Key('0', (Keycode.ZERO,)),
    ')': Key(')', (Keycode.SHIFT, Keycode.ZERO,)),
    '%': Key('%', (Keycode.SHIFT, Keycode.FIVE,)),
    '\n': Key('\n', (Keycode.ENTER,))
}


def parse(value: str):
    result = []
    scape_char = "\\"
    escape_enabled = False
    for c in value:
        if c in key_map:
            if c == scape_char:
                escape_enabled = True
                continue
            if escape_enabled:
                c = f"\{c}"
                escape_enabled = False
            result.append(key_map[c])
    return result
