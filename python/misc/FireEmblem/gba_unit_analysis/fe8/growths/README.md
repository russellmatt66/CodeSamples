# Summary
`vanilla_growths.txt` is the substrate.

`vanilla_growths.csv` is output of `vgtxt_tocsv.py`

`sorted_vanilla_growths.csv` is output of `analyze_growths.py`

# Current Tasks
(1) Come up with efficient way of creating all G's
- `p_of_ngrowths_module.CreateGs`

# Run Instructions
`$ python3 vgtxt_tocsv.py`
`$ python3 analyze_growths.py`

# Directory Structure
`p_of_ngrowths-mod.py`
- Helper module for `p_of_n_growths.py` 
- Implements functions for calculating the probability that a given unit has 0, 1, 2, 3, ... growths upon level up

`p_of_n-test.py`
- Tests functions implemented in `p_of_ngrowths-mod.py`
