from presentation.web.views.error_view import ErrorView


class ErrorController:

    def __init__(self):
        self._view = ErrorView()

    def error(self, message):
        self._view.message = message
        return self._view.render()
