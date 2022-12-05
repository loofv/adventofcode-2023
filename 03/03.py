f = open("input.txt", "r")
sacks = f.read().split("\n")

sum = 0

def getPriorityValue(c):
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet=list(alphabet)
    for i in range(0, len(alphabet)):
        if c == alphabet[i]:
            return i+1

# print(str(getPriorityValue("a")))

# print("expected: 26, actual: ", str(getPriorityValue("Z")))

for sack in sacks:
    if sack != "":
        sack = list(sack)
        # print("sack: ", sack)
        length = len(sack)
        c1 = sack[slice(0, length//2)]
        # print("c1: ", sack[c1])
        c2 = sack[slice(length//2, length)]
        # print("c2: ", sack[c2])
        currDubs=[]
        for c in c1:
            for d in c2:
                if c == d and c not in currDubs:
                    sum += getPriorityValue(c)
                    currDubs.append(c)

print("sum: ", sum)


