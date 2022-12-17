# --- Day 14: Regolith Reservoir ---
# The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

# Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

# As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

# Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

# The sand is pouring into the cave from point 500,0.

# Drawing rock as #, air as ., and the source of the sand as +, this becomes:


#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.
# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

# A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

# So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# ......o.#.
# #########.
# The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# .....oo.#.
# #########.
# After a total of five units of sand have come to rest, they form this pattern:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ......o.#.
# ....oooo#.
# #########.
# After a total of 22 units of sand:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ....#ooo#.
# ..###ooo#.
# ....oooo#.
# ...ooooo#.
# #########.
# Finally, only two more units of sand can possibly come to rest:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #########.
# Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

# .......+...
# .......~...
# ......~o...
# .....~ooo..
# ....~#ooo##
# ...~o#ooo#.
# ..~###ooo#.
# ..~..oooo#.
# .~o.ooooo#.
# ~#########.
# ~..........
# ~..........
# ~..........
# Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?

# --- Part Two ---
# You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

# You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

# In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

#         ...........+........
#         ....................
#         ....................
#         ....................
#         .........#...##.....
#         .........#...#......
#         .......###...#......
#         .............#......
#         .............#......
#         .....#########......
#         ....................
# <-- etc #################### etc -->
# To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

# ............o............
# ...........ooo...........
# ..........ooooo..........
# .........ooooooo.........
# ........oo#ooo##o........
# .......ooo#ooo#ooo.......
# ......oo###ooo#oooo......
# .....oooo.oooo#ooooo.....
# ....oooooooooo#oooooo....
# ...ooo#########ooooooo...
# ..ooooo.......ooooooooo..
# #########################
# Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

data = open('data/day14.txt').read().splitlines()
sandspot=(500,0)
sandspot=sandspot[0]+1,sandspot[1]
def create_cave(data):
    for i in range(len(data)):
        data[i] = data[i].split(' -> ')
    #
    #save each comma separated value as a tuple in a list

    for i in data:
        for j in range(len(i)):
            i[j] = tuple(map(int, i[j].split(',')))


    #create a 2d array of points to represent the cave system start from 5 distance of the left and 0 distance from the top
    #find the max x and y values to determine the size of the array
    max_x = data[0][0][0]
    max_y = data[0][0][1]
    min_x = data[0][0][0]
    min_y = data[0][0][1]

    for i in data:
        for j in i:
            if j[0] > max_x:
                max_x = j[0]
            if j[1] > max_y:
                max_y = j[1]
            if j[0] < min_x:
                min_x = j[0]
            if j[1] < min_y:
                min_y = j[1]

    height = max_y
    width = max_x - min_x + 3

    # create 2d array of points
    cave = []
    for i in range(height+3):
        cave.append([])
        for j in range(width):
            cave[i].append('.')
        # if its the last row, fill it with '#'
        if i == height+2:
            for j in range(width):
                cave[i][j] = '#'
    cave[0][500-min_x+1] = '+'

    #fill in the cave with the data rocks
    for i in data:
        count=0
        for j in i:
            if count == len(i)-1:
                break
            count += 1
            if j[0] == i[count][0]:
                startposition=j[1]
                endposition=i[count][1]
                if startposition > endposition:
                    startposition, endposition = endposition, startposition
                for k in range(startposition, endposition+1):
                    #put '#' to represent rock
                    cave[k][j[0]-min_x+1] = '#'
            else:
                startposition=j[0]-min_x+1
                endposition=i[count][0]-min_x+1
                if startposition > endposition:
                    startposition, endposition = endposition, startposition
                for k in range(startposition, endposition+1):
                    cave[j[1]][k] = '#'
        
       
#printcave
    return cave, min_x
cave, min_x = create_cave(data)

# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

# A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

# So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

def sand_drip(cave,sandspot,rounds, min_x):
    sandposition = sandspot
    for i in range(rounds):
        sandinmotion = True
        wider=0
        #try error if out of range
        try:
            if i == 0:
                sandposition = sandspot[0],sandspot[1]+wider
            while sandinmotion:
                #check if sand can move down
                if cave[sandposition[1]+1][sandposition[0]-min_x] == '.':
                    cave[sandposition[1]][sandposition[0]-min_x] = '.'
                    cave[sandposition[1]+1][sandposition[0]-min_x] = '~'
                    sandposition = (sandposition[0],sandposition[1]+1)
                #check if sand can move down left
                elif cave[sandposition[1]+1][sandposition[0]-min_x-1] == '.':
                    cave[sandposition[1]][sandposition[0]-min_x] = '.'
                    cave[sandposition[1]+1][sandposition[0]-min_x-1] = '~'
                    sandposition = (sandposition[0]-1,sandposition[1]+1)
                    if sandposition[0]-min_x == 0:
                        for i in range(len(cave)):
                            cave[i].insert(0,'.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                        min_x -= 1
                    elif sandposition[0]-min_x == len(cave[0])-1:
                        for i in range(len(cave)):
                            cave[i].append('.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                #check if sand can move down right
                elif cave[sandposition[1]+1][sandposition[0]-min_x+1] == '.':
                    cave[sandposition[1]][sandposition[0]-min_x] = '.'
                    cave[sandposition[1]+1][sandposition[0]-min_x+1] = '~'
                    sandposition = (sandposition[0]+1,sandposition[1]+1)
                    if sandposition[0]-min_x == 0:
                        for i in range(len(cave)):
                            cave[i].insert(0,'.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                        min_x -= 1
                    elif sandposition[0]-min_x == len(cave[0])-1:
                        for i in range(len(cave)):
                            cave[i].append('.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                else:
                    #if sand can't move and its still in the starting position return cave and i 
                    cave[sandposition[1]][sandposition[0]-min_x] = 'o'
                    if sandposition == sandspot:
                        return cave, i+1
                    #if sand position is at the left or right edge of the cave, make the cave bigger
                    if sandposition[0]-min_x == 0:
                        for i in range(len(cave)):
                            cave[i].insert(0,'.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                        min_x -= 1
                    elif sandposition[0]-min_x == len(cave[0])-1:
                        for i in range(len(cave)):
                            cave[i].append('.')
                            if i == len(cave)-1:
                                for j in range(len(cave[i])):
                                    cave[i][j] = '#'
                    sandposition = sandspot[0],sandspot[1]+wider
                    sandinmotion = False
                    
        except:
            return cave, i
    return cave, rounds

cave, rounds = sand_drip(cave,sandspot,30000, min_x)
for i in cave:
    for j in i:
        print(j, end='')
    print()
print(rounds)