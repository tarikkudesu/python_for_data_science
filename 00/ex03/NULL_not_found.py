
def NULL_not_found(object: any) -> int:
    ret = str(type(object))
    if (ret == "<class 'NoneType'>"):
        print(f"Nothing: {object} {ret}")
    elif (ret == "<class 'bool'>" and not object):
        print(f"Fake: {object} {ret}")
    elif (ret == "<class 'int'>" and not object):
        print(f"Zero {object} {ret}")
    elif (ret == "<class 'str'>" and not object):
        print(f"Empty: {ret}")
    elif (ret == "<class 'float'>" and object != float('nan')):
        print(f"Cheese: {object} {ret}")
    else:
        print("Type not Found")
    return 1
