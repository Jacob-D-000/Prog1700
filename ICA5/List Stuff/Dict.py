"""
Program: Dictionary Practice
Author: Jacob Dimoff
Date: 29/11/22
filename: dict.py
Purpose: Practice using Dictionarys
"""

a_set = {1,2,3,4,5} # use curly brackets
print(type(a_set))
musical_instruments =  { 
"Wood winds": ["oboe", "flute", "piccalo"],
"Brass": "Trumpet",
"Percussion": "Timpani"
}

print(type(musical_instruments))
print(musical_instruments)
print(musical_instruments["Wood winds"])

for key in musical_instruments:
    print(f"Key: {key:20}  Value: {musical_instruments[key]}")


print(musical_instruments.keys())
print(list(musical_instruments))
print(len(musical_instruments))
print(musical_instruments.get("Brass"))
print(musical_instruments.items())