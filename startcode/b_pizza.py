class Pizza:
    def __init__(self, naam, grootte, prijs, toppings, prijs_toppings, geen_hawai):
        self.naam = naam
        self.grootte = grootte
        self.prijs = prijs
        self.toppings = toppings
        self.prijs_toppings = prijs_toppings
        self.geen_hawai = geen_hawai

    def toon_informatie(self):
        print(f"Naam: {self.naam}")
        print(f"Grootte: {self.grootte}")
        print(f"Prijs: {self.prijs}")
        print(f"Extra Toppings: {self.toppings}")
        print(f"Prijs per extra Toppings: {self.prijs_toppings}")
        print(f"GEEN HAWAI: {self.geen_hawai}")

    def bereken_prijs(self):
        basisprijs = 0.0
        if self.grootte == "small":
            basisprijs = 8.99
        if self.grootte == "medium":
            basisprijs = 10.99
        if self.grootte == "large":
            basisprijs = 12.99
        basisprijs += len(self.toppings) * 1.50
        return basisprijs



pizza1 = Pizza("Margherita", "medium", "10.99" ,["kaas", "tomatensaus"],"1.50 €", " Of je bent een schade voor het leven.")
pizza2 = Pizza("Margherita", "large", "12.99", ["kaas", "tomatensaus"], "1.50 €", " Of je bent een schade voor het leven. ")
pizza3 = Pizza("Margherita", "small", "8.99", ["kaas", "tomatensaus"], "1.50 €",  " Of je bent een schade voor het leven.")


pizza3.toon_informatie()
pizza1.toon_informatie()
pizza2.toon_informatie()



pizza3.bereken_prijs()
pizza1.bereken_prijs()
pizza2.bereken_prijs()


