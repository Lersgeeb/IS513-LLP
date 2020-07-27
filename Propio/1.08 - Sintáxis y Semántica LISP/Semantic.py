# -*- coding: utf-8 -*-
import re
from lark import Transformer, v_args

@v_args(inline=True)
class Semantic(Transformer):

    def __init__(self):
        self.variable = {}

    def sum(self, tree) :
        result = 0
        for x in tree.children:
            x = str(x)
            if re.match(r"\d+(.\d+)?\s\d+(.\d+)?", x):
                x = x.split(" ")
                result += float(x[0]) + float(x[1])
            else:
                result += float(x)
        return result

    def mul(self, tree):
        result = 0
        for x in tree.children:
            x = str(x)
            if re.match(r"\d+(.\d+)?\s\d+(.\d+)?", x):
                x = x.split(" ")
                result *= float(x[0]) + float(x[1])
            else:
                result *= float(x)
        return result

    def declarevar(self,name):
        self.variable[name] = None
    
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