# User Input
# https://www.w3schools.com/python/python_user_input.asp
# Enter your name inside the running program window
loopMaxString = input("Enter loop max:")
print("loopMaxString is: " + loopMaxString)

# Casting
# https://www.w3schools.com/python/python_casting.asp
loopMaxInt = int(loopMaxString)
for loopVar in range(int(loopMaxInt)):
    print("loopVar = ", loopVar)