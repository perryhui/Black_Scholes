import numpy as np
import scipy.stats
import math 
# Importing math and scipy.stats package

def Black_Scholes_Call(S, K, R, T, Sigma):
    d_1 = (np.log(S/K) + (R+(Sigma)**2)T) / (Sigma*np.sqrt(T))