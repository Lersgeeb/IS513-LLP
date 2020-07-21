class Reader: 

    def __init__(self): pass

    def read(self):
        self.text = []

        try:
            text = input()
            while True:
                self.text += [text]
                text = input()
        
        except EOFError:
            pass

        self.text = "\n".join(self.text)
        return self

    def run(self):
        text = self.text
        for i in range(len(text)):
            print("The Letter '%s' at position '%d'" % (text[i], i))

        return self




'''
r = ( Reader() ).read()
print("hola")
print(r.text)
print("adios")
'''