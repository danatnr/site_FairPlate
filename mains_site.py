import streamlit as st

# ---- Configuration de la page (onglet, layout, etc.) ----
st.set_page_config(
    page_title="FairPlate",
    #page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Masquer le menu supérieur ----
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---- Style personnalisé ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

/* Fond de couleur vert dégradé */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    background-attachment: fixed;
}

/* Police personnalisée */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

@import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&display=swap');

/* Style du titre */
h1 {
    font-family: 'Comfortaa', 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 4rem !important;
    color: #2e7d32 !important;
    letter-spacing: 2px;
}


/* Style des sous-titres */
h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    color: #2e7d32;
}

/* Style de la sidebar */
[data-testid="stSidebar"] {
    background-color: #1b5e20 !important;
}

[data-testid="stSidebar"] .markdown-text-container {
    color: #ffffff !important;
}

[data-testid="stSidebar"] h3 {
    color: #90ee90 !important;
}

[data-testid="stSidebar"] p {
    color: #e8f5e9 !important;
}

/* Boutons de la sidebar - CORRIGÉ */
[data-testid="stSidebar"] [data-testid="stButton"] button {
    background-color: #4caf50 !important;
    color: #1b5e20 !important;
    font-weight: 600 !important;
}

/* Masquer le menu automatique */
[data-testid="collapsedControl"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---- En-tête / Hero ----
st.title("FairPlate")
st.caption("Mangez mieux aujourd'hui pour préserver la planète de demain : le guide de la transition alimentaire")

# ---- Barre latérale ----
with st.sidebar:
    st.markdown("### Navigation")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("pages/mains_site.py")
    with col2:
        if st.button("🔍 Recherche", use_container_width=True):
            st.switch_page("pages/page1.py")
    with col3:
        if st.button("📧 Contact", use_container_width=True):
            st.switch_page("pages/mains_site.py")
    
    st.divider()
    st.markdown("**Paramètres**")
    dark_mode = st.toggle("Mode sombre (visuel)")

# ---- Contenu principal ----
st.subheader("Bienvenue 👋")
st.write(
    " "
)

# ---- Boutons d'accès direct aux pages ----
if st.button("Aller à la Recherche d'aliments", use_container_width=True):
    st.switch_page("pages/page1.py")

# ---- Exemple d'UI ----
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Utilisateurs", 124)
with col2:
    st.metric("Conversions", "12%", delta="+2.3%")
with col3:
    st.metric("Satisfaction", "4.7 / 5")

# ---- Formulaire de contact ----
st.divider()
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
# Container avec fond vert foncé
st.markdown("""
<style>
.contact-form {
    background-color: #2e7d32;
    padding: 30px;
    border-radius: 15px;
    margin: 20px 0;
}

.contact-form h3 {
    color: #ffffff !important;
    margin-top: 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="contact-form">', unsafe_allow_html=True)

st.markdown("### 📧 Contactez-nous", unsafe_allow_html=True)

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        nom = st.text_input("Votre nom", placeholder="Jean Dupont", key="nom_contact")
    
    with col2:
        email = st.text_input("Votre email", placeholder="jean@example.com", key="email_contact")
    
    sujet = st.selectbox("Sujet", ["Question générale", "Suggestion", "Problème technique", "Autre"], key="sujet_contact")
    
    message = st.text_area("Message", placeholder="Écrivez votre message ici...", height=150, key="message_contact")
    
    submitted = st.form_submit_button("Envoyer", use_container_width=True)
    
    if submitted:
        if nom and email and message:
            st.success(f"✅ Merci {nom} ! Nous avons reçu votre message et vous répondrons à {email} bientôt.")
            st.balloons()
        else:
            st.error("⚠️ Veuillez remplir tous les champs!")

st.markdown('</div>', unsafe_allow_html=True)

# ---- Footer ----
st.divider()
st.caption("© 2026 – FairPlate | Fait avec ❤️ et Streamlit")