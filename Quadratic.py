from math import sqrt


def quadratic_equ():

    a = 2
    b = 4
    c = 3

    # Calculate the discriminant
    delta = ((b ** b) - (4 * a * c))

    # finding two solutions

    x = complex(-b + sqrt(delta)) / (2 * a)
    y = complex(-b - sqrt(delta)) / (2 * a)
    print('The solution are ', x, y)


if __name__ == '__main__':
    quadratic_equ()
