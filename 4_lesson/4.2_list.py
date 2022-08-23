def main():
    arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print([arr[i] for i in range(1, len(arr)-1) if arr[i-1] < arr[i]])


if __name__ == '__main__':
    main()
