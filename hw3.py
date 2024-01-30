'''
Use this space to copy and paste functions you wrote in 
the last class. For example:
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

# solution starts here:
  return sum([i * j for i,j in zip(v1,v2,strict=True)]) if len(v1) == len(v2) else None

def is_scalar_multiple(v1, v2):
  '''
  Parameters
  ----------
  - v1: list
  - v2: list

  Returns
  -------
  True if v1 and v2 are lienarly independent, and False otherwise
  '''
  
  


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
  count_vectors([(1,0), (1,0), (2,3), (0,0), (0)])
    = {(1,0) : 2, (2,3) : 1, (0,0): 1, (0): 1}
  '''
  pass


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
  pass

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
  pass

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
  pass


