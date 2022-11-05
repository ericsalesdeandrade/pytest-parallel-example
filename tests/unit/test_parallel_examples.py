from parallel_examples.core import odd_numbers, even_numbers, all_numbers

size = 50000000


def test_odd_numbers() -> None:
    """
    Test to add Odd Numbers to a List
    :return: None
    """
    result = odd_numbers(size=size)


def test_even_numbers() -> None:
    """
    Test to add Even Numbers to a List
    :return: None
    """
    result = even_numbers(size=size)


def test_all_numbers():
    """
    Test to add All Numbers to a List
    :return: None
    """
    result = all_numbers(size=size)
