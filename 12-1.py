# --- Day 12: Hill Climbing Algorithm ---
# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# What is the fewest steps required to move from your current position to the location that should get the best signal?

data = open('data/day12.txt').read().splitlines()

#save the data into 2 dimensional array of characters
matrix = []
for line in data:
    linearray = []
    for char in line:
        linearray.append(char)
    #next array in the matrix
    matrix.append(linearray)

#find the start and end points
start = []
end = []
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        count+=1
        if matrix[i][j] == 'S':
            start = [i,j]
            matrix[i][j] = 'a'
        elif matrix[i][j] == 'E':
            end = [i,j]
            matrix[i][j] = 'z'
print('start: ',start)
print('end: ',end)
#transform each character to a number
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = ord(matrix[i][j]) - 97


def getclosestfour(matrix,currentposition):
    #compare values up, down, left, right and return values of each
    #if not at the top edge, check up
    if currentposition[0] != 0:
        up = matrix[currentposition[0]-1][currentposition[1]]
    else:
        up = 100
    #if not at the bottom edge, check down
    if currentposition[0] != len(matrix)-1:
        down = matrix[currentposition[0]+1][currentposition[1]]
    else:
        down = 100
    #if not at the left edge, check left
    if currentposition[1] != 0:
        left = matrix[currentposition[0]][currentposition[1]-1]
    else:
        left = 100
    #if not at the right edge, check right
    if currentposition[1] != len(matrix[0])-1:
        right = matrix[currentposition[0]][currentposition[1]+1]
    else:
        right = 100
    return [up,down,left,right]
visitedspots = []
#start from the end and work backwards until you reach the start
#keep track of the path you take
#keep track of the number of steps you take
#keep track of the lowest number of steps you take
def climb(matrix,start,end):
    paths = [[[start[0],start[1]]]]
    #initialize the current path
    newpaths = []
    visitedspots = []
    #initialize the path
    #initialize the current elevation
    currentpositionvalue = matrix[start[0]][start[1]]
    for i in range(6800):
        # print('i: ',i)
        newpaths = []
        newpaths = paths[:]
        # print(len(newpaths))
        for path in newpaths:
            #add last position in path to visited spots
            # print(path[-1])
            
            # print('visitedspots: ',len(visitedspots))
            #get path index
            pathindex = paths.index(path)
            #set last position in path as current position
            currentposition = path[-1]
            #set current position value
            currentpositionvalue = matrix[currentposition[0]][currentposition[1]]
            if currentposition == end:
                #append path to paths
                return i
            #if the current position is not the end, continue
            else:                
                up,down,left,right = getclosestfour(matrix,currentposition)
                #initialize new paths for each direction
                newpath= path[:]
                uppath = path[:]
                downpath = path[:]
                leftpath = path[:]
                rightpath = path[:]
                #if up is 1 higher, same level or lower, add it to the path and move to it
                if up == currentpositionvalue + 1 or up == currentpositionvalue or up < currentpositionvalue :
                    uppath.append([newpath[-1][0]-1,newpath[-1][1]])              
                #if down is 1 higher, same level or lower, add it to the path and move to it
                if down == currentpositionvalue + 1 or down == currentpositionvalue or down < currentpositionvalue :
                    downpath.append([newpath[-1][0]+1,newpath[-1][1]])
                #if left is 1 higher, same level or lower, add it to the path and move to it
                if left == currentpositionvalue + 1 or left == currentpositionvalue or left < currentpositionvalue :
                    leftpath.append([newpath[-1][0],newpath[-1][1]-1])
                #if right is 1 higher, same level or lower, add it to the path and move to it
                if right == currentpositionvalue + 1 or right == currentpositionvalue or right < currentpositionvalue:
                    rightpath.append([newpath[-1][0],newpath[-1][1]+1])
                
                #print paths
                up,down,left,right = False,False,False,False
                #check if uppath,downpath,leftpath,rightpath last points are in visitedpoints
                if uppath[-1] not in visitedspots:
                    up = True
                if downpath[-1] not in visitedspots:
                    down = True
                if leftpath[-1] not in visitedspots:
                    left = True
                if rightpath[-1] not in visitedspots:
                    right = True
                

                #if they are not add them to paths
                # print(visitedspots)
                if up == True:
                    visitedspots.append(uppath[-1])
                    paths.append(uppath)
                if down == True:
                    visitedspots.append(downpath[-1])
                    paths.append(downpath)
                if left == True:
                    visitedspots.append(leftpath[-1])
                    paths.append(leftpath)
                if right == True:  
                    visitedspots.append(rightpath[-1])
                    paths.append(rightpath)
                #remove the current path from paths
                # print(len(visitedspots))
                paths.remove(path)
    return
#print last 5 visited spots
# print (climb(matrix,start,end))
#part 2
#find shortest path from any a to end
#all the b are it colum poistion 1
def findshortestroutefromatoend(matrix):
    #run climb from each row 0 position as start
    #find the shortest path
    k =440
    for i in range(len(matrix)):
        print (i)
        j = climb(matrix,[i,0],end)
        print(j)
        if k > j:
            k = j
        else:
            k = k
    return k
print(findshortestroutefromatoend(matrix))

