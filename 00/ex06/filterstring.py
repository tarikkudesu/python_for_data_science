import sys
from ft_filter import ft_filter


def main():
    """
    the program accepts two arguments: a string(S), \
        and an integer(N).
    The program outputs a list of words from S \
        that have a length greater than N.
    """

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEF \
        GHIJKLMNOPQRSTUVWXYZ0123456789'
    ac = len(sys.argv)
    av = sys.argv

    try:
        assert ac == 3, "the arguments are bad"
        assert av[2].isdigit(), "the arguments are bad"
        assert len([c for c in av[1] if c in chars]) == len(av[1]), \
            "the arguments are bad"
        print(ft_filter(lambda ele: len(ele) > int(av[2]), av[1].split()))
    except AssertionError as e:
        print("AssertionError: ", e)


if __name__ == '__main__':
    main()
