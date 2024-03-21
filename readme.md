# Projet de Scrapping IMDB MySQL et Scrapy

Ce projet vise à scraper des données à partir du site IMDb (Internet Movie Database) et à les stocker dans une base de données MySQL. Les données récupérées incluent des informations sur les films et les séries télévisées, telles que les titres, les résumés, les notes, les acteurs, les réalisateurs, etc.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés avant de commencer :

- Python (version recommandée : 3.x)
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
