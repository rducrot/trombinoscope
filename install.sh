#!/bin/bash

# Mise en place de l'environnement virtuel
echo "Création de l'environnement virtuel."
python3 -m venv venv
source venv/bin/activate

# Installation des dépendances
echo "Installation des dépendances."
pip3 install -r requirements.txt

# Création des variables d'environnement
echo "Création des variables d'environnement (trombinoscope/.env)."
secret_key=$(python3 -c "import secrets; print(secrets.token_hex(30))")
read -p "Adresse IP du serveur (plusieurs adresses : séparer par un espace) : " allowed_hosts

# Création du fichier .env
echo "SECRET_KEY=${secret_key}
ALLOWED_HOSTS=${allowed_hosts}
DEBUG=False" > trombinoscope/.env
echo "Fichier trombinoscope/.env créé avec succès."

# Installation de la base de données
echo "Migration de la base de données."
python3 manage.py migrate

# Import des fichiers statiques
python3 manage.py collectstatic --no-input

# Création du super utilisateur
echo "Création du super utilisateur."
python3 manage.py createsuperuser
