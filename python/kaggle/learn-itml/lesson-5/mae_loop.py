# How to optimize the configuration (depth) of a decision tree (that was trained on a given subset of features) 

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

# Write loop to find the ideal tree size from candidate_max_leaf_nodes
# I wrote this
maes = []
for candidate in candidate_max_leaf_nodes:
    maes.append(get_mae(candidate, train_X, val_X, train_y, val_y))

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
# And this
best_tree_size = candidate_max_leaf_nodes[maes.index(min(maes))]

# Kaggle thingy
# Check your answer
# step_1.check()
