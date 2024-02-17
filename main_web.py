if __name__ == '__main__':

    port = 80
    if arg != None and arg != "":
        port = arg
    # pour exécuter ce code, assurer vous d'avoir installé les packages python suivant :
    # fastapi 0.74
    # uvicorn 0.17.6
    # python-multipart 0.0.5

    # os.system(command)
    # on se positionne dans le répertoire bin de l'environnement virtuel python pour démarrer
    # le serveur web unicorn
    print("Initialisation du serveur...")
    project_directory = os.getcwd()
    bin_directory = os.chdir(project_directory + "/venv/Scripts")
    print(f"Répertoire du projet = {project_directory}")
    print(f"Répertoire de lancement du serveur web = {bin_directory}")
    command = f"uvicorn --app-dir={project_directory} main_serveur:serveur --port {str(port)} "
    print(f"Lancement de la commande : {command}")
    os.system(command)
