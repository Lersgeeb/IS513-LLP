# -*- coding: utf-8 -*-

from lark import Lark, Transformer 
from Reader import Reader
from Semantic import Semantic
from Grammar import *

reader = (Reader()).read()

parser = Lark( grammar, parser="lalr", transformer = Semantic() )
language = parser.parse
sample = reader.text

try:
    language(sample)
except Exception as e:
    print ("Error: %s" % e)
