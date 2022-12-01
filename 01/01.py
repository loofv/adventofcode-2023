f = open("input.txt", "r")

lines = f.read().splitlines()

elfKcals = []

maxKcal = 0
currElf = 0
for line in lines:
    if line != '':
        currElf += int(line)
    else:
        elfKcals.append(currElf)
        currElf = 0

print(elfKcals)
elfKcals.sort(reverse=True)
print(elfKcals)

top3Total = elfKcals[0] + elfKcals[1] + elfKcals[2]

print("top 3 total: ", top3Total)
# print("expected: ", 24000)
# print("actual: " , maxKcal)




# for line in lines:
#     if line != '':
#         print("was not empty string")
#         currElf.add(int(line))
#         currKcal += int(line)
#         print("currKcal is now: ", currKcal)
#     else:
#         print("was empty string")
#         print("maxkcal is: ", maxKcal)
#         if currKcal > maxKcal:
#             print("curr was greater than max")
#             print("curr is: ", currKcal)
#             print("max is: ", maxKcal)
#             maxKcal = currKcal
#             print("max is now set to: ", maxKcal)
#         currKcal = 0
# print("expected: ", 24000)
# print("actual: " , maxKcal)
