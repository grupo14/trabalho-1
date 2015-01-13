# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 14:13:38 2014

@author: gabriel
"""

#script para correr o blast, com as proteínas resultantes da sequência selecionada como querys

#importações
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML 

#registo do GI da proteína resultante de um gene da sequência selecionada
seq_record = SeqIO.read('genes.gb', 'gb')
gene = raw_input("Introduza o locus_tag do gene a pesquisar: ")
for feature in seq_record.features:
    if feature.type == "CDS" and feature.qualifiers['locus_tag'] == ['%s' %gene]:
        seq_protein = Seq(str(feature.qualifiers['translation'][-2:-2]), IUPAC.extended_protein)
        protein_record = SeqRecord(seq_protein)

#execução do blast
save_file = open('blast_%s.xml' %gene, 'w')
result_handle = NCBIWWW.qblast('blastp', 'swissprot', protein_record.format('gb'))
save_file.write(result_handle.read())
save_file.write('\n\n')
save_file.close()
result_handle.close()

#verificação dos resultados (baseado no código desenvolvido pelo grupo 1)
verify = open('blast_%s_verificacao.txt' %gene, 'w')
E_VALUE_THRESH = 0.1
result = open('blast_%s.xml' %gene,'r')
records = NCBIXML.parse(result)
for record in records:
    for alignment in record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                verify.write('****Alignment****\n')
                verify.write('sequence: %s' %alignment.title)
                verify.write('length: %i' %alignment.length)
                verify.write('e value: %f' %hsp.expect)
                verify.write(hsp.query[0:75] + '...')
                verify.write(hsp.match[0:75] + '...')
                verify.write(hsp.sbjct[0:75] + '...')
                verify.write('\n')
verify.close()
