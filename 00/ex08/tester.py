from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    """Entrypoint"""
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


def docs():
    """Display __doc__"""
    print(main.__doc__)
    print(ft_tqdm.__doc__)


if __name__ == "__main__":
    main()
