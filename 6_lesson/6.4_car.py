from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car is moving.")

    def stop(self):
        print("Car stopped.")

    def turn(self):
        direction_list = ["Turn Left.", "Turn Right."]
        print(choice(direction_list))

    def show_speed(self):
        print(f'Speed: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'Speed: {self.speed}')
        else:
            print(f'Over speed limit!')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            print(f'Speed: {self.speed}')
        else:
            print(f'Over speed limit!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def main():
    town_car = TownCar(60, "red", "Reno", False)
    town_car.show_speed()
    town_car.go()
    town_car.stop()
    town_car.turn()
    print(town_car.color, town_car.name, town_car.is_police, "\n")

    police_car = PoliceCar(60, "white", "Chevrolet", True)
    police_car.show_speed()
    police_car.go()
    police_car.stop()
    police_car.turn()
    print(police_car.color, police_car.name, police_car.is_police, "\n")


if __name__ == '__main__':
    main()
