import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key_par_defaut")

    DB_HOST = os.getenv("localhost")
    DB_NAME = os.getenv("mentorlink")
    DB_USER = os.getenv("postgres")
    DB_PASSWORD = os.getenv("5652")
    DB_PORT = os.getenv("DB_PORT", "5432")