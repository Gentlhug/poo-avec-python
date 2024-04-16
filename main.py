import exercice1 as ex1
import exercice2 as ex2
import exercice3 as ex3
import exercice4 as ex4
import exercice5 as ex5

if __name__ == '__main__':
    ### EXERCICE 1 ###
    #triangle = ex1.Triangle(5, 6) # initialisation du triangle
    #rectangle = ex1.Rectangle(25, 30) # Initialisation du rectangle
    #print(f"L'aire du rectangle est de : {rectangle.aire()}cm2") # Affichage de l'aire du rectangle
    #print(f"L'aire du triangle est de : {triangle.aire()}cm2") # Affichage de l'aire du triangle

    ### EXERCICE 2 ###
    #geom1 = ex2.Geometry()
    #print(geom1.distance(2, 3, 12, 14)) # Calcul de la distance d'un point A à un point B
    #print(geom1.middle([2, 3], [12, 14])) # Calcul du point médian d'un bipoint (A, B)
    #print(geom1.triangle_perimeter(3, 4, 5)) # Calcul du périmètre d'un triangle
    #print(f"Triangle 1 : {geom1.triangle_isoceles(5, 2, 3)}\nTriangle 2 : {geom1.triangle_isoceles(5, 5, 3)}") # Détermine si un triangle est isocèles ou non

    ### EXERCICE 3 ###
    #compte = ex3.CompteBancaire(25134645632, "Sandy KILOS", 100.0) # Initialisation du compte
    #compte.versement(300.0) # Ajout de 300 EUR
    #compte.retrait(52.31) # Retrait de 52.31 EUR
    #compte.agios() # Agios de 5%
    #compte.afficher() # Affiche le détail du compte

    ### EXERCICE 4 ###
    #employe1 = ex4.Employe("John Doe", 50000.0, "2012-09-01") # Initialisation de l'employé
    #manager1 = ex4.Manager("Anna Tomie", 62000.0, "2016-11-23", equipe=[employe1]) # Initialisation du manager
    #directeur1 = ex4.Directeur("Emma Sculation", 85000.0, "2009-05-12", service="Finance", equipe=[manager1]) # Initialisation du directeur
    #entreprise = ex4.Entreprise() # Initialisation de l'entreprise
    #entreprise.ajouter_employe(employe1) # Ajout de l'employé dans l'entreprise
    #entreprise.ajouter_employe(manager1) # Ajout du manageur dans l'entreprise
    #entreprise.ajouter_employe(directeur1) # Ajout du directeur dans l'entreprise
    #entreprise.afficher_employe() # Affichage des membres de l'entreprise

    ### EXERCICE 5 ###
    rect1 = ex5.Rectangle(5, 8) # Initialisation du rectangle
    print(f"Longueur du rectangle : {rect1.longueur}\nLargeur du rectangle : {rect1.largeur}") # Affichage l et L du rectangle
    print(f"Périmètre du rectangle : {rect1.perimetre()}") # Affichage du périmètre du rectangle
    print(f"Surface du rectangle : {rect1.surface()}") # Affichage de l'aire du rectangle
    rect1.largeur = 12 # Changement de largeur du rectangle
    rect1.longueur = 8 # Changement de longueur du rectangle
    print(f"Longueur du rectangle : {rect1.longueur}\nLargeur du rectangle : {rect1.largeur}") # Affichage l et L du rectangle
    print(f"Périmètre du rectangle : {rect1.perimetre()}") # Affichage du périmètre du rectangle
    print(f"Surface du rectangle : {rect1.surface()}") # Affichage de l'aire du rectangle
    parall1 = ex5.Parallelepipede(5, 8, 6) # Initialisation du parallelepipede rectangle
    print(f"Volume du parallelepipede rectangle : {parall1.volume()}") # Affichage du volume du parallelepipede rectangle

