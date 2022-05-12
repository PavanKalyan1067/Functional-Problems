def array():
    """

    :return:
    """

    row = 3
    column = 3
    matrix = []
    print("Enter the entries row wise : ")
    for i in range(row):
        a = []
        for j in range(column):
            a.append(int(input()))
        matrix.append(a)
    print("The 2D array is given below : ")
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()


if __name__ == '__main__':
    array()
