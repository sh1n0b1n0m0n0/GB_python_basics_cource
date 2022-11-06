class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.look = '*'

    def __str__(self):
        return str(f'Number of cell - {self.cell}')

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, n_cell_in_row):
        rows = self.cell // n_cell_in_row
        remainder = self.cell % n_cell_in_row
        cell_string = ''

        for i in range(rows):
            cell_string += self.look * n_cell_in_row + '\n'
        cell_string += self.look * remainder

        if remainder != 0:
            return cell_string
        else:
            return cell_string[:-1]


def main():
    cell_1 = Cell(5)
    cell_2 = Cell(11)
    cell_3 = Cell(12)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 / cell_2)
    print(cell_3 / cell_2)

    print(cell_1.make_order(3), '\n')
    print(cell_3.make_order(4), '\n')
    print(cell_2.make_order(3), '\n')
    print(cell_2.make_order(5))


if __name__ == '__main__':
    main()
