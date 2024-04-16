class Employe:
    def __init__(self, nom: str, salaire: float, date_embauche: str):
        self.nom = nom
        self.salaire = salaire
        self.date_embauche = date_embauche

    def __str__(self):
        return f"Nom : {self.nom}\nSalaire : {self.salaire}\nDate d'embauche : {self.date_embauche}"

class Manager(Employe):
    def __init__(self, nom: str, salaire: float, date_embauche: str, equipe: list):
        super().__init__(nom, salaire, date_embauche)
        self.equipe = equipe

    def ajouter_membre(self, employe: Employe):
        self.equipe.append(employe)

    def __str__(self):
        return f"Nom : {self.nom}\nSalaire : {self.salaire}\nDate d'embauche : {self.date_embauche}\nNombre de membres : {len(self.equipe)}"

class Directeur(Manager):
    def __init__(self, nom: str, salaire: float, date_embauche: str, equipe: list, service: str):
        super().__init__(nom, salaire, date_embauche, equipe)
        self.service = service

    def __str__(self):
        return f"Nom : {self.nom}\nSalaire : {self.salaire}\nDate d'embauche : {self.date_embauche}\nNombre de membres : {len(self.equipe)}\nService : {self.service}"

class Entreprise:
    def __init__(self):
        self.list_employe = []

    def ajouter_employe(self, employe: Employe):
        self.list_employe.append(employe)

    def retirer_employe(self, nom: str):
        self.list_employe.remove(nom)

    def afficher_employe(self):
        for employe in self.list_employe:
            print(employe)