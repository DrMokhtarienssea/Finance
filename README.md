# Finance
Une application Kivy permettant à l'utilisateur d'enregistrer et de suivre ses prédictions boursières quotidiennement.


# Pages de l'application:
- écran principal:

Titre / bouton "start" / vérification du profil.
- écran de connexion au profil:

Nom + mode de passe / s'inscrire / rester connecté.
- écran de choix des mouvements boursiers:

liste des actifs financiers au jour j / choix de l'utilisateur.
- résultats:

résultats de l'algo et de l'utilisateur pour chaque actif.
- historiques:

calendrier des actifs / retrosprection des résultats contre l'algo


# Modules:
* Connexion à une base de donnée:

MongoDB ou MySQL

* Structure de la base de donnée:

- Users:

UserID (PK)/
Pseudo/
Email/
---------------
- UsersInfo:

Email/
Name/
Surname/
Birthdate/
Nationnality/
Sexe/
---------------
- Events:

EventID (PK)/
UserID (FK)/
PlatformID (FK)/
EventTypeID (FK)/
Value/
Timestamp/
---------------
- EventTypes:

EventTypeID (PK)/
EventName (status update, group created, friend added, friend removed, video posted, image posted, etc...)/
---------------
- Platforms:

PlatformID (PK)/
PlatformName (Facebook, Youtube, likedin, etc)/
---------------
