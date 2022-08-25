class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self):
        print(f"{(self.__length * self.__width * 25 * 5) / 1000} t")


def main():
    road = Road(20, 5000)
    road.calculate_mass()


if __name__ == "__main__":
    main()
