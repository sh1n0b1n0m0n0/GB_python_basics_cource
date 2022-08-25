from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 7}

    def running(self):
        for i in self.__color:
            print(i)
            sleep(self.__color[i])


def main():
    trl = TrafficLight()
    trl.running()


if __name__ == "__main__":
    main()
