#very basic shift fuction for lists, should be chanegd as need for the shift

def shift(list):
    temp = list[0]
    for i in range (1, len(list)):
        list[i-1]=list[i]
    list[len(list)-1] = temp