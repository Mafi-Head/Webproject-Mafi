class Poisteny:
    """
    Trieda reprezentujúca jedného poisteného.
    Dodržiava princíp SRP (Single Responsibility Principle),
    pretože sa stará len o dáta a ich reprezentáciu.
    """

    def __init__(self, meno: str, priezvisko: str, vek: int, telefon: str):
        """
        Konštruktor pre inicializáciu poisteného.
        :param meno: Krstné meno poisteného.
        :param priezvisko: Priezvisko poisteného.
        :param vek: Vek poisteného.
        :param telefon: Telefónne číslo poisteného.
        """
        self.meno = meno
        self.priezvisko = priezvisko
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Metóda pre vytvorenie textovej reprezentácie objektu.
        Slúži na jednoduchý výpis údajov.
        """
        return (f"Meno: {self.meno} {self.priezvisko}, "
                f"Vek: {self.vek}, "
                f"Telefónne číslo: {self.telefon}")


# Súbor: spravca_poistenych.py

class SpravcaPoistenych:
    """
    Trieda pre správu kolekcie poistených.
    Zodpovedá za ukladanie, vytváranie a vyhľadávanie poistených.
    """

    def __init__(self):
        """Inicializuje prázdnu kolekciu poistených."""
        self.zoznam_poistenych = []

    def vytvor_poisteneho(self, meno: str, priezvisko: str, vek: int, telefon: str):
        """
        Vytvorí nového poisteného a pridá ho do zoznamu.
        :return: Vytvorený objekt Poisteny.
        """
        poisteny = Poisteny(meno, priezvisko, vek, telefon)
        self.zoznam_poistenych.append(poisteny)
        return poisteny

    def zobraz_vsetkych(self) -> list:
        """
        Vráti zoznam všetkých poistených.
        """
        return self.zoznam_poistenych

    def najdi_poisteneho(self, meno: str, priezvisko: str):
        """
        Vyhľadá poisteného podľa mena a priezviska.
        :return: Objekt Poisteny, ak sa nájde, inak None.
        """
        for poisteny in self.zoznam_poistenych:
            if poisteny.meno == meno and poisteny.priezvisko == priezvisko:
                return poisteny
        return None


# Súbor: aplikacia.py

class Aplikacia:
    """
    Trieda pre interakciu s používateľom (SoC - Separation of Concerns).
    Stará sa o zobrazovanie menu, spracovanie vstupov a výstupov.
    """

    def __init__(self):
        """Inicializuje inštanciu triedy SpravcaPoistenych."""
        self.spravca = SpravcaPoistenych()

    def _zadaj_meno_a_priezvisko(self) -> (str, str):
        """
        Pomocná metóda na získanie a validáciu mena a priezviska (DRY).
        Zabezpečuje, že meno ani priezvisko nie sú prázdne.
        """
        while True:
            meno = input("Zadajte meno: ").strip()
            priezvisko = input("Zadajte priezvisko: ").strip()
            if not meno or not priezvisko:
                print("Chyba: Meno ani priezvisko nemôžu byť prázdne. Skúste to znova.")
            else:
                return meno, priezvisko

    def _vytvor_poisteneho(self):
        """Logika pre vytvorenie nového poisteného."""
        print("--- Vytvorenie nového poisteného ---")
        meno, priezvisko = self._zadaj_meno_a_priezvisko()

        while True:
            try:
                vek = int(input("Zadajte vek: "))
                if vek < 0:
                    raise ValueError
                break
            except ValueError:
                print("Chyba: Vek musí byť kladné celé číslo. Skúste to znova.")

        telefon = input("Zadajte telefónne číslo: ")

        self.spravca.vytvor_poisteneho(meno, priezvisko, vek, telefon)
        print("Poistený bol úspešne pridaný.")

    def _zobraz_vsetkych_poistenych(self):
        """Logika pre zobrazenie všetkých poistených."""
        print("--- Zoznam všetkých poistených ---")
        poisteni = self.spravca.zobraz_vsetkych()
        if not poisteni:
            print("Zoznam poistených je prázdny.")
        else:
            for poisteny in poisteni:
                print(poisteny)

    def _vyhladaj_poisteneho(self):
        """Logika pre vyhľadávanie poisteného."""
        print("--- Vyhľadanie poisteného ---")
        meno, priezvisko = self._zadaj_meno_a_priezvisko()
        poisteny = self.spravca.najdi_poisteneho(meno, priezvisko)
        if poisteny:
            print("Nájdený poistený:")
            print(poisteny)
        else:
            print("Poistený s daným menom a priezviskom nebol nájdený.")

    def spusti(self):
        """
        Hlavná metóda pre spustenie aplikácie.
        Obsahuje hlavný cyklus menu.
        """
        while True:
            print("\n--- Evidencia poistenia ---")
            print("Vyberte si akciu:")
            print("1 - Vytvoriť nového poisteného")
            print("2 - Zobraziť všetkých poistených")
            print("3 - Vyhľadať poisteného")
            print("4 - Ukončiť aplikáciu")

            volba = input("Vaša voľba: ")

            if volba == "1":
                self._vytvor_poisteneho()
            elif volba == "2":
                self._zobraz_vsetkych_poistenych()
            elif volba == "3":
                self._vyhladaj_poisteneho()
            elif volba == "4":
                print("Aplikácia bola ukončená.")
                break
            else:
                print("Neplatná voľba. Skúste to znova.")


# Súbor: main.py
# Hlavný spúšťací súbor, ktorý iniciuje a spúšťa aplikáciu.
# Pre spustenie stačí spustiť tento súbor.

if __name__ == "__main__":
    app = Aplikacia()
    app.spusti()