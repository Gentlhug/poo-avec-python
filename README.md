# POO avec Python

## :dart: Description

Quelques exercices pour apprendre la programmation orientée objet avec Python.

## :book: Tous les exercices

### :pencil: Exercice n°1

```python
### EXERCICE 1 ###
triangle = ex1.Triangle(5, 6) # initialisation du triangle
rectangle = ex1.Rectangle(25, 30) # Initialisation du rectangle
print(f"L'aire du rectangle est de : {rectangle.aire()}cm2") # Affichage de l'aire du rectangle
print(f"L'aire du triangle est de : {triangle.aire()}cm2") # Affichage de l'aire du triangle
```
**Output:**
```
L'aire du rectangle est de : 750cm2
L'aire du triangle est de : 15.0cm2
```
*En savoir plus sur la création des classes dans le fichier **[exercice1.py](https://github.com/Gentlhug/poo-avec-python/blob/main/exercice1.py)**.*

### :pencil: Exercice n°2

```python
### EXERCICE 2 ###
geom1 = ex2.Geometry()
print(geom1.distance(2, 3, 12, 14)) # Calcul de la distance d'un point A à un point B
print(geom1.middle([2, 3], [12, 14])) # Calcul du point médian d'un bipoint (A, B)
print(geom1.triangle_perimeter(3, 4, 5)) # Calcul du périmètre d'un triangle
print(f"Triangle 1 : {geom1.triangle_isoceles(5, 2, 3)}\nTriangle 2 : {geom1.triangle_isoceles(5, 5, 3)}") # Détermine si un triangle est isocèles ou non
```
**Output:**
```
14.866068747318506
[7.0, 8.5]
12
Triangle 1 : False
Triangle 2 : True
```
*En savoir plus sur la création des classes dans le fichier **[exercice2.py](https://github.com/Gentlhug/poo-avec-python/blob/main/exercice2.py)**.*

### :pencil: Exercice n°3

```python
### EXERCICE 3 ###
compte = ex3.CompteBancaire(25134645632, "Sandy KILOS", 100.0) # Initialisation du compte
compte.versement(300.0) # Ajout de 300 EUR
compte.retrait(52.31) # Retrait de 52.31 EUR
compte.agios() # Agios de 5%
compte.afficher() # Affiche le détail du compte
```
**Output:**
```
N° de compte : 25134645632
Nom du propriétaire : Sandy KILOS
Solde : 330.3055
```
*En savoir plus sur la création des classes dans le fichier **[exercice3.py](https://github.com/Gentlhug/poo-avec-python/blob/main/exercice3.py)**.*

### :pencil: Exercice n°4
```python
### EXERCICE 4 ###
employe1 = ex4.Employe("John Doe", 50000.0, "2012-09-01") # Initialisation de l'employé
manager1 = ex4.Manager("Anna Tomie", 62000.0, "2016-11-23", equipe=[employe1]) # Initialisation du manager
directeur1 = ex4.Directeur("Emma Sculation", 85000.0, "2009-05-12", service="Finance", equipe=[manager1]) # Initialisation du directeur
entreprise = ex4.Entreprise() # Initialisation de l'entreprise
entreprise.ajouter_employe(employe1) # Ajout de l'employé dans l'entreprise
entreprise.ajouter_employe(manager1) # Ajout du manageur dans l'entreprise
entreprise.ajouter_employe(directeur1) # Ajout du directeur dans l'entreprise
entreprise.afficher_employe() # Affichage des membres de l'entreprise
```
**Output:**
```
Nom : John Doe
Salaire : 50000.0
Date d'embauche : 2012-09-01
Nom : Anna Tomie
Salaire : 62000.0
Date d'embauche : 2016-11-23
Nombre de membres : 1
Nom : Emma Sculation
Salaire : 85000.0
Date d'embauche : 2009-05-12
Nombre de membres : 1
Service : Finance
```
*En savoir plus sur la création des classes dans le fichier **[exercice4.py](https://github.com/Gentlhug/poo-avec-python/blob/main/exercice4.py)**.*

### :pencil: Exercice n°5

```python
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
```
**Output:**
```
Longueur du rectangle : 5
Largeur du rectangle : 8
Périmètre du rectangle : 26
Surface du rectangle : 40
Longueur du rectangle : 8
Largeur du rectangle : 12
Périmètre du rectangle : 40
Surface du rectangle : 96
Volume du parallelepipede rectangle : 240
```
*En savoir plus sur la création des classes dans le fichier **[exercice5.py](https://github.com/Gentlhug/poo-avec-python/blob/main/exercice5.py)**.*