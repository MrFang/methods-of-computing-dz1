def readMatrixFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read();
    a = s.split('\n');
    a = a[1:];
    for idx, val in enumerate(a):
        a[idx] = val.split(" ")

    for i, v in enumerate(a):
        for idx, item in enumerate(a[i]):
            a[i][idx] = int(item)

    return a

def copyMatrix(matrix):
    m = list()

    for idx, row in enumerate(matrix):
        m.append(list())
        for item in row:
            m[idx].append(item)
    
    return m