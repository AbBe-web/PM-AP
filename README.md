# Questionnaire Médical pour la Prescription d'Activité Physique

Une application Streamlit pour générer des recommandations médicales personnalisées pour la prescription d'activité physique.

## Installation

1. Clonez ce repository :
```bash
git clone [URL de votre repository]
cd [nom du repository]
```

2. Installez les dépendances requises :
```bash
pip install streamlit
```

## Utilisation

1. Lancez l'application :
```bash
streamlit run main.py
```

2. Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501)

## Fonctionnalités

- Questionnaire médical interactif en 5 étapes
- Calcul automatique de l'IMC
- Génération de recommandations personnalisées
- Interface responsive (PC et mobile)
- Impression des recommandations
- Sauvegarde des données entre les étapes

## Structure du projet

- `main.py` : Application principale Streamlit
- `utils.py` : Fonctions utilitaires (calcul IMC, validations)
- `recommendations.py` : Logique de génération des recommandations
- `.streamlit/config.toml` : Configuration Streamlit

## Licence

[Votre licence]
