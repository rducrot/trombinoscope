import csv

from app.models import Service


def check_db():
    if Service.objects.exists():
        answer = input("Attention ! Une base de données existe déjà. Souhaitez-vous la remplacer ? [o/N]")
        if answer not in ['o', 'O', 'oui', 'Oui', 'y', 'Y']:
            exit()


def create_services():
    with open('scripts/services.csv') as file:
        reader = csv.DictReader(file, delimiter=";")

        Service.objects.all().delete()

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

            if row["mail"]:
                service.mail = row["mail"]

            if row["phone"]:
                service.phone = row["phone"]

            service.save()


def run():
    check_db()
    create_services()
