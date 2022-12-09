
data = open("data\day5.txt", "r").read()
data = data.splitlines()

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
    #add " " to the stack to take from
    #move the crates from the stack to take from to the stack to move to all at once and keep the same order
    stacks[stacktomoveto] = stacks[stacktomoveto] + stacks[stacktotakefrom][-cratestomove:]
    #remove the crates from the stack to take from
    stacks[stacktotakefrom] = stacks[stacktotakefrom][:-cratestomove]
#loop through the stacks and print the last crate
for i in range(9):
    #if the stack is not empty print value of the last crate otherwise print " "
    if(len(stacks[i+1]) != 0):
       print(stacks[i+1][-1], end='')
    else:
        print(" ", end='')
# for i in range(9):
#     print(stacks[i][0], end='')
    


