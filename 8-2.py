# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

# In the example above, consider the middle 5 in the second row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

# Consider each tree on your map. What is the highest scenic score possible for any tree?

data = open('data/day8.txt').read().splitlines()

#make a matrix of the data
matrix = []
for line in data:
    linearray = []
    for char in line:
        linearray.append(char)
    #next array in the matrix
    matrix.append(linearray)


#now we need to count the number of trees visible from the edge

#edges are left of each array, right of each array, top of each position in each array, bottom of each position in each array
def countscenicscore(matrix):    
    best_scenic_score = 0
    for i in range(len(matrix)):        
        #if its the first or last position in the array, all the trees are visible
        for j in range(len(matrix[i])):
            scenic_score = 0
            if i == 0 or i == len(matrix) - 1: 
                continue
            elif j == 0 or j == len(matrix[i]) - 1:
                continue
            #if its not the first or last position in the array, check if the tree is visible
            else:
                scenic_score_down = 0
                scenic_score_up = 0
                scenic_score_left = 0
                scenic_score_right = 0
                for k in range(i+1, len(matrix)):
                    if matrix[i][j] > matrix[k][j]:
                        scenic_score_down += 1                        
                    else:
                        scenic_score_down += 1
                        break
                for k in range(i-1, -1, -1):
                    if matrix[i][j] > matrix[k][j]:
                        scenic_score_up += 1                        
                    else:
                        scenic_score_up += 1
                        break
                for k in range(j+1, len(matrix[i])):
                    if matrix[i][j] > matrix[i][k]:
                        scenic_score_right += 1                        
                    else:
                        scenic_score_right += 1
                        break
                for k in range(j-1, -1, -1):
                    if matrix[i][j] > matrix[i][k]:
                        scenic_score_left += 1                        
                    else:
                        scenic_score_left += 1
                        break
            scenic_score = scenic_score_down * scenic_score_up * scenic_score_left * scenic_score_right
            # set best scenic score
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
    return best_scenic_score

print(countscenicscore(matrix))


