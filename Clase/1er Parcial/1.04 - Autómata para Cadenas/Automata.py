from Token import  Token

class Automata:

    def __init__(self, reader): 
        self.reader = reader

    def run(self):

        text = self.reader.text
        tokens = []
        
        i = 0
        token = None
        while(i < len(text)):

            i, token = self.tokenCreator(text, i, token)
    
            if token.formed:
                tokens += [token] 

        self.tokens = tokens
        return self

    # /"[^"]*"/
    def tokenCreator(self, text, i, token=None):

        if not token or token.formed:
            token = Token()

        char, pos = ord(text[i]), i

        #Formar nuevas cadenas
        if( 
            not token.inFormation and 
            self.is_quote(char) 
        ):
            token.add(char)
            token.inFormation = True
            token.formed = False
            token.type = "string"

        elif( token.inFormation ):
            if( 
                self.is_quote(token.atFirst()) and
                not self.is_quote(char)
            ):
                token.add(char)
            else:
                    token.add(char)
                    token.formed = True
        else:
            token = Token()

        pos += 1
        return (pos, token)


    def is_quote(self, char):
        if(char == 34):
            return True
        return False