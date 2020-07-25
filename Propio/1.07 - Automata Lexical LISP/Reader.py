# -*- coding: utf-8 -*-
class Reader: 

    def __init__(self): pass

    def read(self):
        self.text = []

        #lee el input linea por linea y lo almacena en una lista
        try:
            text = input()
            while True:
                self.text += [text]
                text = input()

        except EOFError:
            pass 

        self.text = "\n".join(self.text)
        self.textlist = list(self.text)

        return self

    def nextchar(self):
        if( len(self.textlist) == 0 ): return None
        return self.textlist.pop(0)






