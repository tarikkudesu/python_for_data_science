
def all_thing_is_obj(object: any) -> int:
    ret = str(type(object))
    if (ret == "<class 'set'>"):
        print(f"Set : {ret}")
    elif (ret == "<class 'dict'>"):
        print(f"Dict : {ret}")
    elif (ret == "<class 'tuple'>"):
        print(f"Tuple : {ret}")
    elif (ret == "<class 'list'>"):
        print(f"List : {ret}")
    elif (ret == "<class 'str'>"):
        print(f"{object} is in the kitchen : {ret}")
    elif (ret == "ret not found"):
        print(f"Set : {ret}")
    return 42
