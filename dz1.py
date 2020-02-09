from utils import readMatrixFromFile, copyMatrix, printMatrix
from findDeterminate import findDet
from findRoot import findRoot,findRoot1

print('Task №1: ')
A = readMatrixFromFile('input14_A.txt')
printMatrix(A,'A')
print('Det A:',findDet(copyMatrix(A)),end = '\n\n')
B = readMatrixFromFile('input14_B.txt')
printMatrix(B,'B')
print('Det B:',findDet(copyMatrix(B)),end = '\n\n')
C = readMatrixFromFile('input14_C.txt')
printMatrix(C,'C')
print('Det C:',findDet(copyMatrix(C)),end = '\n\n')
print('Task №2: ')
findRoot(B,eps=float(input('Enter the epsilon: ')))

