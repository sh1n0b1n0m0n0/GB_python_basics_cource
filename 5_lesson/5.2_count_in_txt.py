def main():
    ch = "s"
    with open("5.2_ex.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(f'Number of strings in file: {len(lines)}')
        for line in lines:
            counter = len(line.split())
            line = line.rstrip("\n")
            print(f'{counter} word{ch if counter > 1 else ""} in {line}')


if __name__ == "__main__":
    main()
