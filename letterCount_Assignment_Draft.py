#This File is used to to test fuctions in scratch.
    
    
charinput = input("Type something: ")

(charinput)

str = ord(charinput)
charlst = []
for charinput in str:
    charlst.append(charinput)


print(charlst)

# print((charinput).isdigit)
# print((charlst).isdigit)

luran = range(0, len(charlst))

x = 0
for x in luran:
    idx = charlst[x]
    couidx = charlst.count(idx)
    if idx > 1:
        
    if couidx == 1:
        print(f"{charlst[x]} was only found once in this string")
    else:
        print(f"{charlst[x]} was found {charlst.count(idx)} times in this string")

# declist = int(charlst)

alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphalist2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# print(ord(charlst))

