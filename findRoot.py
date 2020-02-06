from utils import copyMatrix
from findDeterminate import findDet

def reduceByIdentityMultipledByLambda(lambd, matrix):
    for i in range(len(matrix)):
        matrix[i][i] -= lambd
    
    return matrix

def getDirection(determinates):

    if (determinates['zero'] > 0):
        return 'left' if determinates['left'] < determinates['zero'] else 'right'
    else:
        return 'left' if determinates['left'] > determinates['zero'] else 'right'

def findSecondLambda(direction, determinates):
    step = 1 if direction == 'right' else -1
    lambd = step

    while (determinates['zero'] * determinates[direction] > 0):
        lambd += step
        determinates[direction] = findDet(reduceByIdentityMultipledByLambda(lambd, copyMatrix(A)))

    return lambd

def findRoot(matrix):
    determinates = {
        'zero': findDet(copyMatrix(matrix)),
        'left': findDet(reduceByIdentityMultipledByLambda(-1, copyMatrix(matrix))),
        'right': findDet(reduceByIdentityMultipledByLambda(1, copyMatrix(matrix))),
    }

    direction = getDirection(determinates)
    segment = [0, findSecondLambda(direction, determinates)]

    while (abs(determinates['zero']) > 0.001 and abs(determinates[direction]) > 0.0001):
        lambd = (segment[0] + segment[1]) * 0.5
        det = findDet(reduceByIdentityMultipledByLambda(lambd, copyMatrix(matrix)))
        
        if (det * determinates['zero'] > 0):
            segment[0] = lambd
            determinates['zero'] = det
        else:
            segment[1] = lambd
            determinates[direction] = det

    return segment