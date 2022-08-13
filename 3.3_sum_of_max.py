def my_func(a, b, c):
    result = [a, b, c]
    result.sort()
    return sum(result[-2:])


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    print(my_func(a, b, c))


if __name__ == '__main__':
    main()
