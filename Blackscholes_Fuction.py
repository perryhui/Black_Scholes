import numpy as np
from scipy.stats import norm

def Real_Risk(N_Risk, I_Rate):
    R_Risk = (1 + N_Risk) / (1 + I_Rate)
    return R_Risk
R = Real_Risk()

N = norm.cdf
def Black_Scholes_Call(S, K, R, T, Sigma):
    d_1 = (np.log(S / K) + (R + (Sigma)**2 / 2) * T) / (Sigma * np.sqrt(T))
    d_2 = d_1 - (Sigma * np.sqrt(T))
    return S * N(d_1) - N(d_2) * K * np.exp(- R * T)

def Black_Scholes_Put(S, K, R, T, Sigma):
    d_1 = (np.log(S / K) + (R + (Sigma)**2 / 2) * T) / (Sigma * np.sqrt(T))
    d_2 = d_1 - (Sigma * np.sqrt(T))
    return N(- d_2)* K * np.exp(-R * T) - N(- d_1) * S