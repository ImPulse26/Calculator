from typing import Union
from logg import logging


def check_in_rational(data: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(
            ".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        else:
            logging.error(
                f"An incorrect data entered: '{data[0]}', '{data[1]}'!")
            print(f"\nПовторите попытку!\n")
            data = [input(f"Введите {i + 1} число: ") for i in range(2)]


def check_in_complex(data: list, count: str, real_im=0):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(
            ".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        else:
            logging.error(
                f"An incorrect data entered: '{data[0]}', '{data[1]}'!")
            print(f"\nПовторите попытку!\n")
            match real_im:
                case 0:
                    data = [input(f"Введите 1 действительную часть => "), input(
                        f"Введите 1 мнимую часть => ")]
                case 1:
                    data = [input(f"Введите 2 действительную часть => "), input(
                        f"Введите 2 мнимую часть => ")]


def check_for_root_complex(data: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(
            ".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        print(f"\nПовторите попытку!\n")
        logging.error(
            f"An incorrect data entered: '{data[0]}', '{data[1]}'!")
        data = [input(f"Введите действительную часть => "),
                input(f"Введите мнимую часть => ")]


def check_for_root_rational(data: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(
            ".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 1:
            return check[0]
        print(f"\nПовторите попытку!\n")
        logging.error(f"An incorrect data entered: '{data[0]}'!")
        data = [input(f"Введите число => ")]


def check_zero_rational(data: str):
    while True:
        d = [float(i) if "." in i else int(i) for i in [data]
             if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not (d and d[0]):
            print(
                f"\nНа 0 делить нельзя! Повторите попытку!\n")
            logging.error(f"An incorrect data entered: '{data}'!")
            data = input(f"Введите второе число => ")
        else:
            return d[0]


def check_zero_complex(data_1: Union[int, float], data_2: Union[int, float]):
    while True:
        try:
            data_1 / data_2
        except ZeroDivisionError:
            print(
                f"\nДелить на ноль нельзя! Попторите попытку!\n")
            logging.error(f"An incorrect data entered: '{data_2}'!")
            data_2 = complex(
                *check_in_complex([input(f"Введите 2 действительную часть => "), input(f"Введите 2 минмую часть => ")], "2", 1))
        else:
            return data_2
