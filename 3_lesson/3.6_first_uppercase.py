def int_func(str):
    latin = 'abcdefghijklmnopqrstuvwxyz'

    if not set(str.lower()).difference(latin):
        return str.title()
    else:
        return False


def main():
    text = input("Enter latin words: ").split()

    for str in text:
        result = int_func(str)
        if result:
            print(result, end=" ")


if __name__ == '__main__':
    main()
