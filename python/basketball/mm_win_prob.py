import numpy as np

# 2024
win_probabilities = np.zeros((16, 16)) # (i, j) corresponds to probability that "i+1"th seed beats "j+1"th seed

# https://mcubed.net/ncaab/seeds.shtml
# 1 seed
win_probabilities[0,0] = 0.5
win_probabilities(0,1) = 0.545
win_probabilities(0,2) = 0.634
win_probabilities(0,3) = 0.705
win_probabilities(0,4) = 0.797
win_probabilities(0,5) = 0.706
win_probabilities(0,6) = 0.857
win_probabilities(0,7) = 0.785
win_probabilities(0,8) = 0.906
win_probabilities(0,9) = 0.875
win_probabilities(0,10) = 0.556
win_probabilities(0,11) = 1.0
win_probabilities(0,12) = 1.0
win_probabilities(0,13) = 0.0
win_probabilities(0,14) = 0.0
win_probabilities(0,15) = 0.987

# 2 seed
win_probabilities(1,0) = 0.455
win_probabilities(1,1) = 0.5
win_probabilities(1,2) = 0.606
win_probabilities(1,3) = 0.5
win_probabilities(1,4) = 0.25
win_probabilities(1,5) = 0.722
win_probabilities(1,6) = 0.696
win_probabilities(1,7) = 0.4
win_probabilities(1,8) = 0.667
win_probabilities(1,9) = 0.641
win_probabilities(1,10) = 0.842
win_probabilities(1,11) = 1.0
win_probabilities(1,12) = 0.0
win_probabilities(1,13) = 0.0
win_probabilities(1,14) = 0.928
win_probabilities(1,15) = 0.0

# 3 seed
win_probabilities(2,0) = 0.366
win_probabilities(2,1) = 0.394
win_probabilities(2,2) = 0.5
win_probabilities(2,3) = 0.556
win_probabilities(2,4) = 0.5
win_probabilities(2,5) = 0.583
win_probabilities(2,6) = 0.632
win_probabilities(2,7) = 1.0
win_probabilities(2,8) = 0.75
win_probabilities(2,9) = 0.692
win_probabilities(2,10) = 0.667
win_probabilities(2,11) = 0.0
win_probabilities(2,12) = 0.0
win_probabilities(2,13) = 0.855
win_probabilities(2,14) = 0.667
win_probabilities(2,15) = 0.0

# 4 seed
win_probabilities(3,0) = 0.295
win_probabilities(3,1) = 0.5
win_probabilities(3,2) = 0.444
win_probabilities(3,3) = 0.5
win_probabilities(3,4) = 0.573
win_probabilities(3,5) = 0.333
win_probabilities(3,6) = 0.333
win_probabilities(3,7) = 0.385
win_probabilities(3,8) = 0.4
win_probabilities(3,9) = 1.0
win_probabilities(3,10) = 0.0
win_probabilities(3,11) = 0.705
win_probabilities(3,12) = 0.789
win_probabilities(3,13) = 0.0
win_probabilities(3,14) = 0.0
win_probabilities(3,15) = 0.0

# 5 seed
win_probabilities(4,0) = 0.203
win_probabilities(4,1) = 0.75
win_probabilities(4,2) = 0.5
win_probabilities(4,3) = 0.427
win_probabilities(4,4) = 0.5
win_probabilities(4,5) = 1.0
win_probabilities(4,6) = 0.0
win_probabilities(4,7) = 0.25
win_probabilities(4,8) = 0.4
win_probabilities(4,9) = 1.0
win_probabilities(4,10) = 0.0
win_probabilities(4,11) = 0.674
win_probabilities(4,12) = 0.85
win_probabilities(4,13) = 0.0
win_probabilities(4,14) = 0.0
win_probabilities(4,15) = 0.0

# 6 seed
win_probabilities(5,0) = 0.294
win_probabilities(5,1) = 0.278
win_probabilities(5,2) = 0.417
win_probabilities(5,3) = 0.667
win_probabilities(5,4) = 0.0
win_probabilities(5,5) = 0.0
win_probabilities(5,6) = 0.667
win_probabilities(5,7) = 0.25
win_probabilities(5,8) = 0.0
win_probabilities(5,9) = 0.6
win_probabilities(5,10) = 0.628
win_probabilities(5,11) = 0.0
win_probabilities(5,12) = 0.0
win_probabilities(5,13) = 0.875
win_probabilities(5,14) = 1.0
win_probabilities(5,15) = 0.0

# 7 seed
win_probabilities(6,0) = 0.143
win_probabilities(6,1) = 0.304
win_probabilities(6,2) = 0.368
win_probabilities(6,3) = 0.667
win_probabilities(6,4) = 0.0
win_probabilities(6,5) = 0.33
win_probabilities(6,6) = 0.0
win_probabilities(6,7) = 0.5
win_probabilities(6,8) = 0.0
win_probabilities(6,9) = 0.606
win_probabilities(6,10) = 0.0
win_probabilities(6,11) = 0.0
win_probabilities(6,12) = 0.0
win_probabilities(6,13) = 1.0
win_probabilities(6,14) = 0.33
win_probabilities(6,15) = 0.0

# 8 seed
win_probabilities(7,0) = 0.215
win_probabilities(7,1) = 0.6
win_probabilities(7,2) = 0.0
win_probabilities(7,3) = 0.615
win_probabilities(7,4) = 0.75
win_probabilities(7,5) = 0.75
win_probabilities(7,6) = 0.5
win_probabilities(7,7) = 0.0
win_probabilities(7,8) = 0.511
win_probabilities(7,9) = 0.0
win_probabilities(7,10) = 1.0
win_probabilities(7,11) = 0.0
win_probabilities(7,12) = 1.0
win_probabilities(7,13) = 0.0
win_probabilities(7,14) = 1.0
win_probabilities(7,15) = 0.0

# 9 seed
win_probabilities(8,0) = 0.094
win_probabilities(8,1) = 0.33
win_probabilities(8,2) = 0.25
win_probabilities(8,3) = 0.6
win_probabilities(8,4) = 0.6
win_probabilities(8,5) = 0.0
win_probabilities(8,6) = 0.0
win_probabilities(8,7) = 0.489
win_probabilities(8,8) = 0.0
win_probabilities(8,9) = 1.0
win_probabilities(8,10) = 0.0
win_probabilities(8,11) = 0.0
win_probabilities(8,12) = 1.0
win_probabilities(8,13) = 0.0
win_probabilities(8,14) = 0.0
win_probabilities(8,15) = 1.0

# 10 seed
win_probabilities(9,0) = 0.125
win_probabilities(9,1) = 0.359
win_probabilities(9,2) = 0.308
win_probabilities(9,3) = 0.0
win_probabilities(9,4) = 0.0
win_probabilities(9,5) = 0.4
win_probabilities(9,6) = 0.394
win_probabilities(9,7) = 0.0
win_probabilities(9,8) = 0.0
win_probabilities(9,9) = 0.0
win_probabilities(9,10) = 0.5
win_probabilities(9,11) = 0.0
win_probabilities(9,12) = 0.0
win_probabilities(9,13) = 1.0
win_probabilities(9,14) = 1.0
win_probabilities(9,15) = 0.0

# 11 seed
win_probabilities(10,0) = 0.444
win_probabilities(10,1) = 0.158
win_probabilities(10,2) = 0.333
win_probabilities(10,3) = 0.0
win_probabilities(10,4) = 0.0
win_probabilities(10,5) = 0.372
win_probabilities(10,6) = 1.0
win_probabilities(10,7) = 0.0
win_probabilities(10,8) = 1.0
win_probabilities(10,9) = 0.5
win_probabilities(10,10) = 0.5
win_probabilities(10,11) = 0.0
win_probabilities(10,12) = 0.0
win_probabilities(10,13) = 1.0
win_probabilities(10,14) = 0.0
win_probabilities(10,15) = 0.0

# 12 seed
win_probabilities(11,0) = 0.0
win_probabilities(11,1) = 0.0
win_probabilities(11,2) = 0.0
win_probabilities(11,3) = 0.295
win_probabilities(11,4) = 0.326
win_probabilities(11,5) = 0.0
win_probabilities(11,6) = 0.0
win_probabilities(11,7) = 1.0
win_probabilities(11,8) = 0.0
win_probabilities(11,9) = 0.0
win_probabilities(11,10) = 0.0
win_probabilities(11,11) = 0.5
win_probabilities(11,12) = 0.75
win_probabilities(11,13) = 0.0
win_probabilities(11,14) = 0.0
win_probabilities(11,15) = 0.0

# 13 seed
win_probabilities(12,0) = 0.0
win_probabilities(12,1) = 0.0
win_probabilities(12,2) = 0.0
win_probabilities(12,3) = 0.211
win_probabilities(12,4) = 0.15
win_probabilities(12,5) = 0.0
win_probabilities(12,6) = 0.0
win_probabilities(12,7) = 0.0
win_probabilities(12,8) = 0.0
win_probabilities(12,9) = 0.0
win_probabilities(12,10) = 0.0
win_probabilities(12,11) = 0.25
win_probabilities(12,12) = 0.5
win_probabilities(12,13) = 0.0
win_probabilities(12,14) = 0.0
win_probabilities(12,15) = 0.0

# 14 seed
win_probabilities(13,0) = 0.0
win_probabilities(13,1) = 0.0
win_probabilities(13,2) = 0.145
win_probabilities(13,3) = 0.0
win_probabilities(13,4) = 0.0
win_probabilities(13,5) = 0.125
win_probabilities(13,6) = 0.0
win_probabilities(13,7) = 0.0
win_probabilities(13,8) = 0.0
win_probabilities(13,9) = 0.0
win_probabilities(13,10) = 0.0
win_probabilities(13,11) = 0.0
win_probabilities(13,12) = 0.0
win_probabilities(13,13) = 0.5
win_probabilities(13,14) = 0.0
win_probabilities(13,15) = 0.0

# 15 seed
win_probabilities(14,0) = 0.0
win_probabilities(14,1) = 0.072
win_probabilities(14,2) = 0.333
win_probabilities(14,3) = 0.0
win_probabilities(14,4) = 0.0
win_probabilities(14,5) = 0.0
win_probabilities(14,6) = 0.667
win_probabilities(14,7) = 0.0
win_probabilities(14,8) = 0.0
win_probabilities(14,9) = 0.0
win_probabilities(14,10) = 0.0
win_probabilities(14,11) = 0.0
win_probabilities(14,12) = 0.0
win_probabilities(14,13) = 0.0
win_probabilities(14,14) = 0.0
win_probabilities(14,15) = 0.0

# 16 seed
win_probabilities(15,0) = 0.013
win_probabilities(15,1) = 0.0
win_probabilities(15,2) = 0.0
win_probabilities(15,3) = 0.0
win_probabilities(15,4) = 0.0
win_probabilities(15,5) = 0.0
win_probabilities(15,6) = 0.0
win_probabilities(15,7) = 0.0
win_probabilities(15,8) = 0.0
win_probabilities(15,9) = 0.0
win_probabilities(15,10) = 0.0
win_probabilities(15,11) = 0.0
win_probabilities(15,12) = 0.0
win_probabilities(15,13) = 0.0
win_probabilities(15,14) = 0.0
win_probabilities(15,15) = 0.5
