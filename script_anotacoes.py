# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 14:47:43 2014

@author: gabriel
"""

#script para análise e validação das anotações da sequência selecionada, nomeadamente as features do tipo "gene" ou "CDS"

#importações
from Bio import SeqIO

#selecionar e guardar as features do tipo "gene", CDS" ou outros em ficheiros .txt separados (a lista é demasiado extensa para ser visível na consola)
seq_record = SeqIO.read('genes.gb', 'gb')
seq_gene = open('anotacoes_genes.txt', 'w')
genes =[]
seq_cds = open('anotacoes_CDS.txt', 'w')
cds = []
seq_outras = open('anotacoes_outras.txt', 'w')
outras = []
for feature in seq_record.features:
    if feature.type == 'gene':
        seq_gene.write(str(feature) + '\n')
        genes.append(feature.location)
    elif feature.type == 'CDS':
        seq_cds.write(str(feature) + '\n')
        cds.append(feature.location)
    else:
        seq_outras.write(str(feature) + '\n')
        outras.append(feature.location)
seq_gene.close()
seq_cds.close()
seq_outras.close()

#validação de features de acordo com a tabela fornecida no enunciado (baseado no código desenvolvido pelo grupo 7)
f = open("ProteinTable416_166758.txt", 'r')#tabela retirada de http://www.ncbi.nlm.nih.gov/genome/proteins/416?genome_assembly_id=166758
table=[]
for line in f.readlines():
    table.append(line.split('\t'))
f.close()
CDS_proteinID = []
CDS_geneID = []
for feature in seq_record.features:
    if feature.type == "CDS":
        CDS_proteinID.append(feature.qualifiers["protein_id"][0])
        CDS_geneID.append(feature.qualifiers["db_xref"][1].strip("GeneID:"))
valido = True
invalids = []
for i in xrange(3148911, len(table)):
    if ((table[i][5] != CDS_geneID[i-3148911]) or (table[i][8] != CDS_proteinID[i-3148911])):
        valido=False
        invalids.append(i)

#guardar análise e validação (código baseado no desenvolvido pelo grupo 7)
valid = open('analise_validacao.txt', 'w')
valid.write('Analise das features \n')
valid.write('Numero de genes: ' + str(len(genes)))
valid.write(' Locais: ' + str(genes) + '\n')
valid.write('Numero de CDS: ' + str(len(cds)))
valid.write(' Locais: ' + str(cds) + '\n')
valid.write('Numero de outras features: ' + str(len(outras)))
valid.write(' Locais: ' + str(outras))
valid.write('\n Validacao: ')
if valido:
    valid.write('Todas as features foram validadas com sucesso')
else:
    valid.write('Existem features invalidas nas posicoes ' + str(invalids))
valid.close()
