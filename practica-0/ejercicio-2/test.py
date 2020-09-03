from validator import Validator

file = open("input.txt", "r")
for line in file:
    line_clean = line.replace("\n","")
    words = line_clean.split(" ")
    validator = Validator(words[0], words[1])
    print(words[0], words[1], "=>",validator.isValidText())
