
charinput = str.upper(input(("Type something: ")))

print(charinput)

charlst = list(charinput)

print(charlst)

unilist = [0] * 26

for i in range(0, len(charlst)):
    idx = charlst[i]
    numchar = (ord(idx) - 65)
    if 0 <= numchar <= 65:
        unilist[numchar] += 1


print(unilist)

for i in range(0, len(unilist)):
    if unilist[i] > 0:
        char = i + 65
        oldchar = chr(char)
        print(f"{oldchar} was found in the string {unilist[i]} times")
    



