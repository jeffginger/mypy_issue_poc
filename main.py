from file1 import get_my_float_from_imported_package


def get_my_float(mybool: bool) -> float:
    """Obtain a float from an imported function.

    Returns:
        a float obtained from an imported function somewhere else.
    """
    if mybool:
        return get_my_float_from_imported_package()
    else:
        return 0.0


if __name__ == "__main__":
    print("I am going to print a float")
    print("I've changed the script")
    print(get_my_float(True))
