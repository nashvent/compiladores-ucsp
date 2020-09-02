class Validator:
    valid_chars = {
        "{": 1,
        "}": -1,
        "[": 1,
        "]": -1
    }

    position_chars = {
        "{": "{}",
        "}": "{}",
        "[": "[]",
        "]": "[]"
    }

    def __init__(self, str):
        self.counter = {}
        self.str = str.strip()
        self.insertAll()

    def insert(self, key):
        position = self.position_chars[key]
        if(self.counter.get(position)):
            self.counter[position] += self.valid_chars[key]
        else:
            self.counter[position] = self.valid_chars[key]

    def insertAll(self):
        for key in self.str:
            self.insert(key)

    def isValid(self):
        if (len(self.counter) == 0):
            return False

        for key in self.counter:
            if(self.counter[key] != 0):
                return False
        return True
    
    def isValidText(self):
        if(self.isValid()):
            return "SI"
        return "NO"