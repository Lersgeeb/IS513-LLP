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
        return str(self.variable[name])

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
    
    def catstringvar(self, name, str1):
        return "%s%s" % ( self.cleanParam( str(self.getvar(name)) ), self.cleanParam(str1))

    def plusop(self, term1, term2):

        if(
            re.match(r"^(\"[^\"]*\")|('[^']*')*$", term1) and
            re.match(r"^(\"[^\"]*\")|('[^']*')*$", term2) 
        ):
            return self.catstrings(term1, term2)

        else: 
            return self.sum(term1,term2)    

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
        



     
            
