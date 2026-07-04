-- ==========================================
-- SUPPRESSION DE LA TABLE SI ELLE EXISTE
-- ==========================================

DROP TABLE IF EXISTS mentors;

-- ==========================================
-- CREATION DE LA TABLE
-- ==========================================

CREATE TABLE mentors (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    competences TEXT NOT NULL,
    disponibilite TIME NOT NULL,
    filiere VARCHAR(100) NOT NULL,
    format VARCHAR(30) NOT NULL
);

-- ==========================================
-- INSERTION DES DONNEES
-- ==========================================

INSERT INTO mentors (nom, competences, disponibilite, filiere, format)
VALUES
(
    'Jean Dupont',
    'Python, Flask, HTML, CSS',
    '14:00:00',
    'Informatique',
    'En ligne'
),
(
    'Marie Gomez',
    'Java, SQL, UML, Base de données',
    '09:00:00',
    'Informatique',
    'Présentiel'
),
(
    'Paul Koffi',
    'Python, JavaScript, CSS, Bootstrap',
    '15:00:00',
    'Informatique',
    'Hybride'
);

-- ==========================================
-- VERIFICATION
-- ==========================================

SELECT * FROM mentors;