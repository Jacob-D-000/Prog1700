
# User Input
# https://www.w3schools.com/python/python_user_input.asp
# Enter your name inside the running program window
fahrString = input("Enter fahrenheit:")

# Casting
# https://www.w3schools.com/python/python_casting.asp
fahrFloat = float(fahrString)
celsiusFloat = (fahrFloat - 32) * 5/9
print("fahrFloat=", fahrFloat, "     celsiusFloat=",celsiusFloat)
