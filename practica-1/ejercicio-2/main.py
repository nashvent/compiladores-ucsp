import re
import sys

def init_with_number(str):
    regstr = r"^([0-9]+)(\w*=\w+)"
    result = re.search(regstr, str)
    return result != None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = ''

    result = init_with_number(str)
    print(result)