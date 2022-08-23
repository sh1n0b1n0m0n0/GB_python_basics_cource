def main():
    months = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
    month_num = int(input('Enter month number: '))
    if 0 < month_num <= 12:
        for name, number in months.items():
            if month_num in number:
                print(name)
    else:
        print('Use numbers from 1 to 12!')


if __name__ == '__main__':
    main()
