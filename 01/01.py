f = open("input.txt", "r")

lines = f.read().splitlines()

maxKcal = 0
currKcal = 0
for line in lines:
    print(line)
    if line != '':
        print("was not empty string")
        currKcal += int(line)
        print("currKcal is now: ", currKcal)
    else:
        print("was empty string")
        print("maxkcal is: ", maxKcal)
        if currKcal > maxKcal:
            print("curr was greater than max")
            print("curr is: ", currKcal)
            print("max is: ", maxKcal)
            maxKcal = currKcal
            print("max is now set to: ", maxKcal)
        currKcal = 0
print("expected: ", 24000)
print("actual: " , maxKcal)
