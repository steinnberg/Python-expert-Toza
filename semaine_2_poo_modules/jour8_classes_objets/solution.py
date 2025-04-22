# Exercice 1
class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

# Exercice 2
class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

# Exercice 3
class CompteBancaire:
    def __init__(self, proprietaire, solde_initial=0):
        self.proprietaire = proprietaire
        self.solde = solde_initial

    def depot(self, montant):
        self.solde += montant

    def retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            raise ValueError("Fonds insuffisants")

    def afficher_solde(self):
        return f"Solde de {self.proprietaire} : {self.solde} €"

# Exercice 4
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def description(self):
        return f"{self.titre} par {self.auteur} ({self.annee})"

# Exercice 5
class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        return [livre.description() for livre in self.livres]
