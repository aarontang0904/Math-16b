'''
Use this space to copy and paste functions you wrote in 
the last class. For example:
'''
def norm(v):
  return sum([i**2 for i in v])**0.5

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

# v1, v2 are linearly dependentif there is some a, b spans R such that a*v1+b*v2 = 0 for nonzero a, b
# v1 and v2 are colinear v1 is nonzero, there exists a scalar multiple of v1 that is equal to v2
def is_scalar_multiple(v1, v2):
  '''
  Parameters
  ----------
  - v1: list
  - v2: list

  Returns
  -------
  True if v1 and v2 are linearly dependent, and False otherwise
  '''
  # Check if either of them is the zero vector
  if norm(v1) == 0 or norm(v2) == 0:
    return True 
  # Find the first nonzero entry of v2
  for i,value in enumerate(v2):
    if value != 0:
      c = v1[i]/v2[i]
      break
  # Check c*v2 = v1
  return [i*c for i in v2] == v1

def count_vectors(vectors):
  '''
  Parameters
  ----------
  - vectors: a list of vectors (not necessarily of the same 
    dimension)

  Returns
  -------
  A dictionary whose keys are the vectors, and whose values 
  are the number of occurances of each vector. 

  For example:
  count_vectors([(1,0), (1,0), (2,3), (0,0), (0,)])
    = {(1,0) : 2, (2,3) : 1, (0,0): 1, (0,): 1}
  '''
  # First check if the list is empty
  if not vectors:
    return {}
  output = {} # Initialize the output dictionary
  for vector in vectors:
    if vector in output:
      output[vector] += 1
    else:
      output[vector] = 1
  return output


def reverse_dictionary(d):
  '''
  Parameters
  ----------
  - d: dictionary whose values are immutable

  Returns
  -------
  reversed dictionary, whose keys are the values of d, 
  and whose values are lists of keys of d.

  For example:
  reverse_dictionary({1 : a, 2: b, 3: b}) 
    ={a : 1, b: [2,3]}
  '''
  output = {}
  for key, value in d.items():
    if value in output:
      output[value].append(key)
    else:
      output[value] = [key]
  return output


def normalize(v):
  '''
  Parameters
  ----------
  - v: list representing a nonzero vector

  Returns
  -------
  - normalized_v: list

  Returns v/|v|
  '''
  return [i/norm(v) for i in v]

def orthogonal_projection(v, w):
  '''
  Parameters
  ----------
  - v: list
  - w: list (nonzero)

  Returns
  -------
  The orthogonal projection of v onto w. Returns 
  two vectors, x and y such that:
    1. v = x + y
    2. x is parallel to w
    3. y is perpendicular to w
  '''
  '''
  Formulas: 
    x = aw
    y = v - aw
    y*w = 0 = v*w - a*||w||^2
    a = v*w/||w||^2
  '''
  alpha = dot(v, w)/(norm(w)**2)
  x = [round(alpha * i, 1) for i in w]
  y = [i - j for i, j in zip(v,x)]
  return x, y


