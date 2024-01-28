from math import sqrt
import numpy as np

vectors = np.random.rand(100000,10).tolist()

def is_in_first_quadrant(vector: list) -> bool:
  '''
  Parameters
  ----------
  - vector: length 2 list

  Returns
  -------
  Boolean

  Returns True when vector is in the first quadrant (ie, 
  all of its entries are non-negative). Returns 
  False otherwise.
  '''
  # for n  in vector:
  #   if n < 0:
  #     return False
  # return True

  # Written in one line
  return all(n >= 0 for n in vector)

# print(is_in_first_quadrant([1, 2]))
# print(is_in_first_quadrant([1, -2]))

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
  # sum = 0
  # for i in range(len(v1)):
  #   sum += v1[i]*v2[i]
  # return sum

  # Written in one line
  # return sum(v1[i]*v2[i] for i in range(len(v1)))
  return sum([i * j for i,j in zip(v1,v2,strict=True)]) if len(v1) == len(v2) else None

# print(dot(v1=[1,2,3], v2=[1,2,3]))

def norm(v: list) -> float:
  '''
  Parameters
  ----------
  - v: list

  Returns
  -------
  float

  Returns the Euclidean norm of v
  '''
  # sum = 0
  # for i in range(len(v)):
  #   sum += v[i]**2
  # return sqrt(sum)

  # Written in one line
  return sqrt(sum([n**2 for n in v]))

def largest_norm(vectors: list[list]) -> list:
  '''
  Parameters
  ----------
  - vectors: list of lists

  Returns
  -------
  - v: vector

  Returns the vector v which has the largest norm 
  of all the vectors in 'vectors'. In case of a tie, returns 
  the first vector in the list.
  '''
  largest_norm = norm(vectors[0])
  largest_v = list[0]
  for vector in vectors[1:]:
    if norm(vector) > largest_norm:
      largest_norm = norm(vector)
      largest_v = vector
  return largest_v

  # Written in one line
  # return max(vectors, key=norm)
  # return max(vectors,key=lambda v:sqrt(sum(n**2 for n in v)))

print(largest_norm(vectors))

def second_largest_norm(vectors: list[list]) -> list:
  '''
  Parameters
  ----------
  - vectors: list of lists

  Returns
  -------
  - v: vector

  Returns the vector v which has the largest norm 
  of all the vectors in 'vectors'. In case of a tie, returns 
  the first vector in the list.
  '''
  # if len(vectors)<2:
  #   return None
  
  # largestNorm = norm(vectors[0])
  # secondLargestNorm = norm(vectors[1])

  # if secondLargestNorm > largestNorm:
  #   tmp = secondLargestNorm
  #   secondLargestNorm = largestNorm
  #   largestNorm = tmp

  # for vector in vectors[2:]:
  #   if norm(vector)>largestNorm:
  #     tmpNorm = largestNorm
  #     largestNorm = norm(vector)
  #     secondLargestNorm = tmpNorm
  #   elif norm(vector)>secondLargestNorm:
  #     secondLargestNorm = norm(vector)

  # for vector in vectors:
  #   if norm(vector)==secondLargestNorm:
  #     return vector
  
  return sorted(vectors, key=norm, reverse=True)[1] if len(vectors) >= 2 else None
  
print(second_largest_norm(vectors))
  
def square_root(n:int, eps:float) -> float:
  '''
  Parameters
  ----------
  - n: int
  - eps: float

  Returns
  -------
  float
  
  Returns the square root of n within an error of eps.
  '''
  x = 1
  while abs(x**2-n) >= eps:
      x = (x+n/x)*0.5
  return x

# print(square_root(100,0.000001))