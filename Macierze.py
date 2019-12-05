import random
import numpy


# Dodawanie macierzy: C = A+B
def add_matrix():
    A = [[random.randint(1, 100)] * 8 for i in range(8)]
    B = [[random.randint(1, 100)] * 8 for i in range(8)]
    C = [[random.randint(1, 100)] * 8 for i in range(8)]

    for k in range(8):
        for j in range(8):
            A[k][j] = random.randint(1, 100)
    print(A)

    for k in range(8):
        for j in range(8):
            B[k][j] = random.randint(1, 100)
    print(B)

    for k in range(8):
        for j in range(8):
            C[k][j] = A[k][j]+B[k][j]
    print(C)



#Mnozenie macierzy

def createAndFillWithRandomValues(dim1, dim2):
    matrix = [[0] * dim1 for i in range(dim2)]
    for k in range(dim1):
        for j in range(dim2):
            matrix[k][j] = random.randint(-5, 5)
    return matrix


def matrixProduct(matrix1, matrix2):
    dims1 = numpy.shape(matrix1)
    dims2 = numpy.shape(matrix2)

    if dims1[1] != dims2[0]:
        raise Exception('Cannot perform multiplying! Wrong dimensions!')
    else:
        result = [[0] * max(dims1) for i in range(max(dims2))]
        for k in range(dims1[1]):
            for l in range(dims1[0]):
                for m in range(dims1[0]):
                    result[k][l] = result[k][l] + matrix1[k][m] * matrix2[m][l]
    return result

def multiply_matrix():
    a = createAndFillWithRandomValues(8, 8)
    print(a)
    b = createAndFillWithRandomValues(8, 8)
    print(b)
    c = matrixProduct(a, b)
    print(c)
    #result = numpy.matmul(a, b) #compare
    #print(result)


add_matrix()
multiply_matrix()

