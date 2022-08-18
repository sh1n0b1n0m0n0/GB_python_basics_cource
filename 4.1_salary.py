from sys import argv


def salary(time, rate, bonus):
    return time * rate + bonus


def main():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Your salary: {salary(time, rate, bonus)}')
    except ValueError:
        raise SystemExit(f"Usage numbers!")


if __name__ == '__main__':
    main()
