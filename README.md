# Trombinoscope
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
[![Django](https://badgen.net/badge/Django/4.1/blue)](https://www.djangoproject.com/)

## Présentation
Application permettant de recenser les membres d'une organisation en y associant une photo d'identité.\
Les membres peuvent être regroupés dans une arborescence de services.
## Installation
1. Cloner le répertoire depuis Github, puis se placer dans le répertoire principal.
```shell
git clone https://github.com/rducrot/its-api
cd its-api
```
2. Mettre en place l'environnement virtuel.
```shell
python3 -m venv venv
source venv/bin/activate
```
3. Installer les dépendances depuis l'environnement virtuel.
```shell
pip3 install -r requirements.txt
```
4. Initialiser la base de données.
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Création de l'administrateur.
```shell
python3 manage.py createsuperuser
```
6. Entrer les informations du super utilisateur.
## Exécution
Lancer la commande depuis le répertoire de l'application :
```shell
python3 manage.py runserver
```
L'application est disponible par défaut à l'adresse http://127.0.0.1:8000.\
Le super utilisateur peut gérer les services et les agents à l'adresse http://127.0.0.1:8000/admin.