import sys
from validator_stack import Validator


if __name__ == "__main__":  
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = ''

    validator = Validator(str)
    print(validator.isValidText())
   
