def main():
    data = []
    with open("5.3_ex.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            employee = line.split()
            data_elem = {'employee': employee[0], 'salary': float(employee[1])}
            data.append(data_elem)

    print(f'Salary lower than 20000: {[elem["employee"] for elem in data if elem["salary"] < 20000]}')

    mean_salary = sum([elem["salary"] for elem in data]) / len(data)
    print(f"Mean salary: {mean_salary}")


if __name__ == "__main__":
    main()
