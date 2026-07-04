# IFRI MentorLink

Application web développée dans le cadre du **Projet Intégrateur (Rattrapage) 2025-2026** de l'IFRI.

## Objectif

Cette application permet à un mentoré de rechercher un mentor compatible en fonction :

- des matières ou compétences recherchées ;
- des disponibilités horaires (tolérance de ±1 heure) ;
- de la filière (optionnelle).

Le système affiche ensuite les mentors compatibles avec leur score de compatibilité.

---

## Fonctionnalités

- Recherche de mentors
- Matching par compétences
- Matching par disponibilité horaire (±1 heure)
- Filtrage par filière (optionnel)
- Calcul d'un score de compatibilité
- Affichage des informations du mentor :
  - Nom
  - Matières proposées
  - Matières en commun
  - Disponibilité
  - Filière
  - Format de mentorat
  - Score de compatibilité

---

## Technologies utilisées

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Backend

- Python
- Flask

### Base de données

- PostgreSQL

---

## Structure du projet

```
RPIL_2526_SAGBO_SYDNEY/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── database/
│   └── mentors.sql
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/VOTRE_UTILISATEUR/RPIL_2526_SAGBO_SYDNEY.git
```

Puis entrer dans le dossier :

```bash
cd RPIL_2526_SAGBO_SYDNEY
```

---

### 2. Créer un environnement virtuel (optionnel mais recommandé)

Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS :

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 4. Configurer les variables d'environnement

Copier le fichier :

```
.env.example
```

et le renommer en :

```
.env
```

Modifier ensuite les informations de connexion PostgreSQL.

Exemple :

```env
SECRET_KEY=monSuperSecret2026
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mentorlink
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
```

---

### 5. Créer la base de données

Créer une base PostgreSQL nommée :

```
mentorlink
```

Puis exécuter le script :

```
database/mentors.sql
```

afin de créer la table et insérer les mentors.

---

### 6. Lancer l'application

```bash
python app.py
```

L'application sera accessible à l'adresse :

```
http://127.0.0.1:5000
```

---

## Auteurs

Projet réalisé par :

**Sydney SAGBO**

Étudiant à l'IFRI

Année académique **2025-2026**

---

## Licence

Projet réalisé uniquement dans le cadre pédagogique du Projet Intégrateur (Rattrapage) de l'IFRI.
````
