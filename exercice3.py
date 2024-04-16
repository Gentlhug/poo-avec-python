class CompteBancaire:
    def __init__(self, numeroCompte: int, nom: str, solde: float):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def versement(self, amount: float):
        self.solde += amount

    def retrait(self, amount: float):
        if amount > self.solde:
            raise ValueError("Retrait impossible, solde insuffisant.")
        self.solde -= amount

    def agios(self):
        agios = self.solde * 5 / 100
        self.solde -= agios

    def afficher(self):
        print("N° de compte :", self.numeroCompte)
        print("Nom du propriétaire :", self.nom)
        print("Solde :", self.solde)