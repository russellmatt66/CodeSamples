'''
Computes the probability that a hybrid fusion is attuned to a specific element

A hybrid fusion is a dragon whose parents are different species. For example, a Red/White hybrid fusion has a Red Dragon as one parent, and a White Dragon as the other.

Attunement describes the state of being able to weave a given Element. The magic system is elementally-based, with six being weavable:
(1) Earth
(2) Fire
(3) Wind
(4) Light
(5) Water
(6) Ice
'''
import sys

P1 = float(sys.argv[1])
P2 = float(sys.argv[2])

P_att = P1 + P2 - P1*P2

print("Probability of attunement is {}".format(P_att))
