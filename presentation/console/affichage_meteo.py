import datetime
import os
import sys

from utils import meteo_common
from utils.meteo_common import *
from utils.meteo_utils import MeteoUtils

class AffichageMeteo:

    ECRAN_NOMBRE_COLONNES = 200
    DESCRIPTION_NOMBRE_COLONNES = 20
    JOUR_NOMBRE_COLONNES = 25

    # ------------------------------
    # constructeur
    # ------------------------------
    def __init__(self, meteo):
        self._meteo = meteo

    # ------------------------------
    # propriétés
    # ------------------------------

    # ------------------------------
    # méthodes
    # ------------------------------

    @staticmethod
    def _fermer_ligne(message):
        """
        permet de clôturer une ligne de texte avec le caractère "|" en le positionnant à une position qui respecte la taille
        du tableau graphique souhaité (afin d'obtenir un effet visuel de cadre pour le tableau souhaité)
        :param message: le texte à affiché sur la ligne
        :return: le message + les espaces nécessaire + le caractère "|" qui ferme visuellement la ligne
        """
        nombre_caractere_ajout = AffichageMeteo.ECRAN_NOMBRE_COLONNES - 2 - len(message)  # (80 colonnes - la fermeture de ligne)
        chaine_complement = " " * nombre_caractere_ajout + "|"
        return message + chaine_complement

    @staticmethod
    def _fermer_section(message, taille_section, caractere_fin_destion):
        """
        Une section est une zone du tableau, ici clôturée par le caractère proposé en paramètre, en fonction de la taille de la section souhaitée
        :param message: le texte à afficher
        :param taille_section: la taille de la section souhaité (en nombre de caracères)
        :param caractere_fin_destion: le caractère de clôture de section souhaité
        :return: la chaine de caractère formatée avec le caractère de clôture
        """
        nombre_caractere_ajout = taille_section - 1 - len(message)
        chaine_complement = " " * nombre_caractere_ajout + caractere_fin_destion
        return message + chaine_complement

    def _afficher_ligne_prevision(self, text, val_jour1, val_jour2, val_jour3, val_jour4, val_jour5, val_jour6, val_jour7):
        """
        formatage des données pour créer une ligne d'affichage pour les prévisions météo
        :param text: la description du type de prévision affiché
        :param val_jour1: la valeur pour le jour prévu
        :param val_jour2: la valeur pour le jour prévu
        :param val_jour3: la valeur pour le jour prévu
        :param val_jour4: la valeur pour le jour prévu
        :param val_jour5: la valeur pour le jour prévu
        :param val_jour6: la valeur pour le jour prévu
        :param val_jour7: la valeur pour le jour prévu
        """
        description = self._fermer_section("| " + text, AffichageMeteo.DESCRIPTION_NOMBRE_COLONNES, '|')
        jour1 = self._fermer_section(" " + str(val_jour1), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour2 = self._fermer_section(" " + str(val_jour2), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour3 = self._fermer_section(" " + str(val_jour3), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour4 = self._fermer_section(" " + str(val_jour4), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour5 = self._fermer_section(" " + str(val_jour5), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour6 = self._fermer_section(" " + str(val_jour6), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')
        jour7 = self._fermer_section(" " + str(val_jour7), AffichageMeteo.JOUR_NOMBRE_COLONNES, '|')

        print(description + jour1 + jour2 + jour3 + jour4 + jour5 + jour6 + jour7)

    def _afficher_en_tete(self, ville, temperature, condition_meteo):
        """
        Formatage de l'en tête contenant les informations de météo actuelle pour une ville donnée
        :param ville: la ville sur laquelle porte la recherche
        :param temperature: la température actuelle
        :param condition_meteo: une description courte de la condition météo actuelle
        """
        message1 = "Ville: " + ville
        message2 = "Temperature: " + str(temperature)
        message3 = "Condition: " + condition_meteo
        message_ligne = self._fermer_ligne("| " + message1 + " > " + message2 + " > " + message3)
        print("|" + ("-" * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 7)) + "|")
        print(message_ligne)
        print("|" + ("-" * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 7)) + "|")

    def _afficher_previsions(self, previsions):
        """
        Formatage et affichage des prévisions avec les jours de la semaine en colonne et pour chaque ligne
        un type de prévision différents (en fonction de la liste des privisions passée en paramètre
        :param previsions: listes des prévisions (lignes préformatées en mémoire)
        """
        j_1 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_1)
        j_2 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_2)
        j_3 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_3)
        j_4 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_4)
        j_5 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_5)
        j_6 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_6)
        j_7 = self._get_jour(MeteoCommon.PREVISION_J_PLUS_7)

        self._afficher_ligne_prevision("", j_1, j_2, j_3, j_4, j_5, j_6, j_7)
        print("|" + ("-" * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 7)) + "|")

        for prevision in previsions:
            self._afficher_ligne_prevision(prevision['description'], prevision['j1'], prevision['j2'], prevision['j3'],
                                           prevision['j4'], prevision['j5'], prevision['j6'], prevision['j7'])

    def _get_jour(self, period):
        """
        Obtient le jour de la semaine (Lundi, Mardi, etc.) à afficher en fonction du la période demandé et du jour actuel.
        ex : si l'on veur savoir quel est le jour de la semaine à J+2 en fonction du jour actuel (si on est mercredi, cela renvoi vendredi)
        :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
        :return: le jour calculé (chaine de caractères)
        """
        today = datetime.datetime.today()
        j_1 = today + datetime.timedelta(days=1)
        j_2 = today + datetime.timedelta(days=2)
        j_3 = today + datetime.timedelta(days=3)
        j_4 = today + datetime.timedelta(days=4)
        j_5 = today + datetime.timedelta(days=5)
        j_6 = today + datetime.timedelta(days=6)
        j_7 = today + datetime.timedelta(days=7)

        numero_jour = -1

        if period == MeteoCommon.PREVISION_AUJOURDHUI:
            numero_jour = today.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_1:
            numero_jour = j_1.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_2:
            numero_jour = j_2.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_3:
            numero_jour = j_3.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_4:
            numero_jour = j_4.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_5:
            numero_jour = j_5.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_6:
            numero_jour = j_6.isoweekday()
        if period == MeteoCommon.PREVISION_J_PLUS_7:
            numero_jour = j_7.isoweekday()

        if numero_jour == 1:
            return "Lundi"
        if numero_jour == 2:
            return "Mardi"
        if numero_jour == 3:
            return "Mercredi"
        if numero_jour == 4:
            return "Jeudi"
        if numero_jour == 5:
            return "Vendredi"
        if numero_jour == 6:
            return "Samedi"
        if numero_jour == 7:
            return "Dimanche"

    @staticmethod
    def _afficher_image_meteo(statut_image_meteo):
        """
        Affiche à l'écran le contenu du fichier texte correspondant au statut passé en paramètre
        :param statut_image_meteo: statut météo qui permet de choisir l'image appropriée, c'est à dire le bon fichier à ouvrir
        """
        chemin_reprtoire = os.path.dirname(sys.modules['__main__'].__file__) + "/utils/ressources/textes/"
        nom_image = MeteoUtils.get_texte_meteo_file_name(statut_image_meteo)

        chemin_image = chemin_reprtoire + nom_image
        fichier = open(chemin_image, 'r')
        contenu_fichier = fichier.read()
        print(contenu_fichier)
        fichier.close()

    def afficher_ecran_accueil(self):
        """
        Affiche le premier écran qui permet à l'utilisateur de faire son choix entre recherche de ville et consultation directe
        """
        print("|" + ("-" * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 3)) + "|")
        print("|" + (" " * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 3)) + "|")
        print(self._fermer_ligne("| Bienvenue dans ce programme mété, que souhaitez-vous faire ?"))
        print("|" + (" " * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 3)) + "|")
        print(self._fermer_ligne("|    1) Chercher une ville (tapez 1 et appuyez sur la touche entée)"))
        print(self._fermer_ligne("|    2) Consulter la météo d'une ville (tapez 2 et appuyez sur la touche entée)"))
        print("|" + (" " * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 3)) + "|")
        print("|" + ("-" * (AffichageMeteo.ECRAN_NOMBRE_COLONNES - 3)) + "|")
        print()

    @staticmethod
    def afficher_liste_ville(choix_ville_recherche):
        """
        Affiche la liste des villes issues du resulat de la recherche, avec une formatage permettant de présenter l'index
        pour chaque ville à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
        :param choix_ville_recherche:
        """
        print("Voicie la liste des villes trouvées :")
        for choix_ville in choix_ville_recherche.items():
            print('\t' + str(choix_ville[0]) + ") " + choix_ville[1])

    def _construire_affichage_prevision_temperature(self, ville, description, type_temperature):
        """
        Construit en mémoire un dictionnaire qui contient les données prévisionnelles de températures formatées en décimales
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :param description:
        :param type_temperature:
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = description
        previsions['j1'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_1))
        previsions['j2'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_2))
        previsions['j3'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_3))
        previsions['j4'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_4))
        previsions['j5'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_5))
        previsions['j6'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_6))
        previsions['j7'] = "{:.1f}".format(self._meteo.get_temperature_prevision(ville, type_temperature, MeteoCommon.PREVISION_J_PLUS_7))

        return previsions

    def _construire_affichage_prevision_pression_athmospherique(self, ville):
        """
        Construit en mémoire un dictionnaire qui contient les données prévisionnelles athmosphériques formatées avec l'unité de mesure de pression (hPa)
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = "Pression athm."
        previsions['j1'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_1)) + " hPa"
        previsions['j2'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_2)) + " hPa"
        previsions['j3'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_3)) + " hPa"
        previsions['j4'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_4)) + " hPa"
        previsions['j5'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_5)) + " hPa"
        previsions['j6'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_6)) + " hPa"
        previsions['j7'] = str(self._meteo.get_pression_athmospherique_prevision(ville, MeteoCommon.PREVISION_J_PLUS_7)) + " hPa"

        return previsions

    def _construire_affichage_prevision_avis_meteo_detaille(self, ville):
        """
        Construit en mémoire un dictionnaire qui contient l'avis météo détaillé prévisionnelle
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = "Prévision"
        previsions['j1'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_1)
        previsions['j2'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_2)
        previsions['j3'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_3)
        previsions['j4'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_4)
        previsions['j5'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_5)
        previsions['j6'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_6)
        previsions['j7'] = self._meteo.get_avis_meteo_detaille_prevision(ville, MeteoCommon.PREVISION_J_PLUS_7)

        return previsions

    def _construire_affichage_prevision_humidite(self, ville):
        """
        Construit en mémoire un dictionnaire qui contient les prévisions d'humidité
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = "Humidité"
        previsions['j1'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_1)) + "%"
        previsions['j2'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_2)) + "%"
        previsions['j3'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_3)) + "%"
        previsions['j4'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_4)) + "%"
        previsions['j5'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_5)) + "%"
        previsions['j6'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_6)) + "%"
        previsions['j7'] = str(self._meteo.get_humidite_prevision(ville, MeteoCommon.PREVISION_J_PLUS_7)) + "%"

        return previsions

    def _construire_affichage_prevision_vent_vitesse(self, ville):
        """
        Construit en mémoire un dictionnaire qui contient les prévisions de la vitesse du vent avec précision de l'unité
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = "Vent (vitesse)"
        previsions['j1'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_1)) + " km/h"
        previsions['j2'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_2)) + " km/h"
        previsions['j3'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_3)) + " km/h"
        previsions['j4'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_4)) + " km/h"
        previsions['j5'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_5)) + " km/h"
        previsions['j6'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_6)) + " km/h"
        previsions['j7'] = "{:.1f}".format(self._meteo.get_vent_vitesse_prevision(ville, MeteoCommon.PREVISION_J_PLUS_7)) + " km/h"

        return previsions

    def _construire_affichage_prevision_vent_orientation(self, ville):
        """
        Construit en mémoire un dictionnaire qui contient les prévisions de l'orientation du vent avec précision de l'unité
        -> cela permet un affichage basé sur le parcours du dictionnaire
        :param ville: ville sur laquelle porte la demande
        :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
        """
        previsions = {}

        previsions['description'] = "Vent (direction)"
        previsions['j1'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_1)) + "°"
        previsions['j2'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_2)) + "°"
        previsions['j3'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_3)) + "°"
        previsions['j4'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_4)) + "°"
        previsions['j5'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_5)) + "°"
        previsions['j6'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_6)) + "°"
        previsions['j7'] = str(self._meteo.get_vent_orientation_prevision(ville, MeteoCommon.PREVISION_J_PLUS_7)) + "°"

        return previsions

    def afficher_meteo_ville(self, ville):
        # on affiche maintenant les résultats, c'est à dire les infromations météos relatives à la ville choisie par l'utilisateur.
        # pour cela on utilise une fonction d'affichage en premier pour l'entête, qui permet d'obtenir les valeurs nécéssaires en fonction de la ville choisie
        self._afficher_en_tete(ville, self._meteo.get_temperature_actuelle(ville),
                               self._meteo.get_avis_meteo_detaille(ville))

        # l'entête est maintenant affichée pour l'utilisateur, avec les informations météos actuelles sur la ville, mais on souhaite également afficher
        # les prévisions à 7 jours.
        # pour cela on construit une liste qui va stockée les valeurs de prévisions pour les 7 prochains jours
        liste_previsions = []

        liste_previsions.append(
            self._construire_affichage_prevision_temperature(ville, "T° jour", MeteoCommon.PREVISION_TEMPERATURE_JOUR))
        liste_previsions.append(self._construire_affichage_prevision_temperature(ville, "T° min", MeteoCommon.PREVISION_TEMPERATURE_MINI))
        liste_previsions.append(self._construire_affichage_prevision_temperature(ville, "T° max", MeteoCommon.PREVISION_TEMPERATURE_MAXI))
        liste_previsions.append(
            self._construire_affichage_prevision_temperature(ville, "T° mat", MeteoCommon.PREVISION_TEMPERATURE_MATIN))
        liste_previsions.append(
            self._construire_affichage_prevision_temperature(ville, "T° midi", MeteoCommon.PREVISION_TEMPERATURE_APRES_MIDI))
        liste_previsions.append(
            self._construire_affichage_prevision_temperature(ville, "T° nuit", MeteoCommon.PREVISION_TEMPERATURE_NUIT))
        liste_previsions.append(self._construire_affichage_prevision_pression_athmospherique(ville))
        liste_previsions.append(self._construire_affichage_prevision_humidite(ville))
        liste_previsions.append(self._construire_affichage_prevision_vent_vitesse(ville))
        liste_previsions.append(self._construire_affichage_prevision_vent_orientation(ville))
        liste_previsions.append(self._construire_affichage_prevision_avis_meteo_detaille(ville))

        # une fois qu'on a les informations en mémoire (dans la liste) pour les prévisions météo sur les 7 prochains jours,
        # on peut les afficher à l'écran avec un formatage sur les 7 prochains jours
        self._afficher_previsions(liste_previsions)

        # On récupère à présent l'avis météo, c'est une chaîne de caractère.
        # En fonction de sa valeur, on va afficher une image différentes à l'utilisateur
        # image = représentation sous forme de caractères présent dans une fichier
        avis_meteo_actuel = self._meteo.get_avis_meteo_detaille(ville)
        # obtient l'image correspondante à l'avis météo actuel et l'affiche en mode console
        self._afficher_image_meteo(MeteoUtils.get_statut_meteo(avis_meteo_actuel))
