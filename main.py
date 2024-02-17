import os
import sys

if __name__ == '__main__':
    # Vérifiez si un seul argument est passé (le port)
    if len(sys.argv) != 2:
        print("Usage: python script.py <port>")
        sys.exit(2)

    # Récupérez le port à partir du premier argument
    port = sys.argv[1]

    # Pour exécuter ce code, assurez-vous d'avoir installé les packages Python suivants :
    # fastapi 0.74
    # uvicorn 0.17.6
    # python-multipart 0.0.5

    print("Initialisation du serveur...")
    project_directory = os.getcwd()
    bin_directory = os.chdir(project_directory + "/venv/Scripts")
    print(f"Répertoire du projet = {project_directory}")
    print(f"Répertoire de lancement du serveur web = {bin_directory}")
    command = f"uvicorn --app-dir={project_directory} main_serveur:serveur --port {str(port)} "
    print(f"Lancement de la commande : {command}")
    os.system(command)
    print("Serveur démarré et à l'écoute.")

