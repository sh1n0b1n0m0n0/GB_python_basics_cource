def main():
    proceeds = int(input('Enter your proceeds: '))
    expenses = int(input('Enter your expenses: '))
    if proceeds > expenses:
        profit = proceeds - expenses
        print(f'Profit = {profit}$')
        # Return on Sales (ROS) = прибыль за отчётный период ÷ выручка × 100 %
        ros = (profit / proceeds) * 100
        print(f'Return on Sales = {ros:.2f}%')
        employees = int(input('Enter number of employees: '))
        # Чистая прибыль / на кол-во сотрудников
        profit_per_person = profit / employees
        print(f'Profit per Person = {profit_per_person:.2f}$')
    else:
        print('Loss')


if __name__ == '__main__':
    main()
