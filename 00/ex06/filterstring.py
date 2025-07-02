import sys
from ft_filter import ft_filter


def main():
    """
    the program accepts two arguments: a string(S), \
        and an integer(N).
    The program outputs a list of words from S \
        that have a length greater than N.
    """

    chars = 'abcdefghijklmnopqrstuvwxyz \
        ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ac = len(sys.argv)
    av = sys.argv

    try:
        assert ac == 3
        assert av[2].isdigit()
        assert len([c for c in av[1] if c in chars]) == len(av[1])
        print(ft_filter(lambda ele: len(ele) > int(av[2]), av[1].split()))
    except AssertionError:
        print("AssertionError: the arguments are bad")


def docs():
    print(main.__doc__)
    print(ft_filter.__doc__)


if __name__ == '__main__':
    main()
