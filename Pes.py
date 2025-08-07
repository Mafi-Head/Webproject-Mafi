#Trieda Pes:

class Pes:
    def __init__(self, meno, plemeno):
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








