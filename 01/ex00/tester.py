from give_bmi import give_bmi, apply_limit


def main():
    """Entrypoint"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


def docs():
    """Display __doc__"""
    print(give_bmi.__doc__)
    print(apply_limit.__doc__)


if __name__ == "__main__":
    main()
