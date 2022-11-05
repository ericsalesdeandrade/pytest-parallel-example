from parallel_examples.core import odd_numbers, even_numbers, all_numbers

max_value_parameter = 500000000


def test_odd_numbers():
    result = odd_numbers(max_value=max_value_parameter)


def test_even_numbers():
    result = even_numbers(max_value=max_value_parameter)


def test_all_numbers():
    result = all_numbers(max_value=max_value_parameter)
