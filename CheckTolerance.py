import numpy as np
def CheckTolerance(F, n, err_tol):
    """
    Checks whether the greatest mismatch in the mismatch vector F is smaller than the specified tolerance.
    
    Parameters:
        F (ndarray): Mismatch vector
        n (int): Iteration counter
        err_tol (float): Specified error tolerance
    
    Returns:
        success (int): 1 if the greatest mismatch is smaller than err_tol, else 0
    """
    normF = np.linalg.norm(F, np.inf)  # Get the maximum absolute value in F
    print(f"Iteration {n}: Max mismatch = {normF}")
    
    return 1 if normF < err_tol else 0