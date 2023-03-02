# Trombinoscope
[![Python](https://badgen.net/badge/Python/3.10/blue)](https://www.python.org/)
[![Django](https://badgen.net/badge/Django/4.1/blue)](https://www.djangoproject.com/)
[![License](https://badgen.net/badge/License/MIT/orange)](https://choosealicense.com/licenses/mit/)

## Présentation
Application permettant de recenser les membres d'une organisation en y associant une photo d'identité et diverses informations.

Les membres sont regroupés dans une arborescence de services.
## Installation
1. Cloner le répertoire depuis Github, puis se placer dans le répertoire principal.
```shell
git clone https://github.com/rducrot/trombinoscope
cd trombinoscope
```
2. S'assurer que les paquets suivants sont installés :
```shell
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```
3. Installation de l'application via le script `install.sh`.
```shell
bash install.sh
```
Ce script met en place l'environnement virtuel, les dépendances, les variables d'environnement, la base de données et le super utilisateur.

Les informations qui vous sont demandées sont :
* L'adresse IP du serveur (modifiable dans le fichier `trombinoscope/.env`).
* Les informations du super utilisateur.
## Mise en production
Ci-dessous un exemple d'installation sur un serveur web Debian/Ubuntu avec Apache2 et l'application Trombinoscope installée dans `/var/www`.

On commence par installer les dépendances :
```bash
sudo apt-get update
sudo apt-get install apache2 apache2-dev libapache2-mod-wsgi-py3
```
On attribue les droits d'accès à l'application à Apache2 :
```bash
chown -R www-data:www-data /var/www/trombinoscope
```
### Configuration dans `/etc/apache2/`
#### Exemple de fichier `sites-available/trombinoscope.conf`
```text
<VirtualHost *:80>
DocumentRoot /var/www/trombinoscope

Alias /static /var/www/trombinoscope/static
<Directory /var/www/trombinoscope/static>
Require all granted
</Directory>

Alias /media /var/www/trombinoscope/media
<Directory /var/www/trombinoscope/media>
Require all granted
</Directory>

ErrorLog ${APACHE_LOG_DIR}/trombi_error.log
CustomLog ${APACHE_LOG_DIR}/trombi_access.log combined
</VirtalHost>
```
#### Exemple de fichier `conf-available/wsgi.conf`
```text
WSGIScriptAlias / /var/www/trombinoscope/trombinoscope/wsgi.py
WSGIPythonHome /var/www/trombinoscope/venv
WSGIPythonPath /var/www/trombinoscope

<Directory /var/www/trombinoscope/trombinoscope>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```
On lance ensuite les commandes suivantes :
```bash
a2ensite trombinoscope.conf
a2enmod wsgi.conf
systemctl restart apache2.service
```
## Exécution en ligne de commande
Pour tester l'application en environnement de développement :
1. Affecter `DEBUG=True` dans le fichier `trombinoscope/.env`.

2. Activer l'environnement virtuel :
```shell
source venv/bin/activate
```
3. Lancer la commande suivante depuis le répertoire de l'application :
```shell
python3 manage.py runserver
```
L'application est disponible par défaut à l'adresse http://127.0.0.1:8000.

Le super utilisateur peut gérer les services et les agents à l'adresse http://127.0.0.1:8000/admin.