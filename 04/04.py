f = open("input.txt", "r")
lines = f.read().split("\n")

count = 0

def calcCount(s1, s2, e1, e2):
    global count
    if s1 == e1 and s2 == e2:
        count += 1
    elif s1 <= e1 and s2 >= e2:
        count += 1
    elif e1 <= s1 and e2 >= s2:
        count += 1

for line in lines:
    if line != "":
        pair = line.split(",")
        start = pair[0].split("-")
        end = pair[1].split("-")

        s1 = int(start[0])
        s2 = int(start[1])
        e1 = int(end[0])
        e2 = int(end[1])

        calcCount(s1, s2, e1, e2)

# calcCount(1, 82, 1, 82)

print("count: ", count)


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


