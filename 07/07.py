f = open("input2.txt", "r")
lines = f.read().split("\n")
print(lines)
sums = 0
currFiles = []
for i in range(0, len(lines)):
    curr = lines[i]
    if curr != "":
        currChar = curr[0]
        if currChar.isnumeric():
            sumString = "".join(ch for ch in curr if ch.isnumeric())
            currFiles.append(int(sumString))
        else:
            if sum(currFiles) < 100000:
                sums += sum(currFiles)
                print("currfiles are: ", currFiles)
            currFiles = []



print(sums)









# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
