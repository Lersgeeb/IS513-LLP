import sys,re

class TokenParser:

    def __init__(self): pass

    def read(self):
        params = sys.argv[1:]
        if(len(params) != 1): quit("Error: No se ha definido el programa a ejecutar")  
        
        self.filename = params[0]
        f = open(self.filename,"r")
        self.text = f.read()
        f.close()

        return self

    