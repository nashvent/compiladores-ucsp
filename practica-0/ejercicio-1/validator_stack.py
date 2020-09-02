from collections import deque 

class Validator:
    valid_chars = {
        "{": {"required": None},
        "}": {"required": "{"},
        "[": {"required": None},
        "]": {"required": "["},
        "(": {"required": None},
        ")": {"required": "("}
    }

    def __init__(self, str):
        self.counter = deque()
        self.str = self.cleanString(str)
        self.is_break = False

    def cleanString(self, str):
        clean_str = str.replace(" ", "")
        clean_str = clean_str.replace("\n", "")
        return clean_str

    def insert(self, key):
        if(self.valid_chars.get(key)):
            item = self.valid_chars[key]
            if( item["required"] is None):
                self.counter.append(key)
                return True
            else:
                if(len(self.counter)>0):
                    stack_item = self.counter.pop()
                    if(stack_item ==  item["required"]):
                        return True
                    else:
                        self.counter.append(stack_item)
        return False                    

    def insertAll(self):
        for key in self.str:
            result = self.insert(key)
            if(result == False):
                self.is_break = True
                break

    def isValid(self):
        self.insertAll()
        # print("counter", self.counter)        
        if (len(self.counter) == 0 and self.is_break == False):
            return True
        return False
    
    def isValidText(self):
        if(self.isValid()):
            return "SI"
        return "NO"