def readMatrixFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read();
    a = s.split('\n');
    a = a[1:];
    for idx, val in enumerate(a):
        a[idx] = val.split(" ")      
    
    a=[[int(elem) for elem in row]for row in a]

    return a

def copyMatrix(matrix):
    m = list()

    for idx, row in enumerate(matrix):
        m.append(list())
        for item in row:
            m[idx].append(item)
    
    return m

def printMatrix(matrix , st):
    print('Matrix ',st)
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))
    