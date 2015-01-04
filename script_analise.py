# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 18:21:46 2015

@author: gabriel
"""

#script para análise das proteínas

#importações
from Bio.SwissProt import KeyWList
import urllib
from Bio import SwissProt
from Bio.PDB import PDBList, PDBParser

#análise geral de proteinas (baseado no código desenvolvido pelo grupo 10)
handle = open("uniprot-mylist.txt")
records = KeyWList.parse(handle)
codes = []
review = open("proteinas_uniprot.txt", "w")
for record in records:
    review.write("\n"+record['ID']+"\n")
    review.write("\n"+record['DE']+"\n")
    codes.append(record['AC'][:-1])
review.close()

#análise individual das proteínas relevantes (baseado nos códigos desenvolvidos pelos grupos 10 e 7)
for code in codes:
    data = urllib.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt")
    while True:
         try:
             record = SwissProt.read(data)
             for ref in record.references:
                 f = open("analise_%s.txt" %code,"w")
                 f.write(str("****Informacao sobre a proteina****\n"))
                 f.write(str("\n\nNome:%s\n" %record.entry_name))
                 f.write(str("\nClasse:%s\n" %record.data_class))
                 f.write(str("\nTipo de molecula:%s\n" %record.molecule_type))
                 f.write(str("\nTamanho da sequencia:%s\n" %record.sequence_length))
                 f.write(str("\nAccession:%s\n" %record.accessions))
                 f.write(str("\nCriado:%s\n"% str(record.created)))
                 f.write(str("\nAdaptacao da sequencia:%s\n" %str(record.sequence_update)))
                 f.write(str("\nAdaptacao da anotacao:%s\n" %str(record.annotation_update)))
                 f.write(str("\nDescricao:%s\n" %record.description))
                 f.write(str("\nNome do gene:%s\n" %record.gene_name))
                 f.write(str("\nOrganismo:%s\n" %record.organism))
                 f.write(str("\nOrganelo:%s\n" %record.organelle))
                 f.write(str("\nClassificacao do Organismo:%s\n" %record.organism_classification))
                 f.write(str("\nID da taxonomia:%s\n" %record.taxonomy_id))
                 f.write(str("\nOrganismo Hospedeiro:%s\n" %record.host_organism))
                 f.write(str("\nID da taxonomia do hospedeiro:%s\n" %record.host_taxonomy_id))
                 f.write(str("\nReferencias:%s\n" %record.references))
                 f.write(str("\nComentarios:%s\n" %record.comments))
                 f.write(str("\nReferencias cruzadas:%s\n" %record.cross_references))
                 f.write(str("\nPalavras-chave:%s\n" %record.keywords))
                 f.write(str("\nCaracteristicas:%s\n" %record.features))
                 f.write(str("\nInformacao sobre a sequencia:%s\n" %str(record.seqinfo)))
                 f.write(str("\nSequencia:%s\n" %str(record.sequence)))
                 f.write(str("\n****Referencias sobre a proteina****\n"))
                 f.write(str("\nNumero:%s\n" %ref.number))
                 f.write(str("\nPosicao:%s\n" %ref.positions))
                 f.write(str("\nComentarios:%s\n" %ref.comments))
                 f.write(str("\nReferencias:%s\n" %ref.references))
                 f.write(str("\nAutores:%s\n" %ref.authors))
                 f.write(str("\nTitulo:%s\n" %ref.title))
                 f.write(str("\nLocalizacao:%s\n" %ref.location))
                 f.close()
             break
         except Exception:
             break

#análise da estrutura das proteínas relevantes com base no PDB (código baseado no desenvolvido pelo grupo 10)
