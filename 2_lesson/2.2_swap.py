def first_second_swap(arr):
    if len(arr) <= 1:
        return arr

    elif len(arr) % 2 == 0:
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        for i in range(0, len(arr)-2, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


def main():
    # arr = [2, 1, 4, 3, 6, 5]
    # arr = [2, 1, 4, 3, 6, 5, 7]
    arr = [item for item in input("Enter the list items: ").split()]

    print(first_second_swap(arr))


if __name__ == '__main__':
    main()
