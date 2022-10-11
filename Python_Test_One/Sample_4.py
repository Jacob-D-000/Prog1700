
# Enter loop settings
fahrStartString = input("Enter fahrenheit Start:")
fahrEndString = input("Enter fahrenheit End:")
fahrIncString = input("Enter fahrenheit Increment:")

# convert to float
fahrStartFLoat = float(fahrStartString)
fahrEndFLoat = float(fahrEndString)
fahrIncFLoat = float(fahrIncString)

# While Loop
# https://www.w3schools.com/python/python_while_loops.asp
fahrFloat = fahrStartFLoat
while (fahrFloat<fahrEndFLoat):
    celsiusFloat = (fahrFloat - 32) * 5 / 9
    print("fahrFloat=", fahrFloat, "     celsiusFloat=", celsiusFloat)
    fahrFloat = fahrFloat + fahrIncFLoat