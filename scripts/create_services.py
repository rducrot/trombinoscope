"""
Ce script permet d'importer une liste de services dans la base de données à partir d'un fichier csv.
Si des services et des agents sont déjà présents dans la bdd, CEUX-CI SERONT SUPPRIMÉS.

Le fichier csv doit être placé dans le même dossier que ce script et être nommé "services.csv". Les entêtes doivent être
présents (voir l'exemple "sample_services.csv").

Entêtes CSV :
- pk (int, requis) : Identifiant du service. Numéroter à partir de 0. Cet identifiant est à renseigner comme service_pk
pour les agents (voir "create_agents.py").
- name (str, requis) : Nom du service.
- parent_pk (int) : Identifiant du service parent. Le service est placé à la racine si aucun parent renseigné. Le
service parent doit être antérieur dans la liste au service enfant.
- acronym (str) : Acronyme du service.
- address (str) : Adresse physique du service. Laisser vide si identique au service parent.
- mail (str) : Adresse mail fonctionnelle du service.
- phone (str) : Téléphone du standard du service. Formats national ou international acceptés. Séparation des nombres
acceptés : points, espaces ou sans séparation.
"""

import csv

from app.models import Service, Agent


def check_db():
    if Service.objects.exists():
        answer = input("Attention ! Une base de données existe déjà. Souhaitez-vous la remplacer ? [o/N]")
        if answer not in ['o', 'O', 'oui', 'Oui', 'y', 'Y']:
            exit()


def create_services():
    with open('scripts/services.csv') as file:
        reader = csv.DictReader(file, delimiter=";")

        Service.objects.all().delete()
        Agent.objects.all().delete()

        for row in reader:
            print(row)

            if row["parent_pk"]:
                service = Service(pk=int(row["pk"]),
                                  name=row["name"],
                                  parent=Service.objects.get(pk=int(row["parent_pk"])))
            else:
                service = Service(pk=int(row["pk"]),
                                  name=row["name"])

            if row["acronym"]:
                service.acronym = row["acronym"]

            if row["address"]:
                service.address = row["address"]

            if row["mail"]:
                service.mail = row["mail"]

            if row["phone"]:
                service.phone = row["phone"]

            service.save()


def run():
    check_db()
    create_services()
