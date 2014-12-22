# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 12:20:15 2014

@author: gabriel
"""

#script para pesquisa de bases de dados relevantes

#importações
from Bio import Entrez
from Bio import Medline
from Bio import SeqIO

seq_record = SeqIO.read('genes.gb', 'gb')
Entrez.email = "gabrielpeixoto@sapo.pt"#o e-mail é apenas um exemplo
for feature in seq_record.features:
    if feature.type == "CDS":
        title = str(feature.qualifiers["db_xref"][1].strip("GeneID:"))#pesquisa por gene da sequência
        handle = Entrez.egquery(term = title)
        record = Entrez.read(handle)
        number = 0
        for row in record["eGQueryResult"]:
            if row["DbName"]=="pubmed":
                number = row["Count"]
        handle = Entrez.esearch(db = "pubmed", term = "Legionella  pneumophila", retmax=number)
        record = Entrez.read(handle)
        idlist = record["IdList"]
        handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
        records = list(Medline.parse(handle))
        record_results = open('artigos.txt', 'w')
        for record in records:
            texts = "title: " + str(record.get("TI", "?")) + "\n" + "authors: " + str(record.get("AU", "?")) + "\n" + "source: " + str(record.get("SO", "?"))
            record_results.write(texts)
            record_results.write("\n")
record_results.close()
