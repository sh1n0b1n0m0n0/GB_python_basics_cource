def my_func(x, y):
    return x ** y


def my_func_v2(x, y):
    res = 1
    for i in range(1, -y + 1):
        res *= x

    return 1 / res


def main():
    x = float(input("Enter positive float number: "))
    y = int(input("Enter negative number: "))
    if y < 0:
        print(f"{my_func(x, y)}")
        print(f"{my_func_v2(x, y)}")
    else:
        print("Wrong input!")


if __name__ == '__main__':
    main()
