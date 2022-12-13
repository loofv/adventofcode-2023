f = open("input.txt", "r")
lines = f.read()
lines = list(lines)
cl = []

def checkAns(c, cl):
    for i in range(c+1, c+15):
        curr = lines[i]
        # print("looking at:", curr)
        # print("for starter:", prev)
        if curr not in cl:
            # print("diff found:", curr)
            cl.append(curr)
            if len(cl) == 14:
                print("found c no: ", c+14)
                print("cl: ", cl)
                return True
            # print("length of cl: ", len(cl))
        else:
            return False

for c in range(0, len(lines)-4):
    cl = []
    prev = lines[c]
    cl.append(prev)
    if checkAns(c, cl):
        break

