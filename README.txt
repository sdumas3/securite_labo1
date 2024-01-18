(README) Procédure pour démarrer le serveur et comment y accéder

1. Aller au chemin voulu et ajouter un dossier général pour le projet

2. Créer un environnement virtuel python et l'activer avec les commandes suivantes de l'invite de commades :

> python -mvenv <mon_repertoire>
> cd <mon_repertoire>
> scripts\activate

3. Une fois l'environnement virtuel créé, ajouter le dossier de mon code à la base du dossier du projet

4. Dans le fichier du code, vous verrez le fichier requirement.txt, il suffira d'écrire la commande suivante dans ce chemin du dossier pour installer toutes les dépendances sur l'invite de commandes :

> pip install -r requirement.txt

5. Inscrire la ligne ci-dessous dans l'invite de commandes pour lancer le serveur:

> python main.py

6. Copier-coller le lien web qui affichera dans la console sur le web et il vous restera simplement à remplir le formulaire!
(le lien devrait ressembler à quelque chose comme cela :  http://127.0.0.1:5000)