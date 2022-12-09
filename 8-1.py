# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

# Consider your map; how many trees are visible from outside the grid?


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
def counttrees(matrix):    
    trees = 0
    for i in range(len(matrix)):        
        #if its the first or last position in the array, all the trees are visible
        for j in range(len(matrix[i])):
            if i == 0 or i == len(matrix) - 1:            
                trees += 1
                continue
            elif j == 0 or j == len(matrix[i]) - 1:
                trees += 1
                continue
            #if its not the first or last position in the array, check if the tree is visible
            else:
                isvisible = []
                for k in range(i+1, len(matrix)):
                    if matrix[i][j] > matrix[k][j]:
                        isvisible.append("True")
                    else:
                        isvisible.append("False")
                if "False" not in isvisible:
                    trees += 1
                    continue
                isvisible = []
                for k in range(i-1, -1, -1):
                    if matrix[i][j] > matrix[k][j]:
                        isvisible.append("True")
                    else:
                        isvisible.append("False")
                if "False" not in isvisible:
                    trees += 1
                    continue
                isvisible = []
                for k in range(j+1, len(matrix[i])):
                    if matrix[i][j] > matrix[i][k]:
                        isvisible.append("True")
                    else:
                        isvisible.append("False")
                if "False" not in isvisible:
                    trees += 1
                    continue
                isvisible = []
                for k in range(j-1, -1, -1):
                    if matrix[i][j] > matrix[i][k]:
                        isvisible.append("True")
                        continue
                    else:
                        isvisible.append("False")
                if "False" not in isvisible:
                    trees += 1
                    continue
    return trees

print(counttrees(matrix))


