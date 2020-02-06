from utils import readMatrixFromFile, copyMatrix
from findDeterminate import findDet
from findRoot import findRoot

A = readMatrixFromFile('input14_A.txt')
print(findDet(copyMatrix(A)))

B = readMatrixFromFile('input14_B.txt')
print(findRoot(B))
