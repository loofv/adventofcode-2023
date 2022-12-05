
def convertToP1(p2):
    if p2 == "X":
        return "A"
    elif p2 == "Y":
        return "B"
    else:
        return "C"

def getScoreForVal(val):
    if val == "A":
        return 1
    elif val == "B":
        return 2
    else:
        return 3


def calcScore(p1, p2):
    p2 = convertToP1(p2)
    if p1 == "A":
        if p2 == "A":
            return 3 + getScoreForVal(p2)
        elif p2 == "B":
            return 6 + getScoreForVal(p2)
        elif p2 == "C":
            return 0 + getScoreForVal(p2)

    elif p1 == "B":
        if p2 == "A":
            return 0 + getScoreForVal(p2)
        elif p2 == "B":
            return 3 + getScoreForVal(p2)
        elif p2 == "C":
            return 6 + getScoreForVal(p2)

    elif p1 == "C":
        if p2 == "A":
            return 6 + getScoreForVal(p2)
        elif p2 == "B":
            return 0 + getScoreForVal(p2)
        elif p2 == "C":
            return 3 + getScoreForVal(p2)

# print(str(calcScore("A", "Y")))
# print(str(calcScore("B", "X")))
# print(str(calcScore("C", "Z")))


score = 0

f = open("input.txt", "r")
lines = f.read().split("\n")

for line in lines:
    if line != '':
        curr = line.split(" ")
        print("Curry: ", curr)
        score += calcScore(curr[0], curr[1])

print("score: ", score)
