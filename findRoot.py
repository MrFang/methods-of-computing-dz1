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

def findSecondLambda(direction, determinates, matrix):
    step = 1 if direction == 'right' else -1
    lambd = step

    while (determinates['zero'] * determinates[direction] > 0):
        lambd += step
        determinates[direction] = findDet(reduceByIdentityMultipledByLambda(lambd, copyMatrix(matrix)))

    return lambd

def findRoot(matrix, eps= 0.001):
    determinates = {
        'zero': findDet(copyMatrix(matrix)),
        'left': findDet(reduceByIdentityMultipledByLambda(-1, copyMatrix(matrix))),
        'right': findDet(reduceByIdentityMultipledByLambda(1, copyMatrix(matrix))),
    }
    
    direction = getDirection(determinates)
    segment = [0, findSecondLambda(direction, determinates, matrix)]

    while abs(segment[1]-segment[0])>2*eps :
        lambd = sum(segment)/2
        det = findDet(reduceByIdentityMultipledByLambda(lambd, copyMatrix(matrix)))
        det1 = determinates['zero']
        
        if det * det1 < 0:
            segment[1] = lambd
            determinates[direction] = det
        else:
            segment[0] = lambd
            determinates['zero'] = det
        
    root = sum(segment)/2
    
    print('Lamda = ',root)
    print('Det(B-l*E) = ',findDet(reduceByIdentityMultipledByLambda(root, copyMatrix(matrix))))
    
    return root