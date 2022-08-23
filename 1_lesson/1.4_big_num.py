def main():
    n = int(input('Enter your num: '))
    maximum = n % 10
    n = n // 10

    while n > 0:
        temp = maximum
        maximum = n % 10
        n = n // 10
        if maximum < temp:
            maximum = temp

    print(maximum)


if __name__ == '__main__':
    main()
