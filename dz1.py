from utils import readMatrixFromFile, copyMatrix
from findDeterminate import findDet

def reduceByIdentityMultipledByLambda(lambd, matrix):
    for i in range(len(matrix)):
        matrix[i][i] -= lambd
    
    return matrix

