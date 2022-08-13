def main():
    new_arr = []
    ans = 0
    while True:
        arr = input("Enter nums: ")
        for i in arr.split():
            if i.lower() == 'n':
                print(sum(new_arr))
                ans = 'n'
                break
            else:
                new_arr.append(int(i))

        if ans == 'n':
            break

        print(sum(new_arr))

        ans = input("Do you want enter more nums? (y/n)")
        if ans.lower() == 'n':
            break


if __name__ == '__main__':
    main()
