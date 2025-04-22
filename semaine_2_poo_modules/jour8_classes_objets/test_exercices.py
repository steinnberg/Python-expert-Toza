from solutions import (
    Personne, Rectangle, CompteBancaire,
    Livre, Bibliotheque
)

# Exercice 1 : Personne
def test_personne():
    p = Personne("Marie", "Curie")
    assert p.nom_complet() == "Marie Curie"

# Exercice 2 : Rectangle
def test_rectangle():
    r = Rectangle(5, 10)
    assert r.aire() == 50
    assert r.perimetre() == 30

# Exercice 3 : CompteBancaire
def test_compte_bancaire():
    c = CompteBancaire("Alice", 100)
    c.depot(50)
    assert c.solde == 150
    c.retrait(30)
    assert c.solde == 120
    try:
        c.retrait(200)
        assert False, "Devrait lever une exception"
    except ValueError:
        assert True

# Exercice 4 : Livre
def test_livre():
    l = Livre("1984", "George Orwell", 1949)
    assert l.description() == "1984 par George Orwell (1949)"

# Exercice 5 : Bibliothèque
def test_bibliotheque():
    biblio = Bibliotheque()
    l1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    l2 = Livre("Python Tricks", "Dan Bader", 2017)
    biblio.ajouter_livre(l1)
    biblio.ajouter_livre(l2)
    livres = biblio.afficher_livres()
    assert len(livres) == 2
    assert "Le Petit Prince par Antoine de Saint-Exupéry (1943)" in livres[0]
