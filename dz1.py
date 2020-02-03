from utils import readMatrixFromFile
from findDeterminate import findDet

a = readMatrixFromFile('input14_A.txt')
det = findDet(a)
print(a);

