# Classification automatique des réclamations des citoyens

## 👨‍🎓 Auteurs
Zaidi Islem & Hannachi Oumayma

## 🎓 Classe
3ème année Licence Mathématiques et Informatique (LMI3)

## 🎯 Objectif du projet

Ce projet a pour objectif de développer un site web permettant aux citoyens de déposer leurs réclamations en ligne et de les classer automatiquement grâce à l'intelligence artificielle.

L'objectif principal est de faciliter le traitement des réclamations et de permettre leur orientation vers les services concernés, tout en proposant une interface moderne, simple et agréable à utiliser.

## ⚙️ Fonctionnalités principales

Le site web permet de :

📝 Remplir un formulaire pour déposer une réclamation.

📥 Envoyer et enregistrer les réclamations des citoyens.

🤖 Analyser automatiquement le texte de la réclamation.

🏷️ Identifier la catégorie correspondante grâce au Machine Learning.

✅ Afficher un message de confirmation et de remerciement après la soumission.

📊 Générer des statistiques à partir des réclamations enregistrées.

## 📂 Catégories des réclamations

Le système permet de classer les réclamations selon les catégories suivantes :

| Catégorie | Description |
|---|---|
| Transport | Problèmes liés aux transports publics, bus et circulation |
| Santé | Problèmes liés aux hôpitaux, soins et services médicaux |
| Environnement | Pollution, déchets et problèmes environnementaux |
| Administration | Problèmes liés aux documents et services administratifs |
| Infrastructure | Routes, éclairage public et équipements publics |

## 🔄 Fonctionnement du site

1️⃣ Le citoyen accède au site web.

2️⃣ Il remplit un formulaire en décrivant sa réclamation.

3️⃣ Le système analyse automatiquement le texte à l'aide de l'intelligence artificielle.

4️⃣ La catégorie correspondante est identifiée.

5️⃣ La réclamation et sa catégorie sont enregistrées dans PostgreSQL.

6️⃣ Un message de remerciement confirme la soumission de la réclamation.

## 🖥️ Interface utilisateur

Le site propose une interface moderne et intuitive comprenant :

- Une page d'accueil présentant le service.
- Un formulaire simple pour saisir les réclamations.
- Une interface d'affichage de la catégorie identifiée.
- Un message de confirmation après chaque soumission.

## 🧠 Classification automatique

Le système utilise des techniques d'intelligence artificielle et de traitement automatique du langage naturel (NLP) pour analyser les réclamations.

Un modèle de Machine Learning est entraîné à partir d'un ensemble de données afin de déterminer automatiquement la catégorie correspondante.

La classification est effectuée sans afficher les mots-clés ou les critères internes utilisés par le système.

## 🛠️ Technologies utilisées

- **Python** : développement du backend et de la partie intelligente.
- **FastAPI** : développement de l'API.
- **HTML** : structure des pages web.
- **CSS** : conception d'une interface moderne et esthétique.
- **JavaScript** : gestion des interactions avec l'utilisateur.
- **Scikit-learn** : entraînement et classification automatique.
- **Pandas** : manipulation des données.
- **PostgreSQL** : stockage des réclamations.
- **Matplotlib** : génération des diagrammes statistiques.
- **Docker et Docker Compose** : conteneurisation et exécution de l'application.
- **Visual Studio Code** : environnement de développement.

## 🐳 Environnement de développement

Le projet est développé avec Visual Studio Code et exécuté à l'aide de Docker.

Docker permet de regrouper les composants nécessaires au fonctionnement de l'application, notamment le backend et la base de données PostgreSQL, et de faciliter son lancement dans un environnement cohérent.

## 🚀 Résultat attendu

Le projet permet aux citoyens de :

- Déposer facilement leurs réclamations.
- Obtenir automatiquement la catégorie de leur réclamation.
- Retrouver leurs réclamations enregistrées dans la base de données.
- Recevoir une confirmation après la soumission.

Le système contribue à simplifier l'organisation et le traitement des réclamations des citoyens.

## 🔮 Perspectives d'amélioration

- Développer un tableau de bord avec des statistiques intégrées au site web.
- Ajouter un système de suivi de l'état des réclamations.
- Améliorer les performances du modèle de classification.

## 🚀 Lancement du projet

```bash
# Construire et démarrer le projet
docker compose up --build -d

# Vérifier les conteneurs
docker compose ps

# Générer les diagrammes statistiques
docker compose exec reclamations python -m app.model.statistics

# Arrêter le projet
docker compose down
```

**Application web :** http://localhost:8000

**Documentation API :** http://localhost:8000/docs

## 📌 Conclusion

Ce projet démontre l'intérêt de l'intelligence artificielle dans l'amélioration des services publics.

Grâce à une interface web intuitive, à la classification automatique et à l'enregistrement des données, il est possible de faciliter le dépôt des réclamations, d'améliorer leur organisation et de simplifier leur orientation vers les services concernés.

## 📅 Année universitaire

2026 – 2027