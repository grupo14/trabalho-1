from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Blast import NCBIWWW

seq_record = SeqIO.read('genes.gb', 'gb')
for feature in seq_record.features:
    if (feature.type == 'gene' or feature.type == 'CDS'):
        print feature
