 #!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        if (len(matrix[i]) == 0):
            print()
        for j in range(0, len(matrix[i])):
            if (j != len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=' ')
            elif (j == len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]))
