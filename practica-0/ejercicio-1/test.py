from validator_stack import Validator
file = open("input.txt", "r")
for line in file:
    clean_line = line.replace("\n","")
    validator = Validator(clean_line)
    print(clean_line, "=>",validator.isValidText())
