def main():
    try:
        arr = []
        while True:
            str = input("Enter data: ")
            if len(str) != 0:
                arr.append(str)
            else:
                break

        with open("5.1_ex.txt", "w", encoding='utf-8') as f:
            for elem in arr:
                f.write(f"{elem}\n")
    except IOError:
        print("IO Error my dude!")


if __name__ == "__main__":
    main()
