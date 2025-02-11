import numpy as np

def calculate_F(Ybus, Sbus, V, pv_index, pq_index):
    """
    Calculates the mismatch vector F between specified and calculated values of P and Q.
    
    Parameters:
        Ybus (ndarray): Bus admittance matrix (N x N)
        Sbus (ndarray): Specified apparent power injection vector (N x 1)
        V (ndarray): Complex bus voltage vector (N x 1)
        pv_index (array-like): Indices of PV buses
        pq_index (array-like): Indices of PQ buses
    
    Returns:
        F (ndarray): Mismatch vector
    """
    # Compute the power mismatch
    Delta_S = Sbus - V * (Ybus.dot(V)).conj()
    
    # Extract real and imaginary parts (active and reactive power mismatches)
    Delta_P = Delta_S.real
    Delta_Q = Delta_S.imag
    
    # Construct mismatch vector F
    F = np.concatenate((Delta_P[pv_index], Delta_P[pq_index], Delta_Q[pq_index]), axis=0)
    
    return F
