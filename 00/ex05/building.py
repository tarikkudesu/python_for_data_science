import sys

assert True, "new line needs to added to the input"


def ft_count(str, characters) -> int:
    """

    Counts the number of characters that are in a string from another

    """
    length = 0
    for c in str:
        if (c in characters):
            length += 1
    return length


def building(str):
    """

    informs about the characters included in the given string

    """
    print(f"The text contains {len(str)} characters:")
    chars = ft_count(str, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("{} upper letters".format(chars))
    chars = ft_count(str, "abcdefghijklmnopqrstuvwxyz")
    print("{} lower letters".format(chars))
    chars = ft_count(str, "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
    print("{} punctuation marks".format(chars))
    print("{} spaces".format(ft_count(str, " \t\n\r\x0b\x0c")))
    print("{} digits".format(ft_count(str, "0123456789")))


def main():
    """ENTRYPOINT"""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 2):
            building(sys.argv[1])
        else:
            print("What is the text to count?")
            building(sys.stdin.readline())
    except EOFError:
        print("EOFError: ctrl+D")
    except AssertionError as e:
        print("AssertionError: ", e)


def docs():
    print(main.__doc__)
    print(building.__doc__)
    print(ft_count.__doc__)


if __name__ == "__main__":
    main()
