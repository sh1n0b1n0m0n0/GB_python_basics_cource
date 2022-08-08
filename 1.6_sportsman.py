def main():
    a = int(input('Enter number of km in first day: '))
    b = int(input('Enter how much you want to reach: '))
    day = 1
    while a < b:
        a = a + a * 0.1
        day += 1

    print(day)


if __name__ == '__main__':
    main()
