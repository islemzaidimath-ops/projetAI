
import joblib

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model.pkl"


# Descriptions des categories
DESCRIPTIONS = {

    "Transport":
        "Votre reclamation concerne les transports publics.",

    "Santé":
        "Votre reclamation concerne les services de sante.",

    "Environnement":
        "Votre reclamation concerne l'environnement.",

    "Administration":
        "Votre reclamation concerne les services administratifs.",

    "Infrastructure":
        "Votre reclamation concerne les infrastructures publiques."

}


def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            "Modele introuvable. Executez train.py."
        )

    return joblib.load(MODEL_PATH)


# Chargement du modele
model = load_model()


def predict_category(text):

    prediction = model.predict([text])[0]

    return {
        "category": prediction,
        "description": DESCRIPTIONS[prediction]
    }