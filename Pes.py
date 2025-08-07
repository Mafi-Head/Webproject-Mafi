#Trieda Pes:

class Pes:
    def __init__(self, meno, plemeno): # __init__ na nastavenie vlastností objektu!!!
        self.meno = meno
        self.plemeno = plemeno

    def stekaj(self):
        print(f"{self.meno}: Hav-hav!")

    def predstav_sa(self):
        print(f"Ahoj! Som {self.meno} a som {self.plemeno}.")


# Použitie:

pes1 = Pes("Rex", "nemecký ovčiak")
pes2 = Pes("Benny", "jazvecik")

pes1.predstav_sa()
pes1.stekaj()

pes2.predstav_sa()
pes2.stekaj()

# Rozsirenie: Pridaj vlastnosť vek a metódu oslav_narodeniny(), ktorá vek zvýši o 1.

# Trieda Pes:

# Definujeme triedu Pes – šablónu pre vytváranie psov.

class Pes:
    def __init__(self, meno, plemeno, vek): # __init__ na nastavenie vlastností objektu!!!
        self.meno = meno
        self.plemeno = plemeno
        self.vek = vek

    def stekaj(self):
        print(f"{self.meno}: Hav-hav!")

    def predstav_sa(self):
        print(f"Ahoj! Som {self.meno} a som {self.plemeno}.")

    def oslav_narodeniny(self):
        self.vek += 1
        print(f"{self.meno}: Ma narodeniny! Ma uz {self.vek} rokov.")


# Použitie:

pes1 = Pes("Rex", "nemecký ovčiak",7)

pes1.predstav_sa()
pes1.stekaj()

pes1.oslav_narodeniny()
pes1.predstav_sa()









