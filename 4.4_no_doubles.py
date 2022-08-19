def main():
    arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [i for i in arr if arr.count(i) == 1]
    print(result)


if __name__ == '__main__':
    main()
