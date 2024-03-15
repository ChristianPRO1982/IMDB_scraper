# Projet de Scrapping IMDB avec Django, MySQL et Scrapy

Ce projet vise à scraper des données à partir du site IMDb (Internet Movie Database) et à les stocker dans une base de données MySQL. Les données récupérées incluent des informations sur les films et les séries télévisées, telles que les titres, les résumés, les notes, les acteurs, les réalisateurs, etc. Ces données seront ensuite exploitées dans un site web Django pour fournir aux utilisateurs une plateforme de recherche et de découverte de films et de séries.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés avant de commencer :

- Python (version recommandée : 3.x)
- Django (version recommandée : 3.x)
- MySQL (avec les autorisations nécessaires pour créer une base de données)

## Installation

1. Cloner ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/votre-utilisateur/nom-du-projet.git
    ```

2. Installer les dépendances Python en utilisant pip :

    ```bash
    pip install -r requirements.txt
    ```

3. Configurer la base de données MySQL :
   
   - Créez une nouvelle base de données MySQL pour le projet.
   - Configurez les informations de connexion à la base de données dans le fichier `settings.py` de Django.

4. Lancer le processus de scrapping :

    ```bash
    python manage.py scrape_imdb
    ```

5. Exécutez les migrations pour créer les tables de base de données :

    ```bash
    python manage.py migrate
    ```

6. Lancez le serveur Django :

    ```bash
    python manage.py runserver
    ```

## Structure du Projet

- **scraper**: Contient le code Scrapy pour récupérer les données IMDb.
- **core**: Application Django principale pour la gestion des données.
- **templates**: Templates HTML pour les vues Django.
- **static**: Fichiers statiques tels que les feuilles de style CSS, les scripts JavaScript, etc.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. Fork ce dépôt.
2. Créez une nouvelle branche pour vos fonctionnalités (`git checkout -b feature/nom-de-la-fonctionnalite`).
3. Committez vos modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Push sur la branche (`git push origin feature/nom-de-la-fonctionnalite`).
5. Créez une nouvelle Pull Request.

## Auteurs

- [Christian](https://github.com/ChristianPRO1982)

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
