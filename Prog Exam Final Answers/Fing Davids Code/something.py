def print_name(name):
    lstname = list(name)
    reset = name
    star = "**"
    ran = range(len(name))
    for i in ran:
       let = lstname[i]
       strlet = (star + let + star)
       otlet = name[i]
       newname = name.replace(otlet, strlet) 
       print(newname)
       name = reset


def main ():
    name = input("Type your first name: ")
    print_name(name)

main()