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
    'A': Key('A', (Keycode.A, Keycode.SHIFT,)),
    'a': Key('a', (Keycode.A,)),
    'B': Key('B', (Keycode.B, Keycode.SHIFT,)),
    'b': Key('b', (Keycode.B,)),
    'C': Key('C', (Keycode.C, Keycode.SHIFT,)),
    'c': Key('c', (Keycode.C,)),
    'D': Key('D', (Keycode.D, Keycode.SHIFT,)),
    'd': Key('d', (Keycode.D,)),
    'E': Key('E', (Keycode.E, Keycode.SHIFT,)),
    'e': Key('e', (Keycode.E,)),
    'F': Key('F', (Keycode.F, Keycode.SHIFT,)),
    'f': Key('f', (Keycode.F,)),
    'G': Key('G', (Keycode.G, Keycode.SHIFT,)),
    'g': Key('g', (Keycode.G,)),
    'H': Key('H', (Keycode.H, Keycode.SHIFT,)),
    'h': Key('h', (Keycode.H,)),
    'I': Key('I', (Keycode.I, Keycode.SHIFT,)),
    'i': Key('i', (Keycode.I,)),
    'J': Key('J', (Keycode.J, Keycode.SHIFT,)),
    'j': Key('j', (Keycode.J,)),
    'K': Key('K', (Keycode.K, Keycode.SHIFT,)),
    'k': Key('k', (Keycode.K,)),
    'L': Key('L', (Keycode.L, Keycode.SHIFT,)),
    'l': Key('l', (Keycode.L,)),
    'M': Key('M', (Keycode.M, Keycode.SHIFT,)),
    'm': Key('m', (Keycode.M,)),
    'N': Key('N', (Keycode.N, Keycode.SHIFT,)),
    'n': Key('n', (Keycode.N,)),
    'O': Key('O', (Keycode.O, Keycode.SHIFT,)),
    'o': Key('o', (Keycode.O,)),
    'P': Key('P', (Keycode.P, Keycode.SHIFT,)),
    'p': Key('p', (Keycode.P,)),
    'Q': Key('Q', (Keycode.Q, Keycode.SHIFT,)),
    'q': Key('q', (Keycode.Q,)),
    'R': Key('R', (Keycode.R, Keycode.SHIFT,)),
    'r': Key('r', (Keycode.R,)),
    'S': Key('S', (Keycode.S, Keycode.SHIFT,)),
    's': Key('s', (Keycode.S,)),
    'T': Key('T', (Keycode.T, Keycode.SHIFT,)),
    't': Key('t', (Keycode.T,)),
    'U': Key('U', (Keycode.U, Keycode.SHIFT,)),
    'u': Key('u', (Keycode.U,)),
    'V': Key('V', (Keycode.V, Keycode.SHIFT,)),
    'v': Key('v', (Keycode.V,)),
    'W': Key('W', (Keycode.W, Keycode.SHIFT,)),
    'w': Key('w', (Keycode.W,)),
    'X': Key('X', (Keycode.X, Keycode.SHIFT,)),
    'x': Key('x', (Keycode.X,)),
    'Y': Key('Y', (Keycode.Y, Keycode.SHIFT,)),
    'y': Key('y', (Keycode.Y,)),
    'Z': Key('Z', (Keycode.Z, Keycode.SHIFT,)),
    'z': Key('z', (Keycode.Z,)),
    ' ': Key(' ', (Keycode.SPACE,)),
    '1': Key('1', (Keycode.ONE,)),
    '!': Key('!', (Keycode.ONE, Keycode.SHIFT,)),
    '2': Key('2', (Keycode.TWO,)),
    '@': Key('@', (Keycode.TWO, Keycode.SHIFT,)),
    '3': Key('3', (Keycode.THREE,)),
    '#': Key('#', (Keycode.THREE, Keycode.SHIFT,)),
    '4': Key('4', (Keycode.FOUR,)),
    '$': Key('$', (Keycode.FOUR, Keycode.SHIFT,)),
    '5': Key('5', (Keycode.FIVE,)),
    '%': Key('%', (Keycode.FIVE, Keycode.SHIFT,)),
    '6': Key('6', (Keycode.SIX,)),
    '^': Key('^', (Keycode.SIX, Keycode.SHIFT,)),
    '7': Key('7', (Keycode.SEVEN,)),
    '&': Key('&', (Keycode.SEVEN, Keycode.SHIFT,)),
    '8': Key('8', (Keycode.EIGHT,)),
    '*': Key('*', (Keycode.EIGHT, Keycode.SHIFT,)),
    '9': Key('9', (Keycode.NINE,)),
    '(': Key('(', (Keycode.NINE, Keycode.SHIFT,)),
    '0': Key('0', (Keycode.ZERO,)),
    ')': Key(')', (Keycode.ZERO, Keycode.SHIFT,)),
}


def parse(value: str):
    result = []
    for c in value:
        if c in key_map:
            result.append(key_map[c])
    return result
