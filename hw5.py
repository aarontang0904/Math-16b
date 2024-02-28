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

def stationary_states(P: np.array) -> list:
    '''
    Parameters
    ----------
    - P: numpy array
    
    Returns
    -------
    list
    '''
    # Find the stationary states of the matrix
    # Initialize the list of stationary states
    stationary = []
    # Iterate through each row of the matrix
    for row in range(P.shape[0]):
        # If the row is equal to the dot product of the row and the identity matrix
        if np.allclose(P[row], np.dot(P, P[row])):
            # Add the row to the list of stationary states
            stationary.append(P[row])
    # Return the list of stationary states
    return stationary

def probability_of_return(n: int) -> float:
    transition_matrix = np.full((4, 4), 1/3)
    np.fill_diagonal(transition_matrix, 0)
    probability_distribution = np.array([1, 0, 0, 0])

    # Iterate n times to calculate the probability distribution after n steps
    for _ in range(n):
        probability_distribution = np.dot(probability_distribution, transition_matrix)
    
    # The probability of return is the probability of the ant being at the starting vertex
    return probability_distribution[0]

def matrix_to_dict(M):
    '''
    Convert a NumPy matrix M to a dictionary with row indices as keys and rows as lists.

    Parameters
    ----------
    M : numpy.ndarray
        A NumPy array representing the matrix.

    Returns
    -------
    dict
        A dictionary with keys as row indices and values as lists representing each row.
    '''
    matrix_dict = {row_index: row for row_index, row in enumerate(M)}
    return matrix_dict

