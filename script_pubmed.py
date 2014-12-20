from Bio import Entrez
from Bio import Medline

Entrez.email = "gabrielpeixoto@sapo.pt"#o e-mail é apenas um exemplo
handle = Entrez.egquery(term = "Legionella  pneumophila genome")
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
