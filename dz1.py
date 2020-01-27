def read_m():
    f = open('input14_A.txt', 'r')
    s = f.read();
    f.close();
    a = s.split('\n');
    a = a[1:];
    for idx, val in enumerate(a):
        a[idx] = val.split(" ")

    for i, v in enumerate(a):
        for idx, item in enumerate(a[i]):
            a[i][idx] = int(item)

    return a

a = read_m();

def findMaxInColumn(column):
    max = a[0][column]
    max_row = 0
    for row in range(len(a)):
        if (a[row][column] > max):
            max = a[row][column]
            max_row = row
    return max_row

max = findMaxInColumn(0)

def swapLines(x, y):
    temp = a[x]; a[x] = a[y]; a[y] = temp
    return a;

a = swapLines(0, max)
print(a)