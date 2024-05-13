import pandas as pd
import numpy as np

def NumberOfMicrostates(n) -> int:
    # Just 7 choose n
    # 7 is the total number of stats
    # n is the number that increased upon a level up
    return int(np.math.factorial(7) / (np.math.factorial(n) * np.math.factorial(7 - n)))

def GrowthProduct(unit_growths: pd.Series, G: list[int]) -> np.float64:
    # G is the list of indices representing growths which did not increase
    gp = 1.0

    for ig in range(len(unit_growths)):
        if ig not in G:
            gp *= unit_growths.iloc[ig]

    return gp

def CreateGs(n: int, Nm: int) -> list[list[int]]:
    # list of the G's for a given n
    list_of_Gs = []

    n_did_not_increase = 7 - n # 7 is total number of stats

    # need to create all tuples representing the combinations of stats which did not increase
    temp_G = list(range(n_did_not_increase))
    print(temp_G)

    return list_of_Gs

def NGrowthProbability(n: int, unit_growths: pd.Series) -> np.float64:
    P_of_n = 0.0

    Nm = NumberOfMicrostates(n)
    list_of_Gs = CreateGs(Nm)
    i = 0
    while i < Nm:
        G = list_of_Gs[i]
        P_of_n += GrowthProduct(unit_growths, G)
        i += 1

    return P_of_n
