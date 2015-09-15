import numpy as np
import week2
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import newton

def solve_matrix(filename):
    mat = np.matrix(week2.read_matrix(filename))
    A = np.matrix(mat[:, range(len(mat))])
    last_column = np.array(mat[:, len(mat)])

    return np.linalg.solve(A, last_column)


def roots(filename):
    points = np.matrix(week2.read_matrix(filename))

    x = np.asarray(points[:, 0]).squeeze()
    y = np.asarray(points[:, 1]).squeeze()

    # calculate polynomial
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    # calculate new x's and y's
    #fx = np.linspace(x[0], x[-1], 50)
    #fy = f(fx)

    root = newton(f, 0)

    #print root
    #print f(root)
    #plt.plot(root, f(root), 'ro')
    #plt.plot(x, y, 'o', fx, fy)
    #plt.xlim([x[0] - 1, x[-1] + 1])
    #plt.show()

    return root


if "__main__" == __name__:
    print solve_matrix("matrix3")
    print roots('ENyYffaq.txt')