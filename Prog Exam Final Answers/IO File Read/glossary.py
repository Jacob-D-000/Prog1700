glossary = {}

menu_options = {
    1: 'Define Database Term',
    2: 'List All Terms in Glossary',
    3: 'Show Defintions by Letter',
    4: 'Show All Definitions',
    5: 'Add New Term',
    6: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print(f'{key}. {menu_options[key]}')

def read_tsv_to_dict():
    infile = open("database_terms.tsv", "r")
    redfile = infile.read()
    linecount = int(redfile.count("\n"))
    infile.close
    infile = open("database_terms.tsv", "r")
    for i in range(1, (linecount + 1)):
        lst= []
        output = infile.readline()
        output = output.replace("\n", " " )
        lst = output.split("\t")
        glossary[lst[0]] = lst[1]  
        # print(glossary)
    return glossary

def lookup_term(term):
    value = glossary.get(term) 
    return value

def get_definition():
    # Get term from user to lookup in glossary
    value = None
    try:
        term = input("Enter a database term: ")
        term = term.capitalize()
        value = lookup_term(term)
        print('\n') 
        print(f"{term} \nDefinition:{value}")
    except value == None:
        print("Error try again")   
    # an empty line will help the output look less crowded
    # How should I format the output so it will be something like "term - definition"?

def list_all_terms():
    print()
    col = 1
    for k in glossary.keys():
        if col == 1:
            print(f'{k:40}', end='\t')
            col = 2
        else:
            print(f'{k}', end='\n')
            col = 1
    print()

def list_terms_by_alpha():
    letter = get_alpha()
    print('\n',letter,'\n---')
    for term in glossary.keys():
        if term[0] == letter:
            key = lookup_term(term)
            print(f"{term} \nDefinition:{key} \n")
            

def get_alpha():
    l = input('Enter a Letter: ')
    return l.upper()

def list_all():
    for i in glossary:
        key = glossary[i]
        print(f"{i} -- {key}")

def add_term():
    termtup = get_new() 
    new_term =  termtup[0]
    new_def = termtup[1]
    new_ln = (f"\n{new_term}\t{new_def}")
    infile = open("database_terms.tsv", "a")
    infile.write(new_ln)
    infile.close

def get_new():
    new_term = input('Enter a new term: ')
    new_def = input('Enter the definition for {}: '.format(new_term))
    return new_term, new_def

def main():
    read_tsv_to_dict()
    cont = True
    while(cont):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Not a valid number.')
        if option == 1:
           get_definition()
        elif option == 2:
            list_all_terms()
        elif option == 3:
            list_terms_by_alpha()
        elif option == 4:
            list_all()
        elif option == 5:
            add_term()
        elif option == 6:
            print('Thanks for using Database Glossary!')
            cont = False
        else:
            print('Invalid option. Please enter a number between 1 and 5.')
    exit()

if __name__ == "__main__":
    main()
