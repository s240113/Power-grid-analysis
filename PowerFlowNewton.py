import numpy  as np 
def PowerFlowNewton(Ybus,Sbus,V0,pv_index,pq_index,max_iter,err_tol):
    success= 0 # Initialization of flag, counter and voltage
    n = 0
    V = V0
    print('  iteration      maximum P & Q mismatch (pu)')
    print('  ---------      ---------------------------')
    # Determine mismatch between initial guess and and specified value for P and Q
    F = calculate_F(Ybus,Sbus,V,pv_index,pq_index)
    success = CheckTolerance(F,n,err_tol) # Check if the desired tolerance is reached
    while (not success) an d(n<max_iter):# Start Newton iterations
        # Update counter
        n += 1
        # Generate the Jacobian matrix
        J_dS_dVm,J_dS_dTheta=generate_Derivatives(Ybus,V)
        J=generate_Jacobian(J_dS_dVm,J_dS_dTheta,pv_index,pq_index)
        # Compute step
        dx=np.linalg.solve(J,F) 
        # Update voltages and check if tolerance is now reached
        V=Update_Voltages(dx,V,pv_index,pq_index)
        F=calculate_F(Ybus,Sbus,V,pv_index,pq_index)
        success=CheckTolerance(F,n,err_tol)
        if success: 
            print('The Newton Rapson Power Flow Converged in %d iterations!' % (n,))
        else:
            print('No Convergence!!\n Stopped after %d iterations without solution...' % (n,))

