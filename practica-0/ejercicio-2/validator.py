import re

class Validator:
    cases = [
        {
            "re_verb": ".ar$",
            "re_participle": ".ando$",
        },
        {
            "re_verb": ".[^aeiou]er$",
            "re_participle": ".iendo$",
        },
        {
            "re_verb": ".[^aeiou]ir$",
            "re_participle": ".iendo$",
        },
        {
            "re_verb": ".[aeiou]er$",
            "re_participle": ".yendo$",
        },
        {
            "re_verb": ".[aeiou]ir$",
            "re_participle": ".yendo$",
        },
        {
            "re_verb": "reir$",
            "re_participle": "riendo$",
        },
    ]

    def __init__(self, verb, participle):
        self.verb = verb
        self.participle = participle
        print(verb, participle)

    def validate(self):
        for rule in self.cases:
            # print("rule")
            validVerb = re.search(rule["re_verb"], self.verb)
            validParticiple = re.search(rule["re_participle"], self.participle)
            # print(rule["re_verb"], validVerb)
            # print(rule["re_participle"], validParticiple)
            
            if(validVerb and validParticiple):
                return True
        return False

    def isValidText(self):
        if(self.validate()):
            return "SI"
        return "NO"
