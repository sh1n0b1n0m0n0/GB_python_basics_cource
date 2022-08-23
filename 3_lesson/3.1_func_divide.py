def divide(a, b):
    return (a / b) if b != 0 else 'zero division'


def main():
    a, b = int(input("Enter num: ")), int(input("Enter divider: "))
    print(divide(a, b))


if __name__ == '__main__':
    main()
