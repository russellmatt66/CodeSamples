import pandas as pd
import sys
import os
'''
HELPER FUNCTIONS
'''
# WIP
# calculate the tonnages for a given exercise
def computeTonnage(working_sets: str) -> float:
    tonnage = 0.0
    # Assumption: 'working_sets' looks like WW R1/R2/.../Rn;
    # For example: 255 5/5/5/;
    # Example represents a set of 255 lbs performed for 3 sets of 5
    working_split = working_sets.split('')
    working_weight = float(working_split[0])
    working_reps = working_split[1].split('/')
    num_sets = len(working_reps) - 1 # -1 from ';'
    for ir in range(num_sets):
        tonnage += working_weight * working_reps[ir] 
    return tonnage

# return a dict that can be used to concat together a `.csv` of the tonnages
def parseLiftingData(lifting_df: pd.DataFrame) -> dict:
    tonnage_dict = {} # training date is the key, tonnage is the value
     
    # for each training_day, calculate the tonnage for the lifts in the training_lifts
    
    return tonnage_dict
'''
MAIN CODE
'''
path_to_lifting_numbers = sys.argv[1] # raw data

lifting_data_list = os.listdir(path_to_lifting_numbers)

for lifting_data in lifting_data_list:
    ld_df = pd.read_csv(path_to_lifting_numbers + lifting_data)
    tonnage_record = parseLiftingData(ld_df) 

# Not sure what this is saying
# Find the indices that correspond to training days
# Store these training days
# For a given lift, compute the tonnage on a given training day
# Create tonnage df / concat this to tonnage df 
