import sys

class Reader:

    def __init__(self): pass
        
    #Lee un archivo y cada caracter lo transforma en un elemento de una lista
    def read(self):
        params = sys.argv[1:]
        if(len(params) != 1): quit("Error: No se ha definido el programa a ejecutar")    
        self.filename = params[0]
        
        f = open(self.filename, 'r')
        text = f.read()
        f.close()
        #text = ("%s".strip() % text).strip()

        self.charList = list(text)
        
        return self

    #retorna el siguiente caracter del primer elemento de la lista de caracteres y lo borra
    def nextChar(self):
        if len(self.charList) > 0:
            return self.charList.pop(0)
        else:
            return False


