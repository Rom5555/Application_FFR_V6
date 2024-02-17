from presentation import affichage
from data import data_stock,data_liste,data_selection_liste
from business.components.gestionnaire_stock import Gestionnaire_stock
from business.components.gestionnaire_liste import Gestionnaire_liste

if __name__ == '__main__':

    teststock = Gestionnaire_stock()
    testliste = Gestionnaire_liste()


    teststock.nom_stock = "test"
    testliste.nom_liste = "test"

    while True:

        affichage.affichage_acceuil()

        try:
            affichage.affichage_options()
            choix_tache = int(input("ici: "))

            if choix_tache == 1:
                teststock.afficher_stock()

            elif choix_tache == 2:

                premieres_lettres = input("Donnez les deux premieres lettres de l'item recherché:\n").lower()
                liste=teststock.recherche_item(premieres_lettres)
                id_item = int(input("Entrez l'id de l'item choisi:"))
                teststock.choix_precis(liste, id_item)


            elif choix_tache == 3:
                premieres_lettres = input("Donnez les deux premieres lettres de l'item recherché:\n").lower()
                liste = teststock.recherche_item(premieres_lettres)
                id_item = int(input("Entrez l'id de l'item choisi:"))
                teststock.choix_precis(liste, id_item)
                nombre_ajoute = int(input("Quelle est la quantité à ajouter?:\n"))
                print(nombre_ajoute, teststock.choix_precis(liste, id_item), "ont été ajouté au stock")
                teststock.mise_a_jour_quantite(nombre_ajoute,id_item)


            elif choix_tache == 4:
                nom_item = input("Entrez 1 item:\n").upper()
                nombre_ajoute = input("Definissez la quantite:\n")
                teststock.ajouter_item(nom_item, nombre_ajoute)

            elif choix_tache == 5:
                premieres_lettres = input("Donnez les deux premieres lettres de l'item recherché:\n").lower()
                liste = teststock.recherche_item(premieres_lettres)
                id_item = int(input("Entrez l'id de l'item à supprimer:"))
                print("L'item", teststock.choix_precis(liste, id_item), "a été supprimé du stock")
                teststock.supprimer_item(id_item)

            elif choix_tache == 6:

                nom_choisi=input("Donnez un nom à la liste créée:\n")

                if testliste.verification_existence_liste(nom_choisi) is True:
                    print("Cette liste est déjà crée")
                    testliste.apercu_liste(nom_choisi)

                else:

                    rows = testliste.creer_liste(nom_choisi)

                    i=0
                    while i<len(rows):

                            print("Combien de", rows[i][1],"voulez vous ajouter?:")

                            try:

                                nombre_ajoute=int(input())
                                testliste.remplir_liste(nom_choisi, rows[i][1], nombre_ajoute)
                                i+=1

                            except ValueError:
                                print("Veuillez entrez un nombre")
                                i=i

                print("Voici l'apercu de la liste", nom_choisi)
                testliste.apercu_liste(nom_choisi)

                x=True
                while x==True:
                    confirmation=input("La liste vous convient-elle? y/n\n")

                    if confirmation=='y':
                        print("La liste",nom_choisi,"a bien été créé")

                        x= False

                    elif confirmation=='n':
                        premieres_lettres=input("De quel item souhaiter vous modifier la quantité? Tapez les deux premières lettres:").lower()
                        liste = testliste.rechercher_nom_consommable(nom_choisi,premieres_lettres)
                        id_item = int(input("Entrez l'id de l'item choisi:\n"))
                        testliste.choix_precis(liste, id_item)
                        nombre_ajoute = int(input())
                        testliste.update_liste(nom_choisi,nombre_ajoute,id_item)
                        testliste.apercu_liste(nom_choisi)
                        x=True


                    else:
                        print("Veuillez repondre par y ou n")
                        x= True

            elif choix_tache == 7:
                nom_choisi=input("Quelle liste voulez vous generer?")
                rows = testliste.get_liste(nom_choisi)
                confirmation=input("C'est bien cette liste que vous souhaitez generer? y/n\n")
                if confirmation=='y':
                    print("Le stock va être mis à jour.")
                    for row in rows:
                        testliste.update_stock_avec_liste(nom_choisi, row[1])
                    teststock.afficher_stock()

            elif choix_tache == 8:
                break

            else:
                print("Veuillez choisir un nombre entre 1 et 7")

        except ValueError:
            print("Veuillez tapez un chiffre")
            pass


