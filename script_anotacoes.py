from Bio import SeqIO

seq_record = SeqIO.read('genes.gb', 'gb')
seq_gene = open('anotacoes_genes.txt', 'w')
seq_cds = open('anotacoes_CDS.txt', 'w')
for feature in seq_record.features:
    if feature.type == 'gene':
        seq_gene.write(str(feature) + '\n')
    elif feature.type == 'CDS':
        seq_cds.write(str(feature) + '\n')
seq_gene.close()
seq_cds.close()
