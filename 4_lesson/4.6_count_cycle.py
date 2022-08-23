from itertools import count, cycle


def main():
    my_count = count(3)
    my_cycle = cycle("KEK")
    for _ in range(8):
        print(next(my_count), next(my_cycle))


if __name__ == '__main__':
    main()
