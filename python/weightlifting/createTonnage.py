import pandas as pd
import sys
'''
HELPER FUNCTIONS
'''
# WIP
# calculate the tonnages for a given exercise
# return a dict that can be used to concat together a `.csv` of the tonnages
def computeTonnage(training_lifts: pd.Series, training_days: pd.Series) -> dict:
    tonnage = {}
    # for each training_day, calculate the tonnage for the lifts in the training_lifts
    # training_day is the key, tonnage is the value
    return tonnage
'''
MAIN CODE
'''
path_to_lifting_numbers = sys.argv[1] # raw data

lift_df = pd.read_csv(path_to_lifting_numbers) 

# 

# Find the indices that correspond to training days
# Store these training days
# For a given lift, compute the tonnage on a given training day
# Create tonnage df / concat this to tonnage df 