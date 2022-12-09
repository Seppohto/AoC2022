# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

data = open("data\day5.txt", "r").read()
data = data.splitlines()

#there are 9 stacks
# stack number one is represented by the first 3 characters ( on places 1,2,3) on the first 8 lines
# there is a space between each stack
# stack number two is represented by the next 3 characters ( on places 5,6,7) on the first 8 lines
# and so on
# [T]     [Q]             [S]        
# [R]     [M]             [L] [V] [G]
# [D] [V] [V]             [Q] [N] [C]
# [H] [T] [S] [C]         [V] [D] [Z]
# [Q] [J] [D] [M]     [Z] [C] [M] [F]
# [N] [B] [H] [N] [B] [W] [N] [J] [M]
# [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
# [B] [W] [N] [P] [D] [V] [G] [L] [T]
#  1   2   3   4   5   6   7   8   9 
def getstacksall9stacks(data):
    stacks = []
    stack = []    
    #go through first 8 lines
    for i in range(8):
        #go through each line
        for j in range(0, len(data[i]), 4):
            #get the first 3 characters of each stack
            stacks.append(data[i][j+1])
    #loop through the stacks and add them to 9 lists
    for i in range(9):
        for j in range(8):
            if(stacks[i+j*9] != ' '):
                stack.append(stacks[i+j*9])
        stacks[i] = stack
        stack = []
    #reverse the stacks
    for i in range(9):
        stacks[i].reverse()
    return stacks

stacks = getstacksall9stacks(data)
#make stacks into dictionary
stacks = {i+1:stacks[i] for i in range(9)}

#loop through the steps starting from the line 11
for i in range(10, len(data)):
    #split the line
    step = data[i].split(' ')
    cratestomove = int(step[1])
    stacktotakefrom = int(step[3])
    stacktomoveto = int(step[5])
    #print steps
    print("move " + str(cratestomove) + " from " + str(stacktotakefrom) + " to " + str(stacktomoveto))
    #add " " to the stack to take from
    #move the crates from the stack to take from to the stack to move to
    for j in range(cratestomove):
        stacks[stacktomoveto].append(stacks[stacktotakefrom].pop())
    # for j in range(cratestomove):
    #     stacks[stacktomoveto-1].append(stacks[stacktotakefrom-1].pop())
#loop through the stacks and print the last crate
for i in range(9):
    #if the stack is not empty print value of the last crate otherwise print " "
    if(len(stacks[i+1]) != 0):
       print(stacks[i+1][-1], end='')
    else:
        print(" ", end='')
# for i in range(9):
#     print(stacks[i][0], end='')
    


