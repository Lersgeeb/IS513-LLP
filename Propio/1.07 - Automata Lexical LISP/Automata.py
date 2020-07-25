from Token import Token

class Automata:
    def __init__(self, reader): 
        self.reader = reader

    def run(self):
        
        r = self.reader
        tokens = []

        char = r.nextchar()
        token = None
        
        while(char):
            token, repeat = self.tokenCreator(char, token)

            if token.formed:
                tokens += [token]

            if not repeat:
                char = r.nextchar()

        self.tokens = tokens
        return self

    
    def tokenCreator(self, char, token):

        repeatChar = None
        
        if not token or token.formed:
            token = Token()

        charCode = ord(char)
    
        # Comment
        if not token.inFormation and self.is_semicolon(charCode) :
            token.formed = False
            token.inFormation = True
            token.type = "COMMENT"
            token.add(charCode)
        
        elif token.inFormation and self.is_semicolon(token.atFirst()):
            if self.is_newLine(charCode):
                token = Token()
            else:
                pass
        
        # Quote String
        elif not token.inFormation and self.is_quote(charCode) :
            token.formed = False
            token.inFormation = True
            token.type = "STRING"
            token.add(charCode)
        
        elif token.inFormation and self.is_quote(token.atFirst()):
            if self.is_quote(charCode):
                token.add(charCode)
                token.inFormation = False
                token.formed = True
            else:
                token.add(charCode)     

        # DoubleQuote String
        elif not token.inFormation and self.is_doubleQuote(charCode) :
            token.formed = False            
            token.inFormation = True
            token.type = "STRING"
            token.add(charCode)
        
        elif token.inFormation and self.is_doubleQuote(token.atFirst()):
            if self.is_doubleQuote(charCode):
                token.add(charCode)
                token.inFormation = False
                token.formed = True
            else:
                token.add(charCode)

        # Arithmetic Operator
        elif not token.inFormation and self.is_arithmeticOp(charCode):
            token.add(charCode)
            token.inFormation = False
            token.formed = True
            token.type = "ARITHMETIC_OP"

        # Identifier
        elif not token.inFormation and self.is_alpha(charCode):
            token.add(charCode)
            token.inFormation = True
            Token.Formed = False
            token.type = "IDENT"

        elif token.inFormation and self.is_alpha(token.atFirst()):
            if self.is_alpha(charCode) or self.is_digit(charCode):
                token.add(charCode)
            else:
                token.inFormation = False
                token.formed = True  
                repeatChar = True

        return (token, repeatChar)
    
    
    def is_semicolon(self, charCode):
        if charCode == 59: return True
        return False

    def is_newLine(self, charCode):
        if charCode == 10: return True
        return False

    def is_quote(self, charCode):
        if charCode == 39: return True
        return False
    
    def is_doubleQuote(self, charCode):
        if charCode == 34: return True
        return False


    def is_arithmeticOp(self, charCode):
        if(
            charCode == 47 or # /
            charCode == 42 or # *
            charCode == 45 or # -
            charCode == 43 # +
        ): 
            return True
        return False

    def is_alpha(self, charCode):
        if(
            (charCode >= 65 and charCode <= 90) or # A-Z
            (charCode >= 97 and charCode <= 122) or # a-z
            (charCode == 45) # -
        ):
            return True
        return False

    def is_digit(self, charCode):
        if (charCode >= 48 and charCode <= 57): # 0-9
            return True
        return False
            

    def is_asterisk(self, charCode):
        if charCode == 42:
            return True
        return False