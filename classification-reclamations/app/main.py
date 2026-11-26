
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.database import save_complaint

from pydantic import BaseModel, Field
from pathlib import Path

from app.model.predictor import predict_category


# Initialisation
app = FastAPI(

    title="Classification des reclamations citoyennes",

    description="API de classification automatique avec Machine Learning",

    version="1.0.0"

)


# Chemins
BASE_DIR = Path(__file__).resolve().parent

STATIC_DIR = BASE_DIR / "static"


# Fichiers statiques
app.mount(

    "/static",

    StaticFiles(directory=STATIC_DIR),

    name="static"

)


# Structure d'une reclamation
class Complaint(BaseModel):

    text: str = Field(

        min_length=10,

        max_length=3000,

        description="Une seule reclamation"

    )


# Page d'accueil
@app.get("/")
def home():

    return FileResponse(STATIC_DIR / "index.html")


# Verification du serveur
@app.get("/api/health")
def health():

    return {

        "status": "OK",

        "message": "Application operationnelle"

    }


# Classification
@app.post("/api/classify")
def classify(complaint: Complaint):

    text = complaint.text.strip()

    if len(text) < 10:

        raise HTTPException(

            status_code=400,

            detail="Veuillez saisir une reclamation plus detaillee."

        )

    try:

        result = predict_category(text)
        save_complaint(text, result["category"])

        return {

            "success": True,

            "category": result["category"],

            "description": result["description"],

            "message": "Votre reclamation a ete analysee avec succes. Merci pour votre participation !"

        }

    except Exception:

        raise HTTPException(

            status_code=500,

            detail="Une erreur est survenue pendant la classification."

        )
