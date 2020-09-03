import re
# P = U * I

class Resolver:
    cases = {
        "P": {
            "reg": r"\bP=\b([^\s]+)",
        },
        "U": {
            "reg": r"\bU=\b([^\s]+)",
        },
        "I": {
            "reg": r"\bI=\b([^\s]+)",
        }
    }

    def __init__(self, line):
        self.line = line

    def cleanValue(self, value):
        number = re.findall(r"\d*\.?\d+", value)
        if(len(number)):
            return float(number[0])
        return 1

    def extractValue(self, key):
        print("self.cases", self.cases[key]["reg"])
        result = re.search(self.cases[key]["reg"], self.line)
        if(result):
            return result.group()
        return None

    def calculate(self):
        P = self.extractValue("P")
        U = self.extractValue("U")
        I = self.extractValue("I")

        if(P != None and U != None):
            print("I")
            return self.cleanValue(P) / self.cleanValue(U)
        if(P != None and I != None):
            print("U")
            return self.cleanValue(P) / self.cleanValue(I)
        if(U != None and I != None):
            print("U", U)
            print("I", I)
            print("P")
            return self.cleanValue(U) * self.cleanValue(I)
        return 0

if __name__ == "__main__":
    input = "If the voltage is U=200V and the current is I=4.5A , which power is generated?"
    resolve = Resolver(input)
    print(resolve.calculate())