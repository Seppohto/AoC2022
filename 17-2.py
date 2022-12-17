
import copy
data = open('data/day17.txt').read().splitlines()
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
    bottomheight = 0
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
        #do check after every 40 rocks
        if droppedrocks % 200 == 0:
            for i in range(len(chamber)-1):
                # print("i", i)
                if all("#" in j for j in chamber[i]):
                    #save the height of the row
                    bottomheight += len(chamber)-i
                    print("bottomheight", bottomheight)
                    #cut rest of the chamber off
                    chamber = chamber[:i]
                    break
        for i in range(len(chamber)):
            if any("#" in j for j in chamber[i]):
                highest_rock = len(chamber)-i
                break
    highest_rock = bottomheight + highest_rock


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

chamber, highest_rock = drop_rocks(rocks, chamber, data, 2022)
print("highest rock", highest_rock)
