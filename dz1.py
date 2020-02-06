from utils import readMatrixFromFile, copyMatrix
from findDeterminate import findDet

def reduceByIdentityMultipledByLambda(lambd, matrix):
    for i in range(len(matrix)):
        matrix[i][i] -= lambd
    
    return matrix

def getDirection(determinates):

    if (determinates['zero'] > 0):
        if (determinates['left'] < determinates['zero']):
            return 'left'
        else:
            return 'right'
    else:
        if (determinates['left'] > determinates['zero']):
            return 'left'
        else:
            return 'right'

A = readMatrixFromFile('input14_B.txt')

determinates = {
    'zero': findDet(copyMatrix(A)),
    'left': findDet(reduceByIdentityMultipledByLambda(-1, copyMatrix(A))),
    'right': findDet(reduceByIdentityMultipledByLambda(1, copyMatrix(A))),
}

direction = getDirection(determinates)
