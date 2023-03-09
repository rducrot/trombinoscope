import csv

from app.models import Service, Agent


def check_db():
    if Agent.objects.exists():
        answer = input("Attention ! Une base de données existe déjà. Souhaitez-vous la remplacer ? [o/N]")
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
