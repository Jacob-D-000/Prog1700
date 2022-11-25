import random

def selectionsort(lst):
    for i in range(len(lst) - 1):
        currentMin, currentminindex = lst[i], i
        for j in range(i + 1, len(lst)):            
            if currentMin > lst[j]:
                currentMin, currentminindex = lst[j], j
        if currentminindex != i:
            lst[currentminindex], lst[i] = lst[i], currentMin


lst_to_sort =[]

for k in range(10):
    lst_to_sort.append(random.randint(0, 10))


print(f"Before selction sort: {lst_to_sort}")

selectionsort(lst_to_sort)

print(f"sorted list: {lst_to_sort}")