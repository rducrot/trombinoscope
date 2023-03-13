"""
Ce script permet d'importer une liste d'agents dans la base de données à partir d'un fichier csv.
Si des agents sont déjà présents dans la bdd, CEUX-CI SERONT SUPPRIMES.
Des services doivent être préalablement créés avant de lancer ce script (voir "create_services.py").

Le fichier csv doit être placé dans le même dossier que ce script et être nommé "agents.csv". Les entêtes doivent être
présents (voir l'exemple "sample_agents.csv").

Entêtes CSV :
- last_name (str, requis) : Nom de l'agent.
- first_name (str, requis) : Prénom de l'agent.
- service_pk (int, requis) : Identifiant du service auquel est rattaché l'agent. Voir "create_services.py".
- grade (str) : Grade de l'agent.
- registration_number (str) : Matricule de l'agent.
- role (str) : Rôle de l'agent. Renseigner "Chef", "Adjoint", "Secrétaire", ou laisser vide par défaut.
- mail (str) : Adresse mail de l'agent.
- phone (str) : Téléphone fixe de l'agent. Formats national ou international acceptés. Séparation des nombres
acceptés : points, espaces ou sans séparation.
- mobile (str) : Téléphone mobile pro de l'agent. Même format que "phone".
"""

import csv

from app.models import Service, Agent


def check_db():
    if not Service.objects.exists():
        print("Aucun service trouvé. Veuillez commencer par importer des services.")

    if Agent.objects.exists():
        print("Attention ! Des agents sont déjà présents dans la base de données.")
        answer = input("Souhaitez-vous remplacer les remplacer ? [o/N]")
        if answer not in ['o', 'O', 'oui', 'Oui', 'y', 'Y']:
            exit()


def create_agents():
    with open('scripts/agents.csv') as file:
        reader = csv.DictReader(file, delimiter=";")

        Agent.objects.all().delete()

        for row in reader:
            print(row)

            if row["role"]:
                agent = Agent(last_name=row["last_name"],
                              first_name=row["first_name"],
                              grade=row["grade"],
                              registration_number=row["registration_number"],
                              service=Service.objects.get(pk=int(row["service_pk"])),
                              role=row["role"])
            else:
                agent = Agent(last_name=row["last_name"],
                              first_name=row["first_name"],
                              grade=row["grade"],
                              registration_number=row["registration_number"],
                              service=Service.objects.get(pk=int(row["service_pk"])))

            if row["mail"]:
                agent.mail = row["mail"]

            if row["phone"]:
                agent.phone = row["phone"]

            if row["mobile"]:
                agent.mobile = row["mobile"]

            agent.save()


def run():
    check_db()
    create_agents()
