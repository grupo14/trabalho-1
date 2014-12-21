# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 14:13:38 2014

@author: gabriel
"""

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIWWW

seq_record = SeqIO.read('genes.gb', 'gb')
proteins = []
for feature in seq_record.features:
    if feature.type == "CDS":
        seq_protein = Seq(str(feature.qualifiers['translation']), IUPAC.extended_protein)
        protein_record = SeqRecord(seq_protein)
        proteins.append(protein_record)
save_file = open('blast.xml', 'w')
for protein in proteins:
    result_handle = NCBIWWW.qblast('blastp', 'nr', protein.format('gb'))
    save_file.write(result_handle.read())
    save_file.write('\n')
save_file.close()
result_handle.close()
