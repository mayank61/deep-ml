import numpy as  np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix=np.array(matrix)
	eigneValues,eigenVectors=np.linalg.eig(matrix)
	return eigneValues