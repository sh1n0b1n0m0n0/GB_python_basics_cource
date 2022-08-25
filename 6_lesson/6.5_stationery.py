class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Drawing with Pen - {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Drawing with Pencil - {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Drawing with Handle - {self.title}")


def main():
    pen = Pen("Lol")
    print(pen.title)
    pen.draw()

    pencil = Pencil("Kek")
    print(pencil.title)
    pencil.draw()

    handle = Handle("Cheburek")
    print(handle.title)
    handle.draw()


if __name__ == '__main__':
    main()
