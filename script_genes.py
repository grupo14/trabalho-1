from Bio import SeqIO
from Bio import Entrez

Entrez.email = "gabrielpeixoto@sapo.pt"#o e-mail é apenas um exemplo
handle = Entrez.efetch(db='nucleotide', rettype='gb', retmode='txt', id='NC_002942.5', seq_start=3148911, seq_stop=3397754)
seq_record = SeqIO.read(handle, 'gb')
handle.close()
SeqIO.write(seq_record, 'genes.gb', 'gb')
