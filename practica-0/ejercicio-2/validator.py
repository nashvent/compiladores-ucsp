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

    def validate(self):
        for rule in self.cases:
            validVerb = re.search(rule["re_verb"], self.verb)
            validParticiple = re.search(rule["re_participle"], self.participle)
            if(validVerb and validParticiple):
                return True
        return False

    def isValidText(self):
        if(self.validate()):
            return "SI"
        return "NO"
