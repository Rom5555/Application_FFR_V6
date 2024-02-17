from business.components.ifonction_get import Ifonction_get
from business.components.ifonction_create import Ifonction_create
from business.components.ifonction_update import Ifonction_update
from data.data_liste_depart import Data_liste_depart
from data.data_stock import Data_stock
from data.data_liste_utilisateur import Data_liste_utilisateur
from data.data_equipe import Data_equipe
from data.data_deplacement import Data_deplacement
from business.entities.liste_depart import Liste_depart
from business.entities.equipe import Equipe
from business.entities.deplacement import Deplacement
from business.entities.produit import Produit

class Gestion_liste_depart(Ifonction_get,Ifonction_create,Ifonction_update):

    def __init__(self):

        self.equipe=Equipe()
        self.deplacement=Deplacement()
        self.liste_depart=Liste_depart()
        self.produit = Produit()
        self._data_liste_depart = Data_liste_depart()
        self._data_liste_utilisateur = Data_liste_utilisateur()
        self._data_stock = Data_stock()
        self._data_equipe = Data_equipe()
        self._data_deplacement = Data_deplacement()

    def create(self):

        self._data_liste_depart.create_liste_depart(self.equipe.id,self.deplacement.id)

    def create_association_liste_depart_produit(self,id_produit):

        self._data_liste_depart.create_association_liste_depart_produit(self.liste_depart.id,id_produit, self.produit.quantite_depart)

    def update(self):

        self._data_liste_depart.update_liste_depart(self.produit.quantite_depart,self.liste_depart.id,self.produit.id)

    def get_id(self):

        row = self._data_liste_depart.get_id_liste_depart(self.equipe.id, self.deplacement.id)
        print(row)
        return row[0]


    def get_1(self):

        rows = self._data_liste_depart.get_liste_depart(self.liste_depart.id)
        for row in rows:
            print("id_liste_depart:",row[0],"id_stock:",row[1],"nom_stock:",row[2],"id_produit:",row[3],"nom_produit:",row[4],"quantite_depart:",row[5],"quantite_retour:",row[6])

    def test_exist(self):

        return self._data_liste_depart.test_exist(self.equipe.id, self.deplacement.id)

    def get_all(self):

        rows = self._data_liste_depart.get_all_liste_depart()
        for row in rows:
            print("id_liste_depart:",row[0],"type rugby",row[1],"genre",row[2],"categorie age",row[3],"nombre joueurs",row[4],"duree deplacement",row[5])




