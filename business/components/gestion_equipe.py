from data.data_equipe import Data_equipe
from business.entities.equipe import Equipe
from business.components.ifonction_get import Ifonction_get

class Gestion_equipe(Ifonction_get):

    def __init__(self):
        self.equipe = Equipe()
        self._data_equipe = Data_equipe()

    def get_id(self):

        row = self._data_equipe.get_1_equipe(self.equipe.type_rugby,self.equipe.genre, self.equipe.categorie_age)
        print(row)
        return row[0]

    def get_1(self):
        row = self._data_equipe.get_1_equipe(self.equipe.type_rugby, self.equipe.genre, self.equipe.categorie_age)
        print(row)
        return row

    def get_all(self):
        rows = self._data_equipe.get_all_equipe()
        print(rows)
        return rows
