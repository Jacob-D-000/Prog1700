



# def for_loop; 
# for x in ranx:
#     for y in rany:
#         ans = (x * y)
#         print(f"{x} * {y} = {ans}") 

Progvar = "Y"


while Progvar == "Y": 
    x = int(input("Choose a Number: "))
    y = int(input("Choose a another number: "))

    ranx = range(1, (x + 1))
    rany = range(1, (y + 1))

    for x in ranx:
        for y in rany:
            ans = (x * y)
            print(f"{x} * {y} = {ans}") 
    
    Progvar = input("If you would like to run the program again, type Y. If you would like to exit the program, type N: ")

    if Progvar == "N":
        print("Thanks for using this Multiplcation Times Tables Calculator!")
    while Progvar != "N" or Progvar != "Y":
        Progvar = input("Please try again: ")
        
print("Thanks for using this Multiplcation Times Tables Calculator!")   



