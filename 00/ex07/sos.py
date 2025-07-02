import sys


def main():
    """

    The program takes a string as an argument and encodes it into Morse Code.

    """
    av = sys.argv
    ac = len(sys.argv)
    chars = 'abcdefghijklmnopqrstuvwxyz \
        ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..', ' ': '/',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }

    try:
        assert ac == 2
        assert len([c for c in av[1] if c in chars]) == len(av[1])
        for i, c in enumerate(av[1]):
            print(NESTED_MORSE.get(c.upper()), end="")
            if i != len(av[1]) - 1:
                print(' ', end="")
        print()
    except AssertionError:
        print("AssertionError: the arguments are bad")


def docs():
    """Display __doc__"""
    print(main.__doc__)


if __name__ == '__main__':
    main()
