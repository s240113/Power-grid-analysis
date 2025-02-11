import numpy as np

def generate_Derivatives(Ybus, V):
    """
    Calculates the derivatives of apparent power with respect to voltage magnitude and voltage angles.
    
    Parameters:
        Ybus (ndarray): Bus admittance matrix (N x N)
        V (ndarray): Complex bus voltage vector (N x 1)
    
    Returns:
        J_ds_dVm (ndarray): Derivatives of S with respect to voltage magnitude (N x N)
        J_ds_dTheta (ndarray): Derivatives of S with respect to voltage angles (N x N)
    """
    # Compute derivatives with respect to voltage magnitude
    J_ds_dVm = np.diag(V / np.absolute(V)).dot(np.diag((Ybus.dot(V)).conj())) + np.diag(V).dot(Ybus.dot(np.diag(V / np.absolute(V))).conj())
    
    # Compute derivatives with respect to voltage angles
    J_ds_dTheta = 1j * np.diag(V).dot((np.diag(Ybus.dot(V)) - Ybus.dot(np.diag(V))).conj())
    
    return J_ds_dVm, J_ds_dTheta
