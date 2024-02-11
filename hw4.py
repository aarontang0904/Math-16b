import numpy as np
'''
Use this space to copy and paste functions you wrote in 
the last class.
'''
def dot(v1: list, v2: list) -> float:
  '''
  Parameters
  ----------
  - v1: list
  - v2: list

  Returns
  -------
  float

  Returns the dot product of v1 and v2
  '''
  return sum([i * j for i,j in zip(v1,v2)]) if len(v1) == len(v2) else None

def multiply(M: list[list], v: list) -> list:
  '''
  Parameters
  ----------
  - M: list of lists 
  - v: list

  Returns
  -------
  list
  Returns the vector Mv

  M and v are assumed to be with appropriate dimensions to get a valid Mv.
  '''
  return [dot(vector, v) for vector in M] 


def transpose(M: list[list]) -> list[list]:
  '''
  Parameters
  ----------
  - M: list of lists

  Returns
  -------
  list of lists corresponding to the transpose of M

  '''
  # output = []
  # for i in range(len(M)):   # This loop iterates through the rows of the matrix
  #   tmp = []
  #   for j in range(len(M[i])):    # This loop iterates every element in a row, can be interpreted as the column index
  #     tmp.append(M[j][i])         # tmp list represent the new row, which is the ith entry of j columns
  #   output.append(tmp)
  # return output
  return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def complex_mulitply(z1: tuple, z2: tuple) -> tuple:
  '''
  Parameters
  ----------
  - z1: tuple corresponding to the real and imaginary part of
    a complex number
  - z2: tuple corresponding to the real and imaginary part of
    a complex number

  Returns
  -------
  tuple corresponding to z1*z1
  
  '''
  M = [[z1[0], -z1[1]], [z1[1], z1[0]]]
  return tuple(multiply(M, list(z2)))


def rotate_matrix(M:list[list]) -> list:
  '''
  Parameters
  ----------
  - M: square matrix given as list of lists

  Returns
  -------
  M, but rotated 90 degrees counter-clockwise.
  '''
  # output = []
  # for i in range(len(M)):
  #   tmp = []
  #   for j in range(len(M)):
  #     tmp.append(M[j][len(M)-1-i])
  #   output.append(tmp)
  # return output
  return [[M[j][len(M)-1-i] for j in range(len(M))] for i in range(len(M))]

def is_positive_semidefinite(M: list[list]) -> bool:
  '''
  Parameters
  ----------
  - M: an arbitrary matrix

  Returns
  -------
  True if M is positive semi-definite, False otherwise

  '''
  if not is_symmetric(M):
    return False
  eigvals, _ = np.linalg.eig(np.array(M))
  return all(eigval >= 0 for eigval in eigvals)

def is_symmetric(M: list[list]) -> bool:
  '''
  Parameters
  ----------
  - M: an arbitrary matrix

  Returns
  -------
  True if M is symmetric, False otherwise

  Checks if M is equal to its transpose by comparing whether M[i][j] == M[j][i] for all i,j
  '''
  for i in range(len(M)):
    for j in range(i+1, len(M)):
      if M[i][j] != M[j][i]:
        return False
  return True
            