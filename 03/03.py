f = open("input.txt", "r")
sacks = f.read().split("\n")

sum = 0

def getPriorityValue(c):
    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet=list(alphabet)
    for i in range(0, len(alphabet)):
        if c == alphabet[i]:
            return i+1

for i in range(0, len(sacks), 3):
    print("i: ", i)
    if sacks[i] != '':
        currGrp = []
        currGrp.append(list(sacks[i]))
        currGrp.append(list(sacks[i+1]))
        currGrp.append(list(sacks[i+2]))

        s1 = currGrp[0]
        s2 = currGrp[1]
        s3 = currGrp[2]
        for c in s1:
            if c in s2 and c in s3:
                print("found: ", c)
                sum += getPriorityValue(c)
                break

print("sum: ", sum)


# for sack in sacks:
#     if sack != "":
#         sack = list(sack)
#         # print("sack: ", sack)
#         length = len(sack)
#         c1 = sack[slice(0, length//2)]
#         # print("c1: ", sack[c1])
#         c2 = sack[slice(length//2, length)]
#         # print("c2: ", sack[c2])
#         currDubs=[]
#         for c in c1:
#             for d in c2:
#                 if c == d and c not in currDubs:
#                     sum += getPriorityValue(c)
#                     currDubs.append(c)

# print("sum: ", sum)


