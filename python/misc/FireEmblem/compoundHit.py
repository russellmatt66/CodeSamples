import pandas as pd
import sys

# IS LYN GOING TO DIE

def compoundHitRate(nominal_hit_rates: list[int], truehit_df: pd.DataFrame) -> float:
    compound_hit_rate = 100.0

    for nominal_hit_rate in nominal_hit_rates:
        print(nominal_hit_rate)
        temp = truehit_df[truehit_df['nominal_hit_rate'] == nominal_hit_rate]
        val = temp['true_hit_rate'].iloc[0]
        print(temp['true_hit_rate'].iloc[0])
        compound_hit_rate *= val / 100
        # print(compound_hit_rate)

    # print(compound_hit_rate)

    return compound_hit_rate

truehit_df = pd.read_csv('truehit.csv')

nominal_hit_file = sys.argv[1]

def parseNominalHitFile(inputfile: str) -> list[int]:
    res = []
    with open(inputfile, 'r') as file:
        for line in file:
            res.append(int(line))

    return res

nominal_hit_rates = parseNominalHitFile(nominal_hit_file)

lyn_dying_chance = compoundHitRate(nominal_hit_rates, truehit_df)

print(f"Chance of Lyn dying is {lyn_dying_chance}")
