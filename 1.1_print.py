def main():
    num = 10
    string = 'kek'
    print(f'int: {num}, string: {string}\n')

    num = int(input('Enter some numbers: '))
    print(f'type: {type(num)}, num: {num}\n')

    string = input('Enter some words: ')
    print(f'type: {type(string)}, You say {string}')


if __name__ == '__main__':
    main()
