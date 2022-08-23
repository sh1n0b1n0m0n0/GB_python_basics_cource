def main():
    str = input('Enter some words: ').split()
    for i in str:
        if len(i) <= 10:
            print(str.index(i)+1, i)
        else:
            print(str.index(i)+1, i[0:10])


if __name__ == '__main__':
    main()
