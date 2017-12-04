"""
A python module containing 2 functions for calculating specific water vapor ratio
"""
import numpy as np

def q_sat(T,P):
    """
    Calculate specific ratio.
    
    PARAMETERS
    ----------
    T: float
            Air Temperature[K]
    P: float
            Air Pressure[Pa]
            
    Below refers to a Fortran code
    
    RETURNS
    ----------
    q_sat: float
        The specific water vapor ratio[kg/kg]
    """
    
    Ep = 0.61 

    es = np.exp(60.2227-6.8224e3/T-5.1393*np.log(T))
   
    q = Ep*es/(P-(1-Ep)*es)
    
    return q