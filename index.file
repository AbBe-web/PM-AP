import streamlit as st
from utils import calculate_bmi, validate_age, validate_height_weight
from recommendations import get_recommendations
from datetime import datetime

def initialize_session_state():
    """Initialize all form fields in session state if they don't exist."""
    defaults = {
        'step': 1,
        'nom': '',
        'prenom': '',
        'age': None,
        'gender': 'Homme',
        'height': None,
        'weight': None,
        'bmi': None,
        'sedentary_status': 'Sédentaire',
        'activity_status': 'Inactif',
        'target_activity': 'Faible exclusivement',
        'symptoms': 'Non',
        'cv_risk': 'Faible',
        'personal_cv': 'Non',
        'sudden_death': 'Non',
        'hereditary_cv': 'Non',
        'cardiotoxic': 'Non',
        'disability': 'Non',
        'specialist_consult': 'Non',
        'injury_risk': 'Non',
        'cancer_follow_up': 'Non',
        'pregnancy': 'Non',
        'comorbidity': 'Non',
        'obstetric_comp': 'Non',
        'respiratory_disease': 'Non',
        'efr_done': 'Non',
        'severe_stage': 'Non',
        'walking_test': 'Non',
        'bio_checkup': 'Non'
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def main():
    # Configuration de la page avec métadonnées pour mobile
    st.set_page_config(
        page_title="Questionnaire Médical - Prescription d'AP",
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={
            'About': "Questionnaire Médical pour la Prescription d'Activité Physique"
        }
    )

    # CSS personnalisé pour améliorer l'affichage mobile
    st.markdown("""
        <style>
        /* Adaptation mobile */
        @media (max-width: 640px) {
            .stButton button {
                width: 100%;
                margin: 0.5rem 0;
                padding: 0.5rem;
                min-height: 44px; /* Taille minimale pour les boutons tactiles */
            }
            .stRadio [role="radiogroup"] {
                margin: 1rem 0;
            }
            .stTextInput input {
                min-height: 44px;
            }
            .stNumberInput input {
                min-height: 44px;
            }
        }
        /* Style général */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1000px;
        }
        h1 {
            font-size: 1.8rem;
            margin-bottom: 2rem;
        }
        h2 {
            font-size: 1.5rem;
            margin: 1.5rem 0;
        }
        .stRadio > label {
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        /* Style pour l'impression */
        @media print {
            .stButton, .stProgress { 
                display: none !important; 
            }
            @page { 
                margin: 2cm;
            }
            body { 
                font-size: 12pt;
            }
            h1, h2, h3 {
                page-break-after: avoid;
            }
            p, li {
                page-break-inside: avoid;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("Questionnaire Médical pour la Prescription d'AP")

    # Initialize session state
    initialize_session_state()

    # Progress bar
    progress = st.progress(st.session_state.step * 20)

    # Navigation buttons dans un conteneur responsive
    nav_cols = st.columns([1, 1])

    if st.session_state.step > 1:
        if nav_cols[0].button('⬅️ Précédent', use_container_width=True):
            st.session_state.step -= 1
            st.rerun()

    # Step 1: Informations de base
    if st.session_state.step == 1:
        st.header("1. Informations de base")

        # Ajout des champs nom et prénom
        nom = st.text_input("Nom", value=st.session_state.nom)
        st.session_state.nom = nom

        prenom = st.text_input("Prénom", value=st.session_state.prenom)
        st.session_state.prenom = prenom

        age = st.number_input("Âge (en années)", 
                            min_value=0, 
                            max_value=120, 
                            value=st.session_state.age)
        st.session_state.age = age

        gender = st.radio("Sexe", 
                         ["Homme", "Femme"], 
                         index=0 if st.session_state.gender == "Homme" else 1)
        st.session_state.gender = gender

        height = st.number_input("Taille (cm)", 
                                min_value=0, 
                                step=1, 
                                format="%d", 
                                value=st.session_state.height)
        st.session_state.height = height

        weight = st.number_input("Poids (kg)", 
                                min_value=0.0, 
                                step=0.1, 
                                format="%.1f", 
                                value=st.session_state.weight)
        st.session_state.weight = weight

        if height and weight:
            bmi = calculate_bmi(height, weight)
            st.session_state.bmi = bmi
            st.info(f"Votre IMC est de: {bmi}")

    # Step 2: Niveau d'activité physique
    elif st.session_state.step == 2:
        st.header("2. Évaluation de l'activité physique")

        st.markdown("### _Niveau actuel_")

        sedentary_status = st.radio(
            "Statut de sédentarité",
            ["Sédentaire", "Non sédentaire"],
            index=0 if st.session_state.sedentary_status == "Sédentaire" else 1
        )
        st.session_state.sedentary_status = sedentary_status

        activity_status = st.radio(
            "Niveau actuel d'activité physique",
            ["Inactif", "Actif"],
            index=0 if st.session_state.activity_status == "Inactif" else 1
        )
        st.session_state.activity_status = activity_status

        st.markdown("### _Niveau visé_")

        target_activity = st.radio(
            "Niveau visé d'activité physique",
            ["Faible exclusivement", "Modéré (3-5.9 METs)", "Intense ou très intense (≥ 6 METs)"],
            index=["Faible exclusivement", "Modéré (3-5.9 METs)", "Intense ou très intense (≥ 6 METs)"].index(st.session_state.target_activity)
        )
        st.session_state.target_activity = target_activity

    # Step 3: Évaluation des risques
    elif st.session_state.step == 3:
        st.header("3. Évaluation des risques")

        st.write("Existe-t-il des symptômes ?")
        symptoms = st.radio("", 
                           ["Oui", "Non"], 
                           key="symptoms_radio",
                           index=0 if st.session_state.symptoms == "Oui" else 1)
        st.session_state.symptoms = symptoms

        st.write("Niveau de risque CV (ESC)")
        cv_risk = st.radio("", 
                           ["Faible", "Modéré", "Élevé", "Très élevé"],
                           key="cv_risk_radio",
                           index=["Faible", "Modéré", "Élevé", "Très élevé"].index(st.session_state.cv_risk))
        st.session_state.cv_risk = cv_risk

        st.subheader("Antécédents")

        st.write("ATCD personnel de maladie CV (hors HTA équilibrée)")
        personal_cv = st.radio("", 
                              ["Oui", "Non"],
                              key="personal_cv_radio",
                              index=0 if st.session_state.personal_cv == "Oui" else 1)
        st.session_state.personal_cv = personal_cv

        st.write("ATCD de mort subite à moins de 50 ans chez un membre de la fratrie au 1er degré")
        sudden_death = st.radio("", 
                               ["Oui", "Non"],
                               key="sudden_death_radio",
                               index=0 if st.session_state.sudden_death == "Oui" else 1)
        st.session_state.sudden_death = sudden_death

        st.write("ATCD familial de maladie cardio-vasculaire héréditaire")
        hereditary_cv = st.radio("", 
                                ["Oui", "Non"],
                                key="hereditary_cv_radio",
                                index=0 if st.session_state.hereditary_cv == "Oui" else 1)
        st.session_state.hereditary_cv = hereditary_cv

        st.write("ATCD de cancer avec notion de traitement cardiotoxique")
        cardiotoxic = st.radio("", 
                              ["Oui", "Non"],
                              key="cardiotoxic_radio",
                              index=0 if st.session_state.cardiotoxic == "Oui" else 1)
        st.session_state.cardiotoxic = cardiotoxic

    # Step 4: Situations particulières
    elif st.session_state.step == 4:
        st.header("4. Situations particulières")

        disability = st.radio(
            "La personne est-elle porteuse d'un handicap ?",
            ["Oui", "Non"],
            index=0 if st.session_state.disability == "Oui" else 1
        )
        st.session_state.disability = disability

        if disability == "Oui":
            specialist_consult = st.radio(
                "A-t-elle pu bénéficier d'un avis spécialisé et/ou d'une consultation médicale d'activité physique depuis moins d'un an ?",
                ["Oui", "Non"],
                index=0 if st.session_state.specialist_consult == "Oui" else 1
            )
            st.session_state.specialist_consult = specialist_consult

        injury_risk = st.radio(
            "Situation de risque de blessures musculosquelettiques",
            ["Oui", "Non"],
            index=0 if st.session_state.injury_risk == "Oui" else 1
        )
        st.session_state.injury_risk = injury_risk

        cancer_follow_up = st.radio(
            "Votre patient est-il actuellement suivi pour un cancer ?",
            ["Oui", "Non"],
            index=0 if st.session_state.cancer_follow_up == "Oui" else 1
        )
        st.session_state.cancer_follow_up = cancer_follow_up

        if st.session_state.gender == "Femme":
            pregnancy = st.radio(
                "Une grossesse est-elle en cours ?",
                ["Oui", "Non"],
                index=0 if st.session_state.pregnancy == "Oui" else 1
            )
            st.session_state.pregnancy = pregnancy

            if pregnancy == "Oui":
                comorbidity = st.radio(
                    "Présence d'une comorbidité ?",
                    ["Oui", "Non"],
                    index=0 if st.session_state.comorbidity == "Oui" else 1
                )
                st.session_state.comorbidity = comorbidity

                obstetric_comp = st.radio(
                    "Présence d'une complication obstétricale ?",
                    ["Oui", "Non"],
                    index=0 if st.session_state.obstetric_comp == "Oui" else 1
                )
                st.session_state.obstetric_comp = obstetric_comp

    # Step 5: Évaluation médicale
    elif st.session_state.step == 5:
        st.header("5. Évaluation médicale")

        respiratory_disease = st.radio(
            "La personne souffre-t-elle d'une maladie respiratoire chronique (BPCO, asthme, maladie pulmonaire interstitielle) ?",
            ["Oui", "Non"],
            index=0 if st.session_state.respiratory_disease == "Oui" else 1
        )
        st.session_state.respiratory_disease = respiratory_disease

        if respiratory_disease == "Oui":
            efr_done = st.radio(
                "Des EFR ont-elles été réalisées depuis moins d'un an ?",
                ["Oui", "Non"],
                index=0 if st.session_state.efr_done == "Oui" else 1
            )
            st.session_state.efr_done = efr_done

            if efr_done == "Oui":
                severe_stage = st.radio(
                    "S'agit-il d'un stade sévère ?",
                    ["Oui", "Non"],
                    index=0 if st.session_state.severe_stage == "Oui" else 1
                )
                st.session_state.severe_stage = severe_stage

                if severe_stage == "Oui":
                    walking_test = st.radio(
                        "La personne a-t-elle passé un test de marche avec mesure en continue de la saturation en O2 réalisé depuis moins d'un an ?",
                        ["Oui", "Non"],
                        index=0 if st.session_state.walking_test == "Oui" else 1
                    )
                    st.session_state.walking_test = walking_test

        bio_checkup = st.radio(
            "Le patient a-t-il eu un bilan biologique comprenant un bilan lipidique et une créatinine depuis moins d'un an ?",
            ["Oui", "Non"],
            index=0 if st.session_state.bio_checkup == "Oui" else 1
        )
        st.session_state.bio_checkup = bio_checkup

        # Generate recommendations
        if st.button("Générer les recommandations", use_container_width=True):
            recommendations = get_recommendations(st.session_state)

            # Create a container for printable content
            with st.container():
                # Patient info and date
                st.markdown("""
                    <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;'>
                """, unsafe_allow_html=True)

                st.subheader("Informations du patient")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Nom:** {st.session_state.nom}")
                    st.write(f"**Prénom:** {st.session_state.prenom}")
                with col2:
                    st.write(f"**Date:** {datetime.now().strftime('%d/%m/%Y')}")

                st.markdown("</div>", unsafe_allow_html=True)

                # Display recommendations
                st.subheader("Recommandations")
                for category, items in recommendations.items():
                    if items:
                        st.markdown(f"""
                            <div style='margin-top: 1rem;'>
                                <strong style='color: #1f77b4;'>{category}</strong>
                            </div>
                        """, unsafe_allow_html=True)
                        for item in items:
                            st.markdown(f"• {item}")

                # Add print button with custom CSS for print layout
                st.markdown("<div style='margin-top: 2rem;'>", unsafe_allow_html=True)
                if st.button("🖨️ Imprimer", use_container_width=True):
                    st.markdown("""
                        <script>
                        window.print();
                        </script>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # Navigation
    if st.session_state.step < 5:
        if nav_cols[1].button('Suivant ➡️', use_container_width=True):
            st.session_state.step += 1
            st.rerun()

if __name__ == "__main__":
    main()
