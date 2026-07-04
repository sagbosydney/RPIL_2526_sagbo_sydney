from flask import Flask, render_template, request
import psycopg
from dotenv import load_dotenv 
from datetime import datetime
import os

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# ===========================
# CONNEXION A POSTGRESQL
# ===========================

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()


# ===========================
# FONCTIONS
# ===========================

from datetime import datetime, time

def convertir_heure(heure):
    """
    Convertit une heure en objet datetime.
    Accepte aussi bien une chaîne ('14:00')
    qu'un objet datetime.time venant de PostgreSQL.
    """

    if isinstance(heure, time):
        return datetime.combine(datetime.today(), heure)

    if isinstance(heure, str):
        try:
            return datetime.strptime(heure, "%H:%M")
        except ValueError:
            return datetime.strptime(heure, "%H:%M:%S")

    raise TypeError(f"Type d'heure non pris en charge : {type(heure)}")


def heures_compatibles(h1, h2):
    """
    Vérifie si deux heures sont compatibles
    avec une tolérance de ±1 heure.
    """

    h1 = convertir_heure(h1)
    h2 = convertir_heure(h2)

    difference = abs((h1 - h2).total_seconds()) / 3600

    return difference <= 1


def score_matching(matieres_recherchees,
                   matieres_mentor,
                   heure_recherchee,
                   heure_mentor):
    """
    Retourne :
    - score
    - matières communes
    """

    recherche = [
        x.strip().lower()
        for x in matieres_recherchees.split(",")
    ]

    mentor = [
        x.strip().lower()
        for x in matieres_mentor.split(",")
    ]

    communes = list(set(recherche) & set(mentor))

    score = len(communes) * 50

    if heures_compatibles(
            heure_recherchee,
            heure_mentor):
        score += 50

    return score, communes


# ===========================
# ROUTE PRINCIPALE
# ===========================

@app.route("/", methods=["GET", "POST"])
def index():

    resultats = []

    if request.method == "POST":

        matieres = request.form["matieres"]

        heure = request.form["heure"]

        filiere = request.form.get("filiere")

        # Récupération des mentors

        if filiere != "":

            cursor.execute("""
                SELECT *
                FROM mentors
                WHERE LOWER(filiere)=LOWER(%s)
            """, (filiere,))

        else:

            cursor.execute("""
                SELECT *
                FROM mentors
            """)

        mentors = cursor.fetchall()

        for mentor in mentors:

            id_mentor = mentor[0]
            nom = mentor[1]
            competences = mentor[2]
            disponibilite = mentor[3]
            filiere_mentor = mentor[4]
            format_mentorat = mentor[5]

            score, communes = score_matching(
                matieres,
                competences,
                heure,
                disponibilite
            )

            print("Recherche :", matieres)
            print("Mentor :", competences)
            print("Communes :", communes)
            print("Heure demandée :", heure)
            print("Heure mentor :", disponibilite)
            print("-------------------------")

            if len(communes) > 0 and heures_compatibles(
                    heure,
                    disponibilite):

                resultats.append({

                    "nom": nom,

                    "competences": competences,

                    "communes": ", ".join(communes),

                    "disponibilite": disponibilite,

                    "filiere": filiere_mentor,

                    "format": format_mentorat,

                    "score": score

                })

        resultats = sorted(
            resultats,
            key=lambda x: x["score"],
            reverse=True
        )

    return render_template(
        "index.html",
        resultats=resultats
    )


# ===========================
# LANCEMENT
# ===========================

if __name__ == "__main__":
    app.run(debug=True)