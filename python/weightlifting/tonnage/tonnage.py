import pandas as pd

def anyBackoffSets(exercise_instance: pd.Series) -> bool, int:
    where = 0
    for labels, weight_or_reps in exercise_instance.items():
        if ':' in weight_or_reps:
            return True, where
        where += 1

    where = -1 # safe failure code
    return False, where

def anyEquipment(exercise_instance: pd.Series) -> bool, list[str]:
    # Check if the weight has 'KS', 'ES', 'WS', or some composite attached
        
