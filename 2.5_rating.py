def rating(num):
    rating_list = [7, 5, 3, 3, 2, num]
    rating_list.sort(reverse=True)
    return rating_list


def main():
    num = int(input('Enter a your rating number: '))
    print(rating(num))


if __name__ == '__main__':
    main()
