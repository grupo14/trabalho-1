# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:52:10 2014

@author: gabriel
"""

#script para verificação das informações complementares das features da sequência (baseado no código desenvolvido pelo grupo 7)

#importações
from Bio import SeqIO

#recolher funções e tradução dos diferentes genes na sequência
record = SeqIO.read("genes.gb", "gb")
funcoes=[]
for feature in record.features:
    if feature.type == "CDS":
        if 'function' in feature.qualifiers:
            funcoes.append((feature.qualifiers["locus_tag"][0], feature.qualifiers["function"][0]))
traducao=[]
for feature in record.features:
    if feature.type=="CDS":
        traducao.append((feature.qualifiers["locus_tag"][0], feature.qualifiers["translation"][0]))

#ImprimirInformacaoRelevante
complement = open('informacao_complementar.txt', 'w')
complement.write("Gene e funcao: \n")
complement.write("Genes com funcao definida: " + str(len(funcoes)))
complement.write("\nGenes com funcao desconhecida: " + str(210-len(funcoes))+ "\n")
for funcao in funcoes:
    complement.write(str(funcao))
complement.write("\n Gene e traducao: \n")
for protein in traducao:
    complement.write(str(protein))
complement.close()
