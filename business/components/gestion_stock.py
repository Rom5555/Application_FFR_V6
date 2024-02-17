from business.components.ifonction_get import Ifonction_get
from business.components.ifonction_update import Ifonction_update
from data.data_stock import Data_stock
from business.entities.stock import Stock
from business.entities.produit import Produit

class Gestion_stock(Ifonction_get,Ifonction_update):

    def __init__(self):

        self.produit = Produit()
        self.stock = Stock()
        self._data_stock = Data_stock()


    def get_all(self):

        rows= self._data_stock.get_all_stocks()
        for row in rows:
            print("id:", row[0], "nom du stock:", row[1])


    def get_1(self):

        retour = self._data_stock.get_stock_consommable()
        count = retour[0]
        print("Le nombre d'item",count)
        rows = retour[1]
        for row in rows:
            print("id_stock:", row[0], "nom_stock:", row[1], ":", "id_produit:", row[2], "nom_produit:", row[3],
                  "quantite en stock:", row[4])
        return rows

    def get_id(self):

        return self._data_stock.get_id_stock(self.stock.nom)[0]



    def get_stock_1_produit(self):

        row=self._data_stock.get_stock_1produit(self.produit.id)
        print("id_stock:", row[0], "nom_stock:", row[1], ":", "id_produit:", row[2], "nom_produit:", row[3],
              "quantite en stock:", row[4])

    def get_1_produit(self,premieres_lettres):

        rows=self._data_stock.get_1_produit(premieres_lettres)
        for row in rows:
            print("id:", row[0], "nom:", row[1])

    def ajouter_quantite_stock(self,nombre_ajoute):

        self._data_stock.ajouter_quantite_stock(nombre_ajoute,self.produit.id)

    def retirer_quantite_stock(self, nombre_retire,id_produit):

        self._data_stock.retirer_quantite_stock(nombre_retire,id_produit)


    def update(self):

        self._data_stock.update_produit_stock(self.produit.nom,self.stock.id,self.produit.quantite_en_stock)


