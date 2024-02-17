from presentation.web.views.iview import IView
from presentation.web.views.page_acceuil import Page_acceuil


class IndexView(IView):

    page_acceuil = Page_acceuil()

    def render(self) -> str:

        return self.page_acceuil.generer_page_acceuil()
