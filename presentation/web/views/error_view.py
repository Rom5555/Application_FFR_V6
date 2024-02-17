from presentation.web.views.iview import IView


class ErrorView(IView):

    def __init__(self):
        self._message = ""

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    def render(self) -> str:
        htmlBuilder = HtmlBuilder()
        htmlBuilder.ajouter_html("<h1>Aie ! Une erreur s'est produite côté serveur</h1>")
        htmlBuilder.ajouter_paragraphe("Voici le message pour vous aider à trouver d'ou vient le problème : ")
        htmlBuilder.ajouter_html("<h2>Message : </h2>")
        htmlBuilder.ajouter_html("<br>")
        htmlBuilder.ajouter_zone_texte(self.message)

        return htmlBuilder.HTML
