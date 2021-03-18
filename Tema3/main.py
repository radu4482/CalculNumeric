import copy
import sys


def read_matrix(file_path):
    file = open(file_path, "r")
    matrix_dict = {}

    size = file.readline()

    for line in file:

        if line == "\n":
            continue

        matrix_elements = line.split()
        matrix_elements = list(map(lambda x: x.strip(","), matrix_elements))

        value = float(matrix_elements[0])
        i = int(matrix_elements[1])
        j = int(matrix_elements[2])

        if i not in matrix_dict.keys():
            matrix_dict[i] = {}
        if j not in matrix_dict[i].keys():
            matrix_dict[i][j] = value
        else:
            matrix_dict[i][j] += value

    file.close()

    return matrix_dict


def read_triang_matrix(file_path):
    file = open(file_path, "r")

    size = int(file.readline())
    p = int(file.readline())
    q = int(file.readline())

    a = [0 for i in range(size)]
    b = [0 for i in range(size - p)]
    c = [0 for i in range(size - q)]

    size_b = len(b)
    size_c = len(c)

    file.readline()
    for i in range(size):
        a[i] = float(file.readline())
    file.readline()
    for i in range(size_b):
        b[i] = float(file.readline())
    file.readline()
    for i in range(size_c):
        c[i] = float(file.readline())

    file.close()

    return p, q, [a, b, c]


def addition(sparse_matrix, triang_matrix):
    a, b, c = triang_matrix
    dict_matrix = copy.copy(sparse_matrix)

    if len(dict_matrix) != len(a):
        return [], "Dimensiunile matricilor nu coincid."

    for i in range(0, len(a)):
        if i not in dict_matrix[i].keys():
            dict_matrix[i][i] = a[i]
        else:
            dict_matrix[i][i] += a[i]

    for i in range(0, len(b)):
        if (i + 1) not in dict_matrix[i].keys():
            dict_matrix[i][i + 1] = b[i]
        else:
            dict_matrix[i][i + 1] += b[i]

    for i in range(1, len(c) + 1):
        if (i - 1) not in dict_matrix[i].keys():
            dict_matrix[i][(i - 1)] = c[i - 1]
        else:
            dict_matrix[i][(i - 1)] += c[i - 1]

    return dict_matrix


def matrix_equality(matrix_dict_1, matrix_dict_2, eps):
    if len(matrix_dict_1) != len(matrix_dict_2):
        return False

    for i in range(0, len(matrix_dict_1)):
        for j in range(0, len(matrix_dict_1[i])):
            if j not in matrix_dict_1[i].keys():
                continue
            if abs(matrix_dict_1[i][j] - matrix_dict_2[i][j]) > eps:
                return True

    return True


def matrix_product(matrix_dict, tr_matrix_and_sizes):
    p, q, triang_matrix = tr_matrix_and_sizes
    a, b, c = triang_matrix
    result_matrix = {}

    for i in matrix_dict.keys():
        for j in range(0, len(a)):

            aux_result = 0

            for k in matrix_dict[i].keys():

                factor = 0
                #aici practic implementez definitia din pdf. a_ij = a daca e pe diag principala, b daca e deasupra si c daca e sub; 0 in caz contrat
                if j == k:
                    factor = a[k]
                else:
                    if p == (k - j):
                        factor = c[j]
                    elif q == (j - k):
                        factor = b[k]

                aux_result += matrix_dict[i][k] * factor

            if aux_result != 0:
                if i not in result_matrix.keys():
                    result_matrix[i] = {}
                result_matrix[i][j] = aux_result

    return result_matrix


def main(eps):
    matrix_dict = read_matrix('a.txt')
    p, q, triang_matrix = read_triang_matrix('b.txt')
    addition_result = addition(matrix_dict, triang_matrix)
    addition_dict = read_matrix('aplusb.txt')

    print(matrix_equality(addition_result, addition_dict, eps))

    my_product = matrix_product(matrix_dict, (p, q, triang_matrix))
    mat_product = read_matrix('aorib.txt')
    # print(my_product)
    # print(mat_product)
    print(matrix_equality(my_product, mat_product, eps))


if __name__ == "__main__":
    epsilon = float(sys.argv[1])
    main(epsilon)
