f = open("n.txt", "r")
f = f.readlines()
for i in f:
    for j in i:
        print(ord(j))
    break
