
const form = document.getElementById("complaintForm");

const textarea = document.getElementById("complaint");

const counter = document.getElementById("counter");

const loading = document.getElementById("loading");

const result = document.getElementById("result");

const error = document.getElementById("error");

const submitBtn = document.getElementById("submitBtn");

const newComplaint = document.getElementById("newComplaint");


// Compteur de caracteres
textarea.addEventListener("input", () => {

    counter.textContent =
        `${textarea.value.length} / 3000 caractères`;

});


// Soumission d'une seule reclamation
form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const text = textarea.value.trim();

    // Verification
    if (text.length < 10) {

        error.textContent =
            "Veuillez saisir une réclamation plus détaillée.";

        error.classList.remove("hidden");

        return;
    }

    // Initialisation
    result.classList.add("hidden");

    error.classList.add("hidden");

    loading.classList.remove("hidden");

    submitBtn.disabled = true;

    submitBtn.textContent = "Analyse en cours...";


    try {

        // Appel API
        const response = await fetch("/api/classify", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                text: text

            })

        });


        const data = await response.json();


        // Gestion des erreurs API
        if (!response.ok) {

            throw new Error(
                data.detail || "Une erreur est survenue."
            );

        }


        // Affichage du resultat
        document.getElementById("category").textContent =
            data.category;

        document.getElementById("description").textContent =
            data.description;

        


        loading.classList.add("hidden");

        result.classList.remove("hidden");


        // Cacher le formulaire apres soumission
        form.classList.add("hidden");

    }

    catch (err) {

        loading.classList.add("hidden");

        error.textContent = err.message;

        error.classList.remove("hidden");

    }

    finally {

        submitBtn.disabled = false;

        submitBtn.textContent =
            "Analyser ma réclamation →";

    }

});


// Deposer une nouvelle reclamation
newComplaint.addEventListener("click", () => {

    // Vider le formulaire
    form.reset();

    // Reafficher le formulaire
    form.classList.remove("hidden");

    // Cacher le resultat
    result.classList.add("hidden");

    error.classList.add("hidden");

    // Reinitialiser le compteur
    counter.textContent = "0 / 3000 caractères";

    // Revenir au formulaire
    document.getElementById("depot").scrollIntoView({
        behavior: "smooth"
    });

    textarea.focus();

});
