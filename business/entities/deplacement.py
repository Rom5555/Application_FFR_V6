class Deplacement:

    def __init__(self):
        self.id = 1
        self.nombre_joueur = 0
        self.duree_deplacement = 0
        self.nombre_match = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre_joueur(self):
        return self._nombre_joueur

    @nombre_joueur.setter
    def nombre_joueur(self,value):
        self._nombre_joueur = value

    @property
    def duree_deplacement(self):
        return self._duree_deplacement

    @duree_deplacement.setter
    def duree_deplacement(self,value):
        self._duree_deplacement = value

    @property
    def nombre_match(self):
        return self._nombre_match

    @nombre_match.setter
    def nombre_match(self, value):
        self._nombre_match = value
