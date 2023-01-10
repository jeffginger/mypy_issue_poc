from file1 import get_my_float_from_imported_package


def get_my_float() -> float:
    """Obtain a float from an imported function.

    Returns:
        a float obtained from an imported function
    """
    return get_my_float_from_imported_package()


if __name__ == "__main__":
    print("I am going to print a float")
    print(get_my_float())
