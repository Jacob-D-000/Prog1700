import decimal

print("Bob Said, \"hello world\".\nHi Bobo ")
print('Bob said', "Hello world")
phrase = "Hello world"
print(f'bob said, {phrase}.')

width = 10
precision = 4
value = decimal.Decimal("12.34567")
mystring = f"result: {value:{5}.{precision}}"
print(mystring)