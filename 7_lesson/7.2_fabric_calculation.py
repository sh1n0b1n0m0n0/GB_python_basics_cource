class Clothes:
    def __init__(self, parameter):
        self.parameter = parameter


class Coat(Clothes):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.v = parameter

    @property
    def calculate_expense(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, parameter):
        super().__init__(parameter)
        self.h = parameter

    @property
    def calculate_expense(self):
        return self.h * 2 + 0.3


def main():
    coat = Coat(52)
    suit = Suit(1.78)
    print(coat.calculate_expense)
    print(suit.calculate_expense)


if __name__ == '__main__':
    main()
