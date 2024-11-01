import pandas as pd
import numpy as np

def NumberOfMicrostates(n) -> int:
    # Just 7 choose n
    # 7 is the total number of stats
    # n is the number that increased upon a level up
    return np.factorial(7) / (np.factorial(n) * np.factorial(7 - n))

def GrowthProduct(unit_growths: pd.Series, G: list[int]) -> np.float64:
    # G is the list of indices representing growths which did not increase
    gp = 1.0

    for ig in range(len(unit_growths)):
        if ig not in G:
            gp *= unit_growths.iloc[ig]

    return gp

def NGrowthProbability(n: int, unit_growths: pd.Series) -> np.float64:
    P_of_n = 0.0

    Nm = NumberOfMicrostates(n)
    i = 0
    while i < Nm:
        G = GetG()
        P_of_n += GrowthProduct(unit_growths, G)

    return P_of_n
