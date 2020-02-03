from utils import readMatrixFromFile, copyMatrix
from findDeterminate import findDet

A = readMatrixFromFile('input14_A.txt')
mutableA = copyMatrix(A);
det = findDet(mutableA)
print(mutableA);
print(A);

