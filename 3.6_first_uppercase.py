def int_func(str):
    return str.title()


def main():
    text = input("Enter latin words: ")

    print(int_func(text.lower()))


if __name__ == '__main__':
    main()