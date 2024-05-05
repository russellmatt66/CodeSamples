import pandas as pd
import re

# Maximum of five working sets
def anyBackoffSets(exercise_instance: pd.Series) -> bool, list[int]:
    where = []
    idx = 0
    backoff_truth = False
    for labels, weight_or_reps in exercise_instance.items():
        if ':' in weight_or_reps:
            backoff_truth = True 
            where.append(idx)
        idx += 1

    return backoff_truth, where

def parseWorkingWeight(string):
    # Match numeric characters
    numeric_part = re.match(r'\d+', string).group(0)
    # Match non-numeric characters
    nonnumeric_part = re.sub(r'\d+', '', string)

    return numeric_part, nonnumeric_part

def anyEquipment(exercise_instance: pd.Series) -> bool, list[int] list[str]:
    # Check if the working weight has 'KS', 'ES', 'WS', or some composite form, attached which indicates the usage of sleeves, wrist straps/wraps, or a combination
    # Also checks if equipment was used during backoff sets
    equipment_truth = False
    equipment_kinds = []
    
    working_weight_string = exercise_instance.loc[exercise_instance['WEIGHT (LBS)']]
    
    # Use regex to seperate out the equipment kinds 
    working_weight, equipment_kinds = parseWorkingWeight(working_weight_string)

    any_backoff_sets, bidcs = anyBackoffSets(exercise_instance)
    for bidx in bidcs:
        backoff_string = exercise_instance.iloc[bidx]

        # Use string methods to seperate out backoff weight from string

        backoff_weight = 
