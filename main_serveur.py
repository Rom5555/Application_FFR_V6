from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from presentation.web.controllers.index_controller import IndexController
from presentation.web.controllers.gestion_compte_controller import Login_controller

#  déclaration nécessaire au niveau du module pour prise en compte
#  par le serveur uvicorn lors de son lancement
#  (via la commande -w de ce script)
serveur = FastAPI()


@serveur.get("/")
async def root():

    controller = IndexController()
    return HTMLResponse(content=controller.index(), status_code=200)



@serveur.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    try:
        controller = Login_controller()
        # Appeler la méthode login de votre contrôleur en passant l'e-mail et le mot de passe
        message = controller.login(email, password)
        return HTMLResponse(content=message, status_code=200)
    except Exception as error:
        # Gérer les erreurs comme vous le souhaitez
        return HTMLResponse(content="Une erreur s'est produite lors de la connexion.", status_code=500)
