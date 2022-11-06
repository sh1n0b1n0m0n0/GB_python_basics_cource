from typing import List


class Matrix:
    def __init__(self, matrix: List[List]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return "\n".join([str(" ".join([str(i) for i in row])) for row in self.matrix])

    def __add__(self, other):
        if (self.rows == other.rows) and (self.cols == other.cols):
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        else:
            return "Trying to add matrixes of varying rank!\n"


def main():
    A = [[31, 32], [37, 43], [51, 86]]
    B = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
    C = [[3, 5, 8, 3], [8, 3, 7, 1]]
    D = [[1, 2], [3, 4]]
    E = [[5, 6], [7, 8]]
    Err = [[5, 6], [7, 8], [1, 2]]

    matA = Matrix(A)
    matB = Matrix(B)
    matC = Matrix(C)
    matD = Matrix(D)
    matE = Matrix(E)
    matErr = Matrix(Err)

    print(matA, "\n")
    print(matB, "\n")
    print(matC, "\n")

    print("Addition: ")
    print(f"D + E")
    print(matD + matE, "\n")
    print(matD + matErr, "\n")


if __name__ == '__main__':
    main()
