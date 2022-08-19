from functools import reduce


def multiply(a, b):
    return a * b


def main():
    arr = [i for i in range(100, 1001) if i % 2 == 0]
    res = reduce(multiply, arr)
    print(res)


if __name__ == '__main__':
    main()
