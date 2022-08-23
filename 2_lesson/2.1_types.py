def main():
    types_list = [1, 2.1, "kek", False, None, (1, 2, 3), ["str_1", "str_2"], {0: 1, 1: 2}]
    check_types = [print(f'{i} -> {type(i)}') for i in types_list]


if __name__ == '__main__':
    main()
