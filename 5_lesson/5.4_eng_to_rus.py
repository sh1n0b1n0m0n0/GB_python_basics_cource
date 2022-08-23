def main():
    digits = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'zero': 'ноль'}

    with open("5.4_ex_old.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open("5.4_ex_new.txt", "w", encoding="utf-8") as f:
        for line in lines:
            line = line.lower()
            number = line.split()[0]
            if number in digits.keys():
                new_line = line.replace(number, digits[number].title())

                f.write(new_line)
    print("Complete.")


if __name__ == "__main__":
    main()
