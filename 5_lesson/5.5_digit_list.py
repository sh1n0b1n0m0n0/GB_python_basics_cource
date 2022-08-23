from random import randint


def main():
    with open("5.5_ex.txt", "w", encoding="utf-8") as f:
        lst = [randint(1, 100) for _ in range(100)]
        f.write(" ".join(map(str, lst)))

    with open("5.5_ex.txt", "r", encoding="utf-8") as f:
        print(sum(list(map(int, f.readline().split()))))


if __name__ == "__main__":
    main()
