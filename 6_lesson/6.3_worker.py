class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.wage = wage
        self.bonus = bonus

    def get_full_name(self):
        print(f"Full name: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Total income: {self.wage + self.bonus}")


def main():
    position = Position("eke", "kek", "master_lomaster", 40, 30)

    print(position.position)
    print(position.bonus)
    print(position.wage)

    position.get_full_name()
    position.get_total_income()


if __name__ == '__main__':
    main()
