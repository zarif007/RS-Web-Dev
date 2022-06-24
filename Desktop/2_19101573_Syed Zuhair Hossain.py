#library imports
import numpy as np
#using numpy library to handle infinity issues
import random as rd
#using random library to generate random numbers

# initial input taking
l03_input_st_id = input("Enter Student ID: ")


l03_turn_no = int(l03_input_st_id[0])
#print("Enter the number of nodes in the tree: ")
tree_depth = 2 * l03_turn_no
#print("Enter the number of branches in the tree: ")
#l03_branch_num_count = int(input())
l03_initial_string = l03_input_st_id[7] + l03_input_st_id[6]
#taking 6th and 7th digit of the student id as the initial string
#print("Enter the initial string: ")
l03_initial_hp1 = int(l03_initial_string)
#print("initail HP: ", l03_l03_initial_hp1)
l03_branch_num_count = int(l03_input_st_id[2])

# print("Branches: ", l03_branch_num_count)
# print("Depth: ", tree_depth)

l03_minval_maxval=input("Enter Min-Max: ")
#print(l03_minval_maxval)

l03_temp_var = l03_minval_maxval.split()
# splitting min and max value from the inputted string
l03_min_def = int(l03_temp_var[0])
# print(l03_min_def)
l03_max_def = int(l03_temp_var[1])
# print(l03_max_def)

l03_leaf_node_var = l03_branch_num_count ** tree_depth
#print("Leaf Nodes: ", l03_leaf_node_var)

l03_leaf_nodes = rd.sample (range (l03_min_def, l03_max_def), l03_leaf_node_var)
#min-level: beta changes, max-level: alpha changes
#if alpha is greater or 0equal to beta whole alpha_beta branch will be pruned


def min_and_max_find(l03_leaf_node_idx, depth_in_minmax_meth, alpha_val, beta_val, maximizingPlayer):

    if depth_in_minmax_meth == tree_depth:
        #print("Depth: ", depth_in_minmax_meth)
        global node_traverse_count
        #print("Total Nodes Traversed: ", node_traverse_count)

        node_traverse_count += 1
        #print("Total Nodes Traversed: ", node_traverse_count)
        return l03_leaf_nodes[l03_leaf_node_idx]

    if maximizingPlayer == True:
        #print("Maximizing Player")
        maxVal = -np.inf
        #print("Max Value: ", maxVal)
        for iter_i in range(l03_branch_num_count):
            d_temp = depth_in_minmax_meth + 1
            #print("Depth: ", d_temp)
            temp_max = l03_leaf_node_idx * l03_branch_num_count
            #print("Temp Max: ", temp_max)
            value_check = min_and_max_find(temp_max + iter_i, d_temp, alpha_val, beta_val, False)
            #print("Value: ", value_check)
            maxVal = max(maxVal, value_check)
            #print("Max Value: ", maxVal)
            alpha_val = max(alpha_val, maxVal)
            #print("Alpha Value: ", alpha_val)

            if beta_val <= alpha_val:
                #if beta is less than alpha, then prune the branch
                break
        return maxVal
    else:
        minVal = np.inf
        #print("Min Value: ", minVal)
        for iter_j in range(l03_branch_num_count):
            d_temp = depth_in_minmax_meth + 1
            #print("Depth: ", d_temp)
            temp_min = l03_leaf_node_idx * l03_branch_num_count
            #print("Temp Min: ", temp_min)
            value_check = min_and_max_find(temp_min + iter_j, d_temp, alpha_val, beta_val, True)
            #print("Value: ", value_check)
            
            minVal = min(minVal, value_check)
            #print("Min Value: ", minVal)
            beta_val = min(beta_val, minVal)
            #print("Beta Value: ", beta_val)

            if beta_val <= alpha_val:
                ##if beta is less than alpha, then prune the branch again
                break
        #print("Min Value: ", minVal)
        #dual check done, but did not pass properly yet
        return minVal


#print("Min Value: ", min_and_max_find(0, 0, -np.inf, np.inf, True))

#Alpha Beta Pruning Method Call
#initializing the variables
node_traverse_count = 0

some_value=min_and_max_find(0, 0, -np.inf, np.inf, True)

# output format

print(f"1. Depth and Branches ratio is {tree_depth}:{l03_branch_num_count}")
# this works properly for test case 1
print("2. Terminal States (leaf node values) are", l03_leaf_nodes, ".")
# this is not working :'(
print("3. Left life(HP) of the defender after maximum damage caused by the attacker is",l03_initial_hp1-some_value)
# not this too
print("4. After Alpha-Beta Pruning Leaf Node Comparisons", node_traverse_count)
# this is not working too :(