f = open("input.txt", "r")
lines = f.read().split("\n")

count = 0

# def isOverlapping(r1, r2):
#     for r in r1:
#         if

def calcCount(s1, s2, e1, e2):
    global count
    if s1 <= e1:
        print("got 1")
        for i in range(s1, s2+1):
            print("i: ", i)
            if i == e1:
                count +=1
    elif e1 <= s1:
        print("got 2")
        for i in range(e1, e2+1):
            print("i: ", i)
            if i == s1:
                count +=1


# calcCount(5,7,7,9)




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

print("count: ", count)
