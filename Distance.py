import math


def distance(x, y):
    """

    :param x: inputting the x value
    :param y: inputting the y value
    :return:
    """
    x = float(input("Enter the X co-ordinate : "))
    y = float(input("Enter the Y co-ordinate : "))
    z = math.sqrt(x * x + y * y)
    print(z)
    print("The Euclidean Distance from origin ", x, " and ", y, "is ", z)


def main():
    distance(x="", y="")


if __name__ == '__main__':
    main()
