import numpy as np
import week2


def solve_matrix(filename):
    mat = np.matrix(week2.read_matrix(filename))
    A = np.matrix(mat[:, range(len(mat))])
    last_column = np.array(mat[:, len(mat)])
    return np.linalg.solve(A, last_column)


def roots(filename):
    mat = np.matrix(week2.read_matrix(filename))


#ENyYffaq

if "__main__" == __name__:
    print solve_matrix("matrix3")