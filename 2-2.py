# --- Day 2: Rock Paper Scissors ---
# --- Part One ---
data = open("data\day2.txt", "r").read()
data = data.split("\n")
data = [i.split(" ") for i in data]
# calculate the score for each round
# A is rock, B is paper, C is scissors
# 6 points for a win, 3 points for a tie, 0 points for a loss
# score for picking A is 1, score for picking B is 2, score for picking C is 3

# X Lose, Y draw, Z win

# calculate the score for picking 
def calculatep2score(p2):    
    if p2 == "A": # Rock
        return 1
    elif p2 == "B": # Paper
        return 2
    elif p2 == "C": # Scissors
        return 3

def transformp2values(p1, p2):
    if p2 == "X":
        if p1 == "A":
            return "C"
        elif p1 == "B":
            return "A"
        elif p1 == "C":
            return "B"
    elif p2 == "Y":
        return p1        
    elif p2 == "Z":
        if p1 == "A":
            return "B"
        elif p1 == "B":
            return "C"
        elif p1 == "C":
            return "A"

def score(p1, p2):
    p2 = transformp2values(p1, p2)
    extrascore = calculatep2score(p2)
    if p1 == p2:
        return 3 + extrascore
    elif p1 == "A" and p2 == "B":
        return 6 + extrascore
    elif p1 == "A" and p2 == "C":
        return 0 + extrascore
    elif p1 == "B" and p2 == "A":
        return 0 + extrascore
    elif p1 == "B" and p2 == "C":
        return 6 + extrascore
    elif p1 == "C" and p2 == "A":
        return 6 + extrascore
    elif p1 == "C" and p2 == "B":
        return 0 + extrascore

# calculate the score for each round


data = [[score(i[0], i[1])] for i in data]

# calculate total score
data = [sum(i) for i in data]



print(sum(data))
