import sys
import pandas 

training_program = sys.argv[1]

lifts = []
volume = []

# There is a very specific structure to the training_program
with open(training_program, 'r') as input_file:
    for line in input_file:
        # PARSE MESOCYCLE SCHEDULE - NEED TO LEARN REGEX
        if line == 'START':
            break

    line = next(input_file, None)
    while line != 'END':
        if line == "":
            continue
        if line == "A:" or line == "B:" or line == "C:":
            pass # PLACEHOLDER - SEE BELOW
            # Put the lifts into `lifts`
            # Put the volume into `volume`
            # Use schedule for mesocycle to appropriately account for total volume

        line = next(input_file, None)
            