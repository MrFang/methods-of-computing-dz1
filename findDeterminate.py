stack = list()

def findMaxInColumn(column, matrix):
    max = matrix[column][column]
    max_row = column
    for row in range(column, len(matrix)):
        if (matrix[row][column] > max):
            max = matrix[row][column]
            max_row = row
    return max_row

def swapLines(x, y, matrix):
    temp = matrix[x]; matrix[x] = matrix[y]; matrix[y] = temp

    return matrix;

def mult(num, row):
    r = list()
    for item in row:
        r.append(item * num)

    return r

def sum(row1, row2):
    result = list()
    for idx, item in enumerate(row1):
        result.append(row1[idx] + row2[idx])

    return result

def forwardPropagation(matrix):
    global stack

    for column in range(0, len(matrix)):

        max_row = findMaxInColumn(column, matrix)

        stack.append(-1)
        matrix = swapLines(column, max_row, matrix)

        stack.append(matrix[column][column])
        matrix[column] = mult(1/matrix[column][column], matrix[column]);

        for num in range(column + 1, len(matrix)):
            matrix[num] = sum(matrix[num], mult(-matrix[num][column], matrix[column]))

def backwardPropagation(matrix):
    for i in range(len(matrix)-1, 0, -1):
        for j in range(i-1, -1, -1):
            matrix[j] = sum(matrix[j], mult(-matrix[j][i], matrix[i]))

def findDet(matrix):
    forwardPropagation(matrix);
    backwardPropagation(matrix);

    global stack
    det = 1

    for i in reversed(stack):
        det*=i
    
    return det