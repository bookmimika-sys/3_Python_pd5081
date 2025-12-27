# klasa Organizm
class Organizm:
    def __init__(self, nazwa, rodzaj):
        self.nazwa = nazwa
        self.rodzaj = rodzaj

    def opisz(self):
        return f"To organizm o nazwie " + self.nazwa + " i rodzaju " + self.rodzaj
    
    def transkrybuj(sekwencja_dna):
        return sekwencja_dna.replace("T", "U") 

# klasa Bakteria
class Bakteria(Organizm):
    def __init__(self, nazwa, rodzaj, kształt):
        super().__init__(nazwa, rodzaj)
        self.kształt = kształt

    def opisz(self):
        return super().opisz() + f" i kształcie " + self.kształt


bakteria_1 = Bakteria("bakteria 1", "tlenowe", "spirala")
bakteria_2 = Bakteria("bakteria 2", "beztlenowe", "laseczka")

print(bakteria_1.opisz())
print(bakteria_2.opisz())


print(Bakteria.transkrybuj("TTGCCCCAATGAACT"))