
import pandas as pd
import joblib

from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Chemins
BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "dataset.csv"
MODEL_PATH = BASE_DIR / "model.pkl"


def train_model():

    print("Chargement du dataset...")

    data = pd.read_csv(DATASET_PATH)

    # Verification des donnees
    if data.empty:
        raise ValueError("Le dataset est vide.")

    if data["text"].isnull().any():
        raise ValueError("Le dataset contient des textes vides.")

    X = data["text"].astype(str)
    y = data["category"]

    print("Categories disponibles :")
    print(y.value_counts())

    # Creation du modele
    model = Pipeline([

        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                strip_accents="unicode",
                ngram_range=(1, 2),
                sublinear_tf=True
            )
        ),

        (
            "classifier",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced",
                random_state=42
            )
        )

    ])

    # Entrainement
    print("Entrainement du modele...")

    model.fit(X, y)

    # Sauvegarde
    joblib.dump(model, MODEL_PATH)

    print("Entrainement termine !")
    print(f"Modele sauvegarde : {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
