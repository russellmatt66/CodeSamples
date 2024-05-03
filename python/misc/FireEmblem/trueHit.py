import random
import pandas as pd

def getTwoRandomInts(min_int: int, max_int: int)->tuple[int, int]:
    int_1 = random.randint(min_int, max_int)
    int_2 = random.randint(min_int, max_int)
    return (int_1, int_2)

def trueHit(nominal_hit_rate: int) -> float:
    # A 'miss' is when both hit_rolls are greater than the nominal rate
    num_samples = 10000
    num_hits = 0 # approximation of true hit to compare with analytical value
    
    for i in range(num_samples):
        roll_1, roll_2 = getTwoRandomInts(0,99)
        average_roll = (roll_1 + roll_2) / 2.0
        if average_roll < nominal_hit_rate: # hit
            num_hits += 1

    return float(num_hits) / float(num_samples)

nominal_hit_rates = range(101)
truehit_dict = {}
features = ['nominal_hit_rate', 'true_hit_rate']

for feature in features:
    truehit_dict[feature] = []

for nominal_hit_rate in nominal_hit_rates:
    true_hit = 100 * trueHit(nominal_hit_rate)
    truehit_dict['nominal_hit_rate'].append(nominal_hit_rate)
    truehit_dict['true_hit_rate'].append(true_hit)
    print(f"nominal hit rate of {nominal_hit_rate} = real hit of {true_hit}")

truehit_df = pd.DataFrame(truehit_dict)
truehit_df.to_csv('truehit.csv', index=False)
            
