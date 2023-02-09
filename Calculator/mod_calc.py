def sum_nums(num_1, num_2):
    return num_1 + num_2


def subtraction_nums(num_1, num_2):
    return num_1 - num_2


def multiplication_nums(num_1, num_2):
    return num_1 * num_2


def division_nums(num_1, num_2, par="/"):
    if par == "%":
        return round(num_1 % num_2, 2)
    elif par == "//":
        return num_1 // num_2
    return num_1 / num_2


def root_nums(num_1, num_2=None):
    if not num_2:
        return num_1 ** 0.5
    return num_1 ** num_2
