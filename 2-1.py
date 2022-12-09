# --- Day 2: Rock Paper Scissors ---
# --- Part One ---
data = open("data\day2.txt", "r").read()
data = data.split("\n")
data = [i.split(" ") for i in data]
# calculate the score for each round
# A is rock, B is paper, C is scissors
# 6 points for a win, 3 points for a tie, 0 points for a loss
# score for picking A is 1, score for picking B is 2, score for picking C is 3

# calculate the score for picking 
def calculatep2score(p2):    
    if p2 == "A":
        return 1
    elif p2 == "B":
        return 2
    elif p2 == "C":
        return 3

def transformp2values(p2):
    if p2 == "X":
        return "A"
    elif p2 == "Y":
        return "B"
    elif p2 == "Z":
        return "C"

def score(p1, p2):
    p2 = transformp2values(p2)
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
