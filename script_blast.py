from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIWWW

seq_record = SeqIO.read('genes.gb', 'gb')
translated = seq_record.seq.translate(table='Bacterial')
proteins = []
protsAtuais = []
for aa in translated:
    if aa == "_":
        if protsAtuais:
            for p in protsAtuais:
                proteins.append(SeqRecord(Seq(p, IUPAC.IUPACProtein)))
            protsAtuais = []
        else:
            if aa == "M":
                protsAtuais.append("")
            for i in xrange(len(protsAtuais)):
                protsAtuais[i] += aa
for j in xrange(len(proteins)):
    record = SeqIO.read(proteins[j], format == 'gb')
    result_handle = NCBIWWW.qblast('blastp', 'nr', record.format('gb'))
    name_protein = 'blast_gene_' + str(j) + '.xml'
    save_file = open(name_protein, 'w')
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()
