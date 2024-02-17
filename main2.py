from business.components.gestion_compte import Gestion_compte
from business.components.gestion_deplacement import Gestion_deplacement
from business.components.gestion_equipe import Gestion_equipe
from business.components.gestion_stock import Gestion_stock
from business.components.gestion_liste_depart import Gestion_liste_depart
from business.components.gestion_liste_utilisateur import Gestion_liste_utilisateur
from data.data_administrateur import Data_administrateur
from data.data_liste_utilisateur import Data_liste_utilisateur
from datetime import date

if __name__ == '__main__':


    gestion_compte=Gestion_compte()
    gestion_deplacement=Gestion_deplacement()
    gestion_equipe=Gestion_equipe()
    gestion_liste_depart=Gestion_liste_depart()
    gestion_stock=Gestion_stock()
    gestion_liste_utilisateur = Gestion_liste_utilisateur()
    data_administrateur=Data_administrateur()
    data_liste_utilisateur=Data_liste_utilisateur()

    #Acceuil,connexion

    print("Acceuil")

    data_administrateur.create_compte_administrateur("faure","romain","romain.faure@ffr.fr","bal")

    connexion=input("Entrer vos identifiants taper 1 pour creer un compte taper 2")

    if connexion=="1":

        print("Entrer vos identifiants")
        gestion_compte.utilisateur.nom = input("nom")
        gestion_compte.utilisateur.prenom = input("prenom")
        gestion_compte.utilisateur.mail = input("mail:")
        gestion_compte.utilisateur.mot_de_passe = input("mot_de_passe")
        gestion_compte.create()

    else:

        print("Entrer vos identifiants")
        gestion_compte.utilisateur.mail=input("mail:")
        gestion_compte.utilisateur.mot_de_passe=input("mot_de_passe")
        gestion_compte.verifier_identifiant()

        if gestion_compte.utilisateur.is_admin:

        #administrateur

            print("Administrateur")

        #A-Gestion des comptes

            option_administrateur=input("Choisir option:1,2,3,4")

        #1-gerer les comptes

            if option_administrateur=="1":

                option_gestion_compte=input("Choisir option 1,2,3")

                if option_gestion_compte=="1":

                #consulter les comptes utilisateurs

                        gestion_compte.get_all()

                elif option_gestion_compte=="2":

                #modifier un compte utilisateur

                    gestion_compte.utilisateur.nom=input("nom:")
                    gestion_compte.utilisateur.prenom=input("prenom:")
                    gestion_compte.utilisateur.mail=input("mail:")
                    gestion_compte.utilisateur.mot_de_passe=input("mot_de_passe:")
                    gestion_compte.update()

                elif option_gestion_compte=="3":

                #supprimer un compte utilisateur

                    gestion_compte.utilisateur.id=input("id_utilisateur")
                    gestion_compte.delete_1_utilisateur()


        #B-Gestion du stock

            if option_administrateur=="2":

                option_gestion_stock = input("Choisir option 1,2,3,4")

                if option_gestion_stock=="1":

                #1-Consulter les stocks

                    gestion_stock.get_all()
                    gestion_stock.get_1()

                elif option_gestion_stock=="2":

                #2-Rechercher un produit

                    premieres_lettres=input("Taper les 2 premieres lettres du produit recherché:")
                    gestion_stock.get_1_produit(premieres_lettres)
                    gestion_stock.produit.id=input("Entrer l'id_produit")
                    gestion_stock.get_stock_1_produit()

                elif option_gestion_stock=="3":

                #3-mettre à jour les quantités en stock

                    nombre_ajoute=input("Quantité à ajouter:")
                    premieres_lettres = input("Taper les 2 premieres lettres du produit recherché:")
                    gestion_stock.get_1_produit(premieres_lettres)
                    gestion_stock.produit.id = input("Entrer l'id_produit")
                    gestion_stock.ajouter_quantite_stock(nombre_ajoute)

                elif option_gestion_stock=="4":

                #4-ajouter de nouveaux produits dans le stocks

                    gestion_stock.produit.nom=input("nom_produit:")
                    gestion_stock.produit.id=input("id_stock")
                    gestion_stock.produit.quantite_en_stock=input("quantite:")
                    gestion_stock.update()


        #C-Gestion des liste_depart

            elif option_administrateur=="3":

                option_gestion_liste_depart=input("Choisir une option 1,2")

                if option_gestion_liste_depart=="1":

                #creer une nouvelle liste depart

                    #1-choisir une équipe pour recuperer un id_equipe

                    gestion_equipe.equipe.type_rugby = input("Rugby à 15 ou rugby à 7 ?\n")
                    gestion_equipe.equipe.genre = input("Equipe masculine ou feminine ?\n")
                    gestion_equipe.equipe.categorie_age = input("Quelle categorie d'âge ?\n")

                    gestion_liste_depart.equipe.id = gestion_equipe.get_1()

                    #2-creer un deplacement pour recuperer un id_deplacement si il existe déjà, reprendre l'id_existant.

                    gestion_deplacement.deplacement.nombre_joueurs = input("Quel est le nombre de joueurs pendant le deplacement?\n")
                    gestion_deplacement.deplacement.duree_deplacement = input("Quelle est la duree du deplacement?\n")
                    gestion_deplacement.deplacement.nombre_match = input("Quel est le nombre de match: ")

                    gestion_deplacement.create()

                    gestion_liste_depart.deplacement.id = gestion_deplacement.get_1()

                    #3-verifier si la liste_depart n'existe pas déjà en testant la combinaison id_equipe,id_deplacement
                    if gestion_liste_depart.get_id():

                        gestion_liste_depart.liste_depart.id = gestion_liste_depart.get_id()[0]
                        print("La liste existe déjà.")
                        pass

                    else:
                        gestion_liste_depart.create()
                        gestion_liste_depart.liste_depart.id = gestion_liste_depart.get_id()[0]


                    #4-remplir la liste_depart de produit si elle n'existe pas


                        rows=gestion_stock.get_1()

                        i = 0
                        while i < 4:

                            print("Combien de", rows[i][3], "voulez vous ajouter?:")

                            try:

                                gestion_liste_depart.produit.quantite_depart = int(input())
                                gestion_liste_depart.create_association_liste_depart_produit(rows[i][2])
                                i += 1

                            except ValueError:
                                print("Veuillez entrez un nombre")
                                i = i

                        print("Voici l'apercu de la liste")
                        gestion_liste_depart.get_1()

                elif option_gestion_liste_depart=="2":

                    #afficher une liste
                    gestion_liste_depart.get_all()
                    gestion_liste_depart.liste_depart._id=input("entrer l'id")
                    gestion_liste_depart.get_1()


        #D-Gestion liste utilisateur

            elif option_administrateur == "4":

                option_gestion_liste_utilisateur= input("Choisissez l'option 1 creer une liste utilisateur,2 consulter liste utilisateur,3 modifier liste utilisateur")

                if option_gestion_liste_utilisateur=="1":

                    #recuperer l'id de l'utilisateur

                    gestion_liste_utilisateur.utilisateur.nom = input("Nom de l'utilisateur: ")
                    gestion_liste_utilisateur.utilisateur.prenom = input("Prenom de l'utilisateur: ")
                    gestion_liste_utilisateur.utilisateur.id = gestion_liste_utilisateur.get_id_utilisateur()

                    #recuperer l'id liste depart

                    #1-choisir une équipe pour recuperer un id_equipe

                    gestion_equipe.equipe.type_rugby = input("Rugby à 15 ou rugby à 7 ?\n")
                    gestion_equipe.equipe.genre = input("Equipe masculine ou feminine ?\n")
                    gestion_equipe.equipe.categorie_age = input("Quelle categorie d'âge ?\n")

                    gestion_liste_depart.equipe.id = gestion_equipe.get_id()

                    #2-creer un deplacement pour recuperer un id_deplacement si il existe déjà, reprendre l'id_existant.

                    gestion_deplacement.deplacement.nombre_joueurs=input("Quel est le nombre de joueurs pendant le deplacement?\n")
                    gestion_deplacement.deplacement.duree_deplacement=input("Quelle est la duree du deplacement?\n")
                    gestion_deplacement.deplacement.nombre_match=input("Quel est le nombre de match: ")

                    gestion_liste_depart.deplacement.id = gestion_deplacement.get_id()

                    #obtenir la liste depart

                    gestion_liste_utilisateur.liste_depart.id = gestion_liste_depart.get_id()

                    #entrer la date du jour

                    gestion_liste_utilisateur.liste_utilisateur.date = date(int(input("Entrer l'année: ")),int(input("le mois: ")),int(input("le jour: ")))

                    #entrer la destination

                    gestion_liste_utilisateur.liste_utilisateur.destination = input("Destination: ")

                    #creer la liste utilisateur pour l'aller

                    gestion_liste_utilisateur.create()
                    gestion_liste_utilisateur.liste_utilisateur.id = gestion_liste_utilisateur.get_id()

                    #remplir la liste utilisateur

                    gestion_liste_utilisateur.create_association_liste_utilisateur_produit()
                    gestion_liste_utilisateur.get_1()

                    #recuperer la liste utilisateur au depart



                    gestion_liste_utilisateur.utilisateur.nom = input("Nom de l'utilisateur: ")
                    gestion_liste_utilisateur.utilisateur.prenom = input("Prenom de l'utilisateur: ")
                    gestion_liste_utilisateur.utilisateur.id = gestion_liste_utilisateur.get_id_utilisateur()

                    gestion_liste_utilisateur.liste_utilisateur.id = gestion_liste_utilisateur.get_id_liste_utilisateur_en_cours()
                    gestion_liste_utilisateur.get_1()

                    #retirer les quantites du stock

                    rows = gestion_liste_utilisateur.get_1()

                    for row in rows:
                        gestion_stock.retirer_quantite_stock(row[5], row[3])



                    #valider les quantites retours

                    #mettre à jour le stock