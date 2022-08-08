def main():
    num = int(input('Enter seconds: '))
    hours = num // 3600
    minutes = (num % 3600) // 60
    seconds = (num % 3600) % 60

    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')


if __name__ == '__main__':
    main()
