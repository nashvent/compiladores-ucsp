import re
import sys

subjects = [
    "me gustaria pedirle",
    "le solicito",
    "quiero pedirle"
]

def clean_result_regex(str, subject):
    return str.replace(subject,"")

def have_subject(str, subject):
    regstr = "("+subject+")([^.])+"
    result = re.search(regstr, str)
    if(result):
        return clean_result_regex(result.group(0), subject)
    return None

def examine_text(text):
    for subject in subjects:
        result = have_subject(text, subject)
        if(result):
            return result 
    return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = ''

    result = examine_text(str)
    print("Subject:",result)