from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from presentation.web.controllers.index_controller import IndexController


#  déclaration nécessaire au niveau du module pour prise en compte
#  par le serveur uvicorn lors de son lancement
#  (via la commande -w de ce script)
serveur = FastAPI()


@serveur.get("/")
async def root():

    controller = IndexController()
    return HTMLResponse(content=controller.index(), status_code=200)



"""@serveur.post("/villes")
async def read_meteo_ville(ville: str = Form(...)):
    try:
        controller = MeteoVilleController()
        return HTMLResponse(content=controller.read_meteo_ville(ville), status_code=200)

    except Exception as error:
        controller = ErrorController()
        errorMessage = ''.join(tb.format_exception(None, error, error.__traceback__))
        errorMessage = errorMessage.replace(",", "\n")
        htmlMessage = controller.error(errorMessage)
        return HTMLResponse(content=htmlMessage, status_code=500)"""
