# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 17:07:30 2014

@author: gabriel
"""

#script usado para guardar a sequência pretendida e a informação a ela associada

#importações
from Bio import SeqIO
from Bio import Entrez

#abrir a sequência selecionada para o nosso grupo (genes lpg2796 a lpg3005; posições 3148911 a 3397754)
Entrez.email = "gabrielpeixoto@sapo.pt"#o e-mail é apenas um exemplo
handle = Entrez.efetch(db='nucleotide', rettype='gb', retmode='txt', id='NC_002942.5', seq_start=3148911, seq_stop=3397754)

#guardar a sequência selecionada
seq_record = SeqIO.read(handle, 'gb')
handle.close()
SeqIO.write(seq_record, 'genes.gb', 'gb')

#guardar informação relevante sobre a sequência selecionada (baseado no código desenvolvido pelo grupo 7)
intel = open('informacao_sequencia.txt', 'w')
intel.write('Registo NCBI')
intel.write('\n')
intel.write(str(seq_record))
intel.close()
