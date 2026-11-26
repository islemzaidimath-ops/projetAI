
import os
import psycopg
import matplotlib.pyplot as plt

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/reclamations"
)

# Récupérer le nombre de réclamations par catégorie
with psycopg.connect(DATABASE_URL) as conn:
    data = conn.execute("""
        SELECT category, COUNT(*)
        FROM reclamations
        GROUP BY category
        ORDER BY category
    """).fetchall()

if not data:
    print("Aucune réclamation enregistrée dans la base.")
    exit()

categories = [row[0] for row in data]
nombres = [row[1] for row in data]

# Créer le diagramme à bandes
plt.figure(figsize=(10, 6))

plt.bar(categories, nombres)

plt.title("Nombre de réclamations par catégorie")
plt.xlabel("Catégories")
plt.ylabel("Nombre de réclamations")

plt.xticks(rotation=20)
plt.tight_layout()

# Enregistrer le diagramme
os.makedirs("statistiques", exist_ok=True)
plt.savefig("statistiques/reclamations_par_categorie.png")

plt.show()

print("Diagramme généré avec succès.")
