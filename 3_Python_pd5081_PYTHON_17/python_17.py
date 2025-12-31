from Bio.Align import PairwiseAligner
from Bio import Entrez
from Bio import SeqIO


# Ustawienie adresu email
Entrez.email = "dominika.wojtanowska98@gmail.com"


# Wczytanie sekwencji
sekwencja_1 = Entrez.efetch(db="nucleotide", id="JX669568", rettype="fasta", retmode="text")
sekwencja_1 = SeqIO.read(sekwencja_1, "fasta")

sekwencja_2 = Entrez.efetch(db="nucleotide", id="JX669571", rettype="fasta", retmode="text")
sekwencja_2 = SeqIO.read(sekwencja_2, "fasta")


# Zapis do pliku
sekwencje = [sekwencja_1, sekwencja_2]

SeqIO.write(sekwencje, 'sekwencje.fasta', "fasta")


# Odczyt z pliku
records = list(SeqIO.parse('sekwencje.fasta', "fasta"))

seq_1 = records[0].seq
seq_2 = records[1].seq


aligner = PairwiseAligner()
aligner.mode = 'global'
alignments = aligner.align(seq_1, seq_2)

print(f"Wynik: {alignments[0].score:.1f}")
print(alignments[0]) 

