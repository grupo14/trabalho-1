# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 18:21:46 2015

@author: gabriel
"""

#script para análise das proteínas

#importações
from Bio import ExPASy
from Bio import SeqIO
from Bio import SwissProt
from Bio.SwissProt import KeyWList

#análise geral de proteinas (baseado no código desenvolvido pelo grupo 10)
handle = open("proteome.txt")
records = KeyWList.parse(handle)
review = open("proteinas_reviewed.txt", "w")
for record in records:
    review.write("\n"+record['ID']+"\n")
    review.write("\n"+record['DE']+"\n")
review.close()
