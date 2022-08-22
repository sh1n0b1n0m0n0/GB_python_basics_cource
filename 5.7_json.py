import json


def main():
    profit = {}
    with open("5.7_ex.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            firm = line.split()
            profit.update({firm[0]: int(firm[2]) - int(firm[3])})

    mean = sum([profit[num] for num in profit if profit[num] > 0])
    result = [profit, {"Mean profit": mean}]
    print(result)
    with open("5.7_ex.json", "w", ) as j:
        json.dump(result, j, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
