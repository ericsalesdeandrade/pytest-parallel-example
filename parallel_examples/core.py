
def odd_numbers(max_value: str | int):
    number_list = []
    for n in range(0, max_value):
        if n % 2 != 0:
            number_list.append(n)
    return number_list


def even_numbers(max_value: str | int):
    number_list = []
    for n in range(0, max_value):
        if n % 2 == 0:
            number_list.append(n)
    return number_list


def all_numbers(max_value: str | int):
    number_list = []
    for n in range(0, max_value):
        number_list.append(n)
    return number_list
