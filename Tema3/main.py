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
    a, c, b = triang_matrix
    result_matrix = {}

    for i in matrix_dict.keys():
        for j in range(0, len(a)):

            aux_result = 0

            for k in matrix_dict[i].keys():

                factor = 0
                # aici practic implementez definitia din pdf. a_ij = a daca e pe diag principala, b daca e deasupra si c daca e sub; 0 in caz contrat
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


def triag_matrix_product(tr_matrix_and_sizes_1, tr_matrix_and_sizes_2):
    p1, q1, triang_matrix1 = tr_matrix_and_sizes_1
    a1, c1, b1 = triang_matrix1
    p2, q2, triang_matrix2 = tr_matrix_and_sizes_2
    a2, c2, b2 = triang_matrix2

    result_matrix = {}
    size = len(a1)
    if size != len(a2): return False

    for i in range(size):
        myA = a1[i]
        secondA = a2[i]
        aux_result = 0
        for j in {i - p1, i, i + q1}:
            if j >= 0:
                if j < size - 1:
                    myC = c1[j]
                else:
                    myC = 0
                if j < size - 1:
                    myB = b1[j]
                else:
                    myB = 0
                if i - j == q2 and j < size - q2:
                    secondB = b2[j]
                else:
                    secondB = 0
                if j - i == p2 and j < size - p2:
                    secondC = c2[i]
                else:
                    secondC = 0
                aux_result = myA * secondA + myB * secondB + myC * secondC
                if aux_result != 0 and 0 <= j < size:
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
    print(matrix_equality(my_product, mat_product, eps))

    print(triag_matrix_product((p, q, triang_matrix), (p, q, triang_matrix)))


def getEpsilon():
    u = 1
    aux = 0

    while u != 0 and 1 + u != 1:
        lastU = u
        u /= 10
        aux = aux + 1
    return lastU


if __name__ == "__main__":
    epsilon = getEpsilon()
    print(epsilon)
    # epsilon = float(sys.argv[1])
    main(epsilon)
