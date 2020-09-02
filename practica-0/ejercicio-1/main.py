import sys
from validator import Validator


if __name__ == "__main__":  
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = ''

    validator = Validator(str)
    print(validator.isValidText())
   
