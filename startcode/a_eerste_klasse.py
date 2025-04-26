class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")


Kat = Dier("Kat", 'Meow')
Hond = Dier("Hond", 'Bark')
Koe = Dier("Koe", 'Moe')

Kat.maak_geluid()
Hond.maak_geluid()
Koe.maak_geluid()