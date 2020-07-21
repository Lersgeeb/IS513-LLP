class Token:

    def __init__(self):
        self.formed = False
        self.inFormation = False
        self.value = []
        self.type = None

    def info(self):
        return (
            "".join(list(map(lambda x: chr(x), self.value))),
            self.type
        )

    def atFirst(self):
        if len(self.value) == 0: return None
        return self.value[0]

    def add(self, value):
        self.value += [value]
