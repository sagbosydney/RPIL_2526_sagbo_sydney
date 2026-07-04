document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const matieres = document
                .querySelector('input[name="matieres"]')
                .value
                .trim();

            const heure = document
                .querySelector('input[name="heure"]')
                .value;

            if (matieres === "") {
                alert("Veuillez saisir au moins une matière ou compétence.");
                event.preventDefault();
                return;
            }

            if (heure === "") {
                alert("Veuillez sélectionner une heure.");
                event.preventDefault();
                return;
            }

            const bouton = form.querySelector("button");

            bouton.disabled = true;
            bouton.innerHTML = "Recherche en cours...";
        });

    }

});
