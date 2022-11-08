def odd_numbers(size: int) -> list:
    """
    Function to add Odd Numbers to a list
    :param size: Maximum value, Type - int
    :return: List
    """
    number_list = []
    [number_list.append(n) for n in range(0, size) if n % 2 != 0]
    return number_list


def even_numbers(size: int) -> list:
    """
    Function to add Even Numbers to a list
    :param size: Maximum value, Type - int
    :return: List
    """
    number_list = []
    [number_list.append(n) for n in range(0, size) if n % 2 == 0]
    return number_list


def all_numbers(size: str | int) -> list:
    """
    Function to add All Numbers to a list
    :param size: Maximum value, Type - int
    :return: List
    """
    number_list = []
    [number_list.append(n) for n in range(0, size)]
    return number_list
