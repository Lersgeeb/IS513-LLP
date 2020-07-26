# -*- coding: utf-8 -*-
import re
from lark import Transformer, v_args

@v_args(inline=True)
class Semantic(Transformer):

    def __init__(self):
        self.variable = {}

    def sum(self, A, B) :
        return float(A) + float(B)

    def sub(self, A, B):
        return float(A) - float(B)
    
    def mul(self, A, B):
        return float(A) * float(B)
    
    def div(self, A, B):
        return float(A) / float(B)

    def assignvar(self,name,value):
        self.variable[name] = value

    def getvar(self, name):
        if name in self.variable.keys():
            return str(self.variable[name]) 
        return False

    def print(self, param):
        print("%s" % self.cleanParam(param))

    def cleanParam(self, param):
        if re.match(r"^((\"[^\"]*\")|('[^']*'))$", param):
            
            #reconocer caracteres especiales dentro de una cadena
            param = re.sub(r"\\n","\n" , param)
            param = re.sub(r"\\t","\t" , param)

            #print(param)
            return param[1:-1]
        return param

    def catstrings(self, str1, str2):
        return "%s%s" % (self.cleanParam(str1), self.cleanParam(str2) )

    def plusop(self, term1, term2):
        
        if type(term1) == float:
            term1 = "%s" % term1
        
        if type(term2) == float:
            term2 = "%s" % term2

        #convert  nameOfVariable to value
        if(re.match(r"^[a-zA-Z]\w*$", term1 )):
            print("dentro de termino1")
            if(self.getvar(term1)):
                term1 = self.getvar(term1)
        if(re.match(r"^[a-zA-Z]\w*$", term2 )):
            print("dentro de termino2")
            if(self.getvar(term2)):
                term2 = self.getvar(term2)


        #Si ambos son numeros ejecuta una suma aritmetica
        if( 
            re.match(r"^\d+(\.\d+)?$", term1) and
            re.match(r"^\d+(\.\d+)?$", term2)
        ):
            return self.sum(term1,term2)  
        
        else:
            return self.catstrings(term1, term2)

    def arguments(self, val1, val2):
        if(type(val2) == list ):
            parameters = val2[:]
            if(val1 in self.variable.keys()):
                val1 = self.getvar(val1)
            parameters += [val1]
        
        else:
            
            if(val1 in self.variable.keys()):
                val1 = self.getvar(val1)

            if(val2 in self.variable.keys()):
                val2 = self.getvar(val2)
            
            parameters = [val2, val1 ]
        
        return parameters

    def printf(self, strvalue, parameters):
        strList = strvalue.split("%s")
        newStr = []

        for s in strList:
            if(len(parameters) == 0):
                newStr += [s]
                break
            newStr += [s, self.cleanParam(parameters.pop())]

        print(self.cleanParam("".join(newStr)))
        



     
            
