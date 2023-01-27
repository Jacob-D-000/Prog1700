def print_name(x):
    star = "**"
    ran = range(len(x))
    for i in ran:
       let = x[i]
       upperlet = let.upper()
       strlet = (star + upperlet + star)
       newname = x.replace(let, strlet) 
       print(newname)

name = "Jacob"
print_name(name)
