import numpy 

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    a=numpy.array(a)
    a=a.T
	return a