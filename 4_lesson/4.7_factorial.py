def fact(n):
    first_n = 1
    for i in range(n + 1):
        yield f'{i}! = {first_n}'
        first_n *= i + 1


def main():
    n = int(input("Enter a number: "))
    for el in fact(n):
        print(el)


if __name__ == '__main__':
    main()
