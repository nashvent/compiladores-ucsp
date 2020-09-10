import re
import sys

def is_ip_format(str): # 0.0.0.0 -> 299.299.299.299
    regstr = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-9]{2})\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-9]{2})$"
    result = re.search(regstr, str)
    return result != None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = ''
    result = is_ip_format(str)
    print(result)