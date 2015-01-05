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
    codes.append(record['AC'][:-1])#remover ";" no final de cada código de acesso
review.close()

#análise individual das proteínas relevantes (baseado nos códigos desenvolvidos pelos grupos 10 e 7)
f = open("analise_reviewed.txt","w")
for code in codes:
    data = urllib.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt")
    while True:
         try:
             record = SwissProt.read(data)
             for ref in record.references:
                 f.write("\n****Codigo %s****\n" %code)
                 f.write("\n****Informacao sobre a proteina****\n")
                 f.write("\n\nNome:%s\n" %record.entry_name)
                 f.write("\nClasse:%s\n" %record.data_class)
                 f.write("\nTipo de molecula:%s\n" %record.molecule_type)
                 f.write("\nTamanho da sequencia:%s\n" %record.sequence_length)
                 f.write("\nAccession:%s\n" %record.accessions)
                 f.write("\nCriado:%s\n"% str(record.created))
                 f.write("\nAdaptacao da sequencia:%s\n" %str(record.sequence_update))
                 f.write("\nAdaptacao da anotacao:%s\n" %str(record.annotation_update))
                 f.write("\nDescricao:%s\n" %record.description)
                 f.write("\nNome do gene:%s\n" %record.gene_name)
                 f.write("\nOrganismo:%s\n" %record.organism)
                 f.write("\nOrganelo:%s\n" %record.organelle)
                 f.write("\nClassificacao do Organismo:%s\n" %record.organism_classification)
                 f.write("\nID da taxonomia:%s\n" %record.taxonomy_id)
                 f.write("\nOrganismo Hospedeiro:%s\n" %record.host_organism)
                 f.write("\nID da taxonomia do hospedeiro:%s\n" %record.host_taxonomy_id)
                 f.write("\nReferencias:%s\n" %record.references)
                 f.write("\nComentarios:%s\n" %record.comments)
                 f.write("\nReferencias cruzadas:%s\n" %record.cross_references)
                 f.write("\nPalavras-chave:%s\n" %record.keywords)
                 f.write("\nCaracteristicas:%s\n" %record.features)
                 f.write("\nInformacao sobre a sequencia:%s\n" %str(record.seqinfo))
                 f.write("\nSequencia:%s\n" %str(record.sequence))
                 f.write("\n****Referencias sobre a proteina****\n")
                 f.write("\nNumero:%s\n" %ref.number)
                 f.write("\nPosicao:%s\n" %ref.positions)
                 f.write("\nComentarios:%s\n" %ref.comments)
                 f.write("\nReferencias:%s\n" %ref.references)
                 f.write("\nAutores:%s\n" %ref.authors)
                 f.write("\nTitulo:%s\n" %ref.title)
                 f.write("\nLocalizacao:%s\n" %ref.location)
             break
         except Exception:
             break
f.close()

#análise da estrutura das proteínas relevantes com base no PDB (código baseado no desenvolvido pelo grupo 10)
parser = PDBParser()
a = "SIM"
while a == "SIM":
    s = raw_input ("Nome do ficheiro a analisar:")
    ficheiro= open("Resultados da %s"%s, "w")
    structure = parser.get_structure('%s'%s, '%s.pdb'%s)
    pdbl = PDBList()
    pdbl.retrieve_pdb_file('%s'%s)
    print "\nAnalise do ficheiro: %s"%(s)
    keywords = structure.header['keywords']
    ficheiro.write(keywords)
    print "\nPalavras Chave:%s"%keywords
    name = structure.header['name']
    print "\nNome do Organismo:%s"%name
    head = structure.header['head']
    print "\nCabecalho:%s"%head
    dep = structure.header['deposition_date']
    print "\nData da deposicao::%s"%dep
    dat = structure.header['release_date']
    print "\nData da publicacaos::%s"%dat
    s = structure.header['structure_method']
    print "\nMetodo usado:%s"%s
    resolution = structure.header['resolution']
    print "\nResolucao:%s"%resolution
    ref = structure.header['structure_reference']
    print "\nReferencia da estrutura:%s"%ref
    j = structure.header['journal_reference']
    print "\nReferencia de artigo:%s"%j
    a = structure.header['author']
    print "\nAutor:%s"%a
    c = structure.header['compound']
    print "\nComposto:%s\n"%c
    w = raw_input ("Existe mais algum ficheiro que deseje analisar( responda sim ou nao):")
    a = w.upper()
