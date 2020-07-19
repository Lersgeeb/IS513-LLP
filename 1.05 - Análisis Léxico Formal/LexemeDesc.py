class LexemeDesc:

    def __init__(self):
        self.countlexem = 0

    def isKeyword(self, ident):
        keyword = { 
            'auto', 'double', 'int', 'struct',
            'break', 'else', 'long', 'switch',
            'case', 'enum', 'register', 'typedef',
            'char', 'extern', 'return', 'union',
            'const', 'float', 'short', 'unsigned',
            'continue', 'for', 'signed', 'void',
            'default', 'goto', 'sizeof', 'volatile',
            'do', 'if', 'static', 'while',
            'asm', 'bool', 'catch', 'class',
            'const_cast', 'delete', 'dynamic_cast', 'explicit',
            'export', 'false', 'friend', 'inline',
            'mutable', 'namespace', 'new', 'operator', 
            'private', 'protected', 'public', 'reinterpret_cast',
            'static_cast', 'template', 'this', 'throw',
            'true', 'try', 'typeid', 'typename', 
            'using', 'virtual', 'wchar_t','include', 'cout', 'cin'
        }

        if(ident in keyword):
            self.countlexem +=  1
            return [self.countlexem, 'IDENT' , 'Palabra reservada', ident]
        else:
            self.countlexem +=  1
            return [self.countlexem, 'IDENT' , 'Identificador de Usuario', ident]
    
    def operator(self, operator):
        operatorDesc = {
            '+': 'Operador aritmético de Suma.',
            '-': 'Operador aritmético de Resta.',
            '*': 'Operador aritmético de Multiplicación.',
            '/': 'Operador aritmético de División.',
            '%': 'Operador aritmético de Modulo.',
            '++': 'Operador aritmético de Aumento.',
            '--': 'Operador aritmético de Decremento.',
        }

        if(operator in operatorDesc.keys()):
            self.countlexem +=  1
            return [self.countlexem, 'Operador' , operatorDesc[operator], operator]
        else:
            return False

    def conditionAssign(self, conditionAssign):
        conditionAssignDesc = {
            '==': 'Operador Condicional de comparación.',
            '<=': 'Operador Condicional de menor igual que.',
            '>=': 'Operador Condicional de mayor igual que.',
            '!=': 'Operador Condicional de diferencia.',
            '<': 'Operador Condicional de menor que.',
            '>': 'Operador Condicional de mayor que.',
            '=': 'Símbolo de asignación.',
            '>>': 'Símbolo de iostream de salida.',
            '<<': 'Símbolo de iostream de entrada.',
        }
    
        if(conditionAssign in conditionAssignDesc.keys()):
            self.countlexem +=  1

            if (conditionAssign == '=') or (conditionAssign == '<<') or (conditionAssign == '>>'):
                return [self.countlexem, 'Símbolo' , conditionAssignDesc[conditionAssign] , conditionAssign]
            else:
                return [self.countlexem, 'Operador' , conditionAssignDesc[conditionAssign] , conditionAssign]
        
        else:
            return [False]
    
    def classToken(self, classToken):
        classTokenDesc = {
            '::':"Símbolo de identificador de función.",
            ':':"Símbolo de definición de función.",
        }
        
        if(classToken in classTokenDesc.keys()):
            self.countlexem += 1
            return [self.countlexem, 'Símbolo' , classTokenDesc[classToken], classToken]
        else:
            return [False]

    def lookup(self, lookup):
        lookupDesc = {
            ';':"Símbolo Fin de instrucción.",
            '{':"Símbolo de apertura de statements.",
            '}':"Símbolo de finalización de statements.",
            '(':"Símbolo de inicio de agrupación.",
            ')':"Símbolo de fin de agrupación.",
            '#':"Símbolo de importe.",
            ',':"Símbolo de Separación.",
            '.':"Símbolo de identificador de Método.",
        }
        
        if(lookup in lookupDesc.keys()):
            self.countlexem += 1
            return [self.countlexem, 'Símbolo' , lookupDesc[lookup], lookup]
        else:
            return [False]

    def stringDesc(self, stringLex):
        self.countlexem += 1 
        return [self.countlexem, 'STRING' , "Token Cadena de caracteres", stringLex]  
    
    def floatDesc(self, floatLex):    
        self.countlexem += 1 
        return [self.countlexem, 'LIT_FLOAT' , "Token para numeros flotantes Literales", floatLex]  
    
    def intDesc(self, intLex):
        self.countlexem += 1 
        return [self.countlexem, 'LIT_INT' , "Token para numeros enteros Literales", intLex]  

