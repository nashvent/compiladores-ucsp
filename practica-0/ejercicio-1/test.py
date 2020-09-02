from validator_stack import Validator
f = open("input.txt", "r")
for x in f:
    validator = Validator(x)
    print(validator.isValidText())
