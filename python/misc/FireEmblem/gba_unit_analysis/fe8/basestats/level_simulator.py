import pandas as pd
import numpy as np
import random 

bases_df = pd.read_csv('vanilla_bases.csv')
print(bases_df.head())
print(bases_df.dtypes)

growths_df = pd.read_csv('../growths/vanilla_growths.csv')
print(growths_df.head())
print(growths_df.dtypes)

def GetLevelUpRolls() -> list[int]: # Generate the level-up numbers
    level_up_rolls = []
    i = 0
    while i < 7:
        level_up_rolls.append(random.randint(0,99))
        i += 1
    return level_up_rolls

def StatIncreased(unit_growth: np.int64, level_up_roll: int) -> bool:
    return level_up_roll < unit_growth

def LevelUp(unit_data: pd.Series, unit_growths: pd.Series, max_level: int) -> pd.Series:
    print(unit_data)
    while unit_data['Lv '] < max_level: # trailing whitespace won't be stripped
        level_up_rolls = GetLevelUpRolls()
        i = 0
        while i < 7:
            if StatIncreased(unit_growths.iloc[i+1], level_up_rolls[i]):
                unit_data.iloc[i + 3] += 1
            i += 1
        unit_data['Lv '] += 1 # .strip(), .rstrip() wouldn't work
    return unit_data

'''
Main
'''
# Go unit by unit and level them up a prescribed number of times to a prescribed level
number_of_runs = 25
data_dir_base = "./data/"
max_level = 20

print(bases_df.columns)
print(bases_df['Name ']) # For some unknown reason, can't strip the trailing whitespace
names = bases_df['Name ']

base_dict = {} # Need to initialize char_df with labels
for label in bases_df.columns:
    base_dict[label] = []

ridx = 0
while ridx < len(names):
    char_df = pd.DataFrame(base_dict)
    data_file = data_dir_base + names.iloc[ridx] + ".csv"
    num_run = 0
    unit_data = bases_df.iloc[ridx]
    while num_run < number_of_runs:
        unit_data = LevelUp(unit_data, growths_df.iloc[ridx], max_level)
        char_df.loc[num_run] = unit_data
        unit_data = bases_df.iloc[ridx]
        num_run += 1
    char_df.to_csv(data_file, index=False)
    ridx += 1
