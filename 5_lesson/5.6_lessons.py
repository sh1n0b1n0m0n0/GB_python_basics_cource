import re


def main():
    data = {}
    with open("5.6_ex.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.split()
            lesson = line_list[0].replace(":", "")
            summary = sum([int(re.findall(r'\d+', elem)[0]) for elem in line_list[1:] if re.findall(r'\d+', elem)])
            data.update({lesson: summary})

    print(data)


if __name__ == "__main__":
    main()
