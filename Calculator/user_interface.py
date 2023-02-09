from excep import *
from mod_calc import *
from logg import logging

type_dict = {"1": "rational numbers", "2": "complex numbers"}
operations_dict = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "корень"}


def menu():
    print("\nДобро пожаловать в калькулятор!\n")
    while True:
        main_menu = input("Главное меню:"
                          "\n1 - Рациональные числа"
                          "\n2 - Комплексные числа"
                          "\n3 - Выход\n")
        match main_menu:
            case "1" | "2":
                menu_calc(main_menu)
            case "3":
                logging.info("The work of the calculator is completed.")
                print("Работа калкулятора завершена!")
                break
            case _:
                logging.error(
                    "An incorrect point in the main menu was selected.")
                print("Данного пункта нет в главном меню. Повторите попытку!")


def menu_calc(data_type):
    logging.info(f"The start of the calculator with {type_dict[data_type]}.")
    first, second = 0, 0
    result = "q"
    sign = "/"
    while True:
        menu_operations = input("Операции:"
                                "\n1 - Сложение"
                                "\n2 - Вычитание"
                                "\n3 - Умножение"
                                "\n4 - Деление"
                                "\n5 - Возведение в степень"
                                "\n6 - Нахождение корня"
                                "\n7 - Главное меню\n")

        if menu_operations.isdigit() and int(menu_operations) in range(1, 6):
            if data_type == "1":
                first, second = check_in_rational(
                    [input(f"Введите {i + 1} число: ") for i in range(2)], data_type)
            elif data_type == "2":
                first, second = [complex(*check_in_complex([input(f"Введите {i + 1} действительную часть => "),
                                                            input(f"Введите {i + 1} мнимую часть => ")], data_type, i))
                                 for i in range(2)]
        match menu_operations:
            case "1":
                result = sum_nums(first, second)
                logging.info(f"Sum => {first} + {second} = {result}")
            case "2":
                result = subtraction_nums(first, second)
                logging.info(f"Subtractionь => {first} - {second} = {result}")
            case "3":
                result = multiplication_nums(first, second)
                logging.info(
                    f"Multiplication => {first} * {second} = {result}")
            case "4":
                if data_type == "1":
                    second = check_zero_rational(str(second))
                    sign = menu_divisions()
                    operations_dict[menu_operations] = sign
                else:
                    second = check_zero_complex(first, second)
                    operations_dict[menu_operations] = "/"
                if sign:
                    result = division_nums(first, second, sign)
                    logging.info(
                        f"Division => {first} {sign} {second} = {result}")
            case "5":
                result = root_nums(first, second)
                logging.info(f"Root => {first} ^ {second} = {result}")
            case "6":
                second = ""
                if data_type == "1":
                    first = check_for_root_rational(
                        [input(f"Введите число => ")], data_type)
                else:
                    first = complex(*check_for_root_complex([input(f"Введите действительную часть => "),
                                                             input(f"Введите мнимую часть => ")], data_type))
                result = root_nums(first)
                logging.info(f"Root: {first} = {result}")
            case "7":
                logging.info('Transition to the main menu')
                print()
                break
            case _:
                logging.error(
                    f"An incorrect point in the operations menu has been introduced.")
                print("Данного пункта нет в меню ОПЕРАЦИЙ. Повторите попытку!")
                continue
        if result != "q":
            print(
                f"Результат => {first} {operations_dict[menu_operations]} {second} = {result}", end="\n\n")


def menu_divisions():
    logging.info(f"Start of the division menu.")
    while True:
        menu_division = input("Операции:\n"
                              "1 - '/'\n"
                              "2 - '//'\n"
                              "3 - '%'\n"
                              "4 - Предыдущее меню\n")
        match menu_division:
            case "1":
                return "/"
            case "2":
                return "//"
            case "3":
                return "%"
            case "4":
                logging.info('Stop division menu')
                print()
                return 0
            case _:
                logging.error(
                    f"An incorrect point in the division menu has been introduced.")
                print("Данного пункта нет в меню ДЕЛЕНИЯ. Повторите попытку!")
