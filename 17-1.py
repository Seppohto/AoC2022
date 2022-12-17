# --- Day 17: Pyroclastic Flow ---
# Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

# The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

# The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# ##
# The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

# The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

# For example, suppose this was the jet pattern in your cave:

# >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
# In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

# After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

# Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right:
# |...@@@@|
# |.......|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# |.......|
# +-------+

# Jet of gas pushes rock right, but nothing happens:
# |...@@@@|
# |.......|
# +-------+

# Rock falls 1 unit:
# |...@@@@|
# +-------+

# Jet of gas pushes rock left:
# |..@@@@.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |..####.|
# +-------+

# A new rock begins falling:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |..####.|
# +-------+

# Jet of gas pushes rock left:
# |..@....|
# |.@@@...|
# |..@....|
# |.......|
# |..####.|
# +-------+

# Rock falls 1 unit:
# |..@....|
# |.@@@...|
# |..@....|
# |..####.|
# +-------+

# Jet of gas pushes rock right:
# |...@...|
# |..@@@..|
# |...@...|
# |..####.|
# +-------+

# Rock falls 1 unit, causing it to come to rest:
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# A new rock begins falling:
# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |...#...|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# The moment each of the next few rocks begins falling, you would see this:

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |..#....|
# |..#....|
# |####...|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |...@...|
# |..@@@..|
# |...@...|
# |.......|
# |.......|
# |.......|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |....@..|
# |....@..|
# |..@@@..|
# |.......|
# |.......|
# |.......|
# |..#....|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@....|
# |..@....|
# |..@....|
# |..@....|
# |.......|
# |.......|
# |.......|
# |.....#.|
# |.....#.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@...|
# |..@@...|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |....##.|
# |..####.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+

# |..@@@@.|
# |.......|
# |.......|
# |.......|
# |....#..|
# |....#..|
# |....##.|
# |##..##.|
# |######.|
# |.###...|
# |..#....|
# |.####..|
# |....##.|
# |....##.|
# |....#..|
# |..#.#..|
# |..#.#..|
# |#####..|
# |..###..|
# |...#...|
# |..####.|
# +-------+
# To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

# How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
import copy
data = open('data/day17.txt').read().splitlines()
# The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

# ####

# .#.
# ###
# .#.

# ..#
# ..#
# ###

# #
# #
# #
# #

# ##
# #
rocks = {1: [["#", "#", "#", "#"]],
        2: [[".", "#", "."], 
            ["#", "#", "#"], 
            [".", "#", "."]],
        3: [[".", ".", "#"], 
            [".", ".", "#"], 
            ["#", "#", "#"]],
        4: [["#"], 
            ["#"], 
            ["#"], 
            ["#"]],
        5: [["#", "#"], 
            ["#", "#"]]}
#The tall, vertical chamber is exactly seven units wide. Each rock appears
# so that its left edge is two units away from the left wall and its bottom edge
#  is three units above the highest rock in the room (or the floor, if there isn't one).
#example how first rock begins falling

# The first rock begins falling:
# |..@@@@.|
# |.......|
# |.......|
# |.......|
# +-------+

# build the chamber
chamber = []

def initiate_rocks(rocks, chamber, rock_type, highest_rock):
    #if top of the chamber is not 3 units above the highest rock increase the chamber height so that it is
    while len(chamber) - highest_rock != 3+len(rocks[rock_type]):
        #if the difference between the height of the chamber and the highest rock is less than 3+the height of the rock
        if len(chamber) - highest_rock < 3+len(rocks[rock_type]):
            chamber.insert(0, ["."]*7)
        else:
            chamber.pop(0)
    #initate the rock at the top and two units away from the left wall
    for i in range(len(rocks[rock_type])):
        for j in range(len(rocks[rock_type][i])):
            if rocks[rock_type][i][j] == "#":
                chamber[i][j+2] = "@"

    return chamber

def move_rocks(direction, chamber, rockisfalling):
    original_chamber = copy.deepcopy(chamber)
    if direction == "down":
        #move rocks down
        for i in range(len(chamber)-1, -1, -1):
            for j in range(len(chamber[i])):
                if chamber[i][j] == "@":
                    #test if the rock is at the bottom or if there is a rock in the way
                    if i == len(chamber)-1 or chamber[i+1][j] == "#":
                        rockisfalling = True
                        return original_chamber[:], rockisfalling
                    chamber[i][j] = "."
                    chamber[i+1][j] = "@"
    elif direction == "left":
        #move rocks left
        for i in range(len(chamber)):
            for j in range(len(chamber[i])):
                if chamber[i][j] == "@":
                    #test if the rock is at the left wall or if there is a rock in the way
                    if j == 0 or chamber[i][j-1] == "#":
                        return original_chamber[:], rockisfalling
                    chamber[i][j] = "."
                    chamber[i][j-1] = "@"
    elif direction == "right":
        #move rocks right
        for i in range(len(chamber)):
            for j in range(len(chamber[i])-1, -1, -1):
                if chamber[i][j] == "@":
                    #test if the rock is at the right wall or if there is a rock in the way
                    if j == len(chamber[i])-1 or chamber[i][j+1] == "#":
                        return original_chamber[:], rockisfalling
                    chamber[i][j] = "."
                    chamber[i][j+1] = "@"
    return chamber, rockisfalling

def drop_rocks(rocks, chamber, data, numberofrocks):
    droppedrocks = 0
    rock_type = 1
    highest_rock = 0
    jetmode = True
    jetnumber = 0
    rockisfalling = False
    while droppedrocks < numberofrocks:    
        initiate_rocks(rocks, chamber, rock_type, highest_rock)
        while True:
            #check if the there are rocks in motion
            if not any("@" in i for i in chamber):
                break
            #drop the rocks
            if jetmode:
                if data[0][jetnumber] == ">":
                    #push rocks to right
                    chamber, rockisfalling = move_rocks("right", chamber, rockisfalling)
                else:
                    #push rocks to left
                    chamber, rockisfalling = move_rocks("left", chamber, rockisfalling)
                jetnumber += 1
                if jetnumber == len(data[0]):
                    jetnumber = 0
                jetmode = False
            else:
                #move rocks down
                chamber, rockisfalling = move_rocks("down", chamber, rockisfalling)
                jetmode = True    

                if rockisfalling:
                    #turn falling rock to stationary rock
                    for i in range(len(chamber)):
                        for j in range(len(chamber[i])):
                            if chamber[i][j] == "@":
                                chamber[i][j] = "#"
                    rockisfalling = False
                    break
            #check if the rock has hit the bottom
        #check
        droppedrocks += 1 
        rock_type += 1
        if rock_type == 6:
            rock_type = 1
        #find the highest rock from the bottom and give value as looking from the bot, so 0 is a t bottom of the cave
        for i in range(len(chamber)):
            if any("#" in j for j in chamber[i]):
                highest_rock = len(chamber)-i
                break
    return chamber, highest_rock

#draw the chamber
def print_chamber(chamber):
    for i in chamber:
        print('|', end='')
        for j in i:
            print(j, end='')
        print('|')
    print('+-------+')
    print()
    return

chamber, highest_rock = drop_rocks(rocks, chamber, data, 50)
print("highest rock", highest_rock)
