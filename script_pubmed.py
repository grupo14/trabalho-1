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
record_results = open('artigos.txt', 'w')
handle = Entrez.egquery(term = "Legionella pneumophila")
record = Entrez.read(handle)
number = 0
for row in record["eGQueryResult"]:
    if row["DbName"]=="pubmed":
        number = row["Count"]
handle = Entrez.esearch(db = "pubmed", term = "Legionella  pneumophila philadelphia 1", retmax=number)
record = Entrez.read(handle)
idlist = record["IdList"]
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = list(Medline.parse(handle))
for record in records:
    record_results.write("title: ")
    record_results.write(str(record.get("TI", "?")))
    record_results.write("\nauthors: ")
    record_results.write(str(record.get("AU", "?")))
    record_results.write("\nsource: ")
    record_results.write(str(record.get("SO", "?")))
    record_results.write("\n\n")
record_results.close()
