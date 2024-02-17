from presentation.web.models.meteo_ville_model import MeteoVilleModel
from presentation.web.views.meteo_ville_view import MeteoVilleView


class MeteoVilleController:

    def __init__(self):
        self._view = MeteoVilleView()
        self._model = None

    def read_meteo_ville(self, nom_ville: str) -> str:
        self._model = MeteoVilleModel(nom_ville)
        self._view.nom_ville = nom_ville
        self._view.previsions_jour = self._model.get_previsions_jour()
        self._view.previsions_min = self._model.get_previsions_min()
        self._view.previsions_max = self._model.get_previsions_max()
        self._view.previsions_matin = self._model.get_previsions_matin()
        self._view.previsions_midi = self._model.get_previsions_midi()
        self._view.previsions_soir = self._model.get_previsions_soir()

        return self._view.render()
