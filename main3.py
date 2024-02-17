from data.data_stock import Data_stock
from data.data_equipe import Data_equipe
from data.data_deplacement import Data_deplacement
from data.data_utilisateur import Data_utilisateur
from data.data_liste_depart import Data_liste_depart
from data.data_liste_utilisateur import Data_liste_utilisateur
from datetime import date
from gestion_compte import Gestion_compte
from gestion_liste_utilisateur import Gestion_liste_utilisateur

if __name__ == '__main__':

    test_stock = Data_stock()
    test_equipe = Data_equipe()
    test_deplacement = Data_deplacement()
    test_utilisateur = Data_utilisateur()
    test_liste_depart = Data_liste_depart()
    test_liste_utilisateur = Data_liste_utilisateur()
    gestion_liste_utilisateur = Gestion_liste_utilisateur()
    gestion_compte = Gestion_compte()

    #utilisateur


    #A-creer un compte,mettre à jour son compte


    #B-Creer une liste utilisateur


    #1-Se connecter en tant qu'utilisateur pour recuperer l'id_utilisateur

    utilisateur=gestion_compte.get_1utilisateur()

    #2-choisir une équipe pour recuperer l'id_équipe

    type_rugby=input("Rugby à 15 ou rugby à 7 ?\n")
    genre=input("Equipe masculine ou feminine ?\n")
    categorie_age=input("Quelle categorie d'âge ?\n")

    equipe=test_equipe.get_1_equipe(type_rugby,genre,categorie_age)

    #3-choisir un deplacement pour recuperer l'id_deplacement

    nombre_joueurs=input("Quel est le nombre de joueurs pendant le deplacement?\n")
    duree_deplacement=input("Quelle est la duree du deplacement?\n")

    deplacement=test_deplacement.get_1_deplacement(nombre_joueurs,duree_deplacement)

    #4-recuperer l'id de la liste_depart qui correspond à l'équipe et au deplacement

    liste_depart = test_liste_depart.get_id_liste_depart(equipe[0], deplacement[0])

    #5-entrer une destination et une date pour pouvoir identifier la liste_utilisateur que l'on va creer

    destination = input("Quelle est la destination?\n")
    date_liste = date(int(input("Entrer l'année: ")),int(input("le mois: ")),int(input("le jour: ")))


    #6-creer la liste_utilisateur et recuperer son id

    test_liste_utilisateur.create_liste_utilisateur(utilisateur[0],liste_depart[0],date_liste,destination)

    liste_utilisateur=test_liste_utilisateur.get_id_liste_utilisateur(utilisateur[0],liste_depart[0],date_liste)

    #7-pour le depart de l'utilisateur,remplir la liste_utilisateur avec les quantites de depart de la liste depart

    test_liste_utilisateur.create_association_liste_utilisateur_produit(liste_utilisateur[0], liste_depart[0])

    #8-mise à jour du stock en enlevant les quantites de depart de la liste

    rows = test_liste_utilisateur.get_liste_utilisateur(liste_utilisateur[0])

    for row in rows:

        test_stock.retirer_quantite_stock(row[5],row[3])

    #9-pour le retour de l'utilisateur,remplir la liste_utilisateur avec les quantites_retour

    print("Inventaire retour")

    i = 0
    while i < 4:

        print("Combien de", rows[i][4], "reste_il?:")

        try:

            quantite_retour = int(input())
            test_liste_utilisateur.update_liste_utilisateur(quantite_retour,liste_utilisateur[0], rows[i][3])
            i += 1

        except ValueError:
            print("Veuillez entrez un nombre")
            i = i

    print("Voici l'apercu de la liste")

    lignes=test_liste_utilisateur.get_liste_utilisateur(liste_utilisateur[0])

    #10-mise à jour du stock en ajoutant les quantité_retour après validation de l'administrateur
    #fonction valider le retour de l'utilisateur aller=False

    for ligne in lignes:

        test_stock.ajouter_quantite_stock(ligne[6],ligne[3])

    test_stock.get_stock_consommable()