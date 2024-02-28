import numpy as np

'''
Use this space to copy and paste functions you wrote in 
the last class.
'''

def is_stochastic(M: np.array) -> bool:
    '''
    Parameters
    ----------
    - M: numpy array
    
    Returns
    -------
    bool
    '''
    # Check if the matrix is square 0 --> row 1 --> column
    if M.shape[0] != M.shape[1]:
        return False
    # Check if all entries are non-negative
    if not np.all(M >= 0):
        return False
    # Check if the sum of each column is 1
    if not np.allclose(np.sum(M, axis=0), np.ones(M.shape[0])):
        return False
    # If all checks pass, the matrix is left stochastic
    return True

def stationary_states(P):
    """
    Parameters
    ----------
    P : np.array
    
    Returns
    -------
    list

    Find the stationary states of a stochastic matrix P.
    A stationary state is a row vector v such that vP = v.
    """
    # Find the eigenvalues and left eigenvectors of P
    eigenvalues, left_eigenvectors = np.linalg.eig(P.T)
    
    # Find the eigenvector corresponding to eigenvalue 1 (within a tolerance)
    stationary = []
    for i, eigenvalue in enumerate(eigenvalues):
        if np.isclose(eigenvalue, 1):
            # Normalize the eigenvector to have a sum of 1
            vec = left_eigenvectors[:, i].real / np.sum(left_eigenvectors[:, i].real)
            stationary.append(vec)
    
    return stationary

def probability_of_return(n: int) -> float:
    '''
    Parameters
    ----------
    n : int

    Returns
    -------
    float

    Calculate the probability that a random walk on a graph returns to the starting vertex after n steps.
    The graph is represented by a transition matrix where the entry (i, j) is the probability of moving from vertex i to vertex j.
    '''
    transition_matrix = np.full((4, 4), 1/3)
    np.fill_diagonal(transition_matrix, 0)
    probability_distribution = np.array([1, 0, 0, 0])

    # Iterate n times to calculate the probability distribution after n steps
    for _ in range(n):
        probability_distribution = np.dot(probability_distribution, transition_matrix)
    
    # The probability of return is the probability of the ant being at the starting vertex
    return probability_distribution[0]

def matrix_to_dict(M: np.array) -> dict:
    '''
    Parameters
    ----------
    M : numpy.ndarray
    
    Returns
    -------
    dict

    Convert a stochastic matrix M representing a Markov chain into a dictionary representation.
    The keys of the dictionary are the state numbers, and the values are lists of tuples
    (state number, transition probability).
    '''
    matrix_dict = {}
    for row_index, row in enumerate(M):
        # List of tuples (state number, transition probability)
        matrix_dict[row_index] = [(col_index, prob) for col_index, prob in enumerate(row) if prob > 0]
    return matrix_dict

print(matrix_to_dict([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(matrix_to_dict([[0,0.5], [1, 0.5]]))