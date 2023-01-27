glossary = {}
infile = open("prog final\database_terms.tsv", "r")
redfile = infile.read()
linecount = int(redfile.count("\n"))
infile.close
infile = open("prog final\database_terms.tsv", "r")
for i in range(1, linecount):
    lst= []
    output = infile.readline()
    output = output.replace("\n", " " )
    lst = output.split("\t")
    glossary[lst[0]] = lst[1]  
    # print(glossary) 

# Get term from user to lookup in glossary

value = None
while value == None:
    term = input("Enter a database term: ")
    term = term.capitalize()
    value = glossary.get(term)
    if value == None:
        print("Error try again")   
print('\n') 
print(f"{term} --- {value}")