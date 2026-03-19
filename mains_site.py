import streamlit as st

# ---- Configuration de la page (onglet, layout, etc.) ----
st.set_page_config(
    page_title="FairPlate",
    #page_icon="",
    layout="wide",
)
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

/* Style du titre */
h1 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    color: #1b5e20;
}

/* Style des sous-titres */
h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    color: #2e7d32;
}
</style>
""", unsafe_allow_html=True)

# ---- En-tête / Hero ----
st.title("FairPlate")
st.caption("Mangez mieux aujourd'hui pour préserver la planète de demain : le guide de la transition alimentaire")

# ---- Barre latérale ----
with st.sidebar:
    #st.image("assets/logo.png", caption="Mon logo", use_container_width=True)
    st.markdown("### Navigation")
    st.link_button("Recherche aliment", "pages/page1.py")
    st.divider()
    st.markdown("**Paramètres**")
    dark_mode = st.toggle("Mode sombre (visuel)")

# ---- Contenu principal ----
st.subheader("Bienvenue 👋")
st.write(
    "Ceci est la page d’accueil de ton site. Utilise le menu **pages** (en haut à gauche) "
    "ou les boutons dans la barre latérale pour naviguer."
)

# ---- Boutons d'accès direct aux pages ----
if st.button("📊 Aller au Tableau de bord", use_container_width=True):
    st.switch_page("pages/page1.py")

# ---- Exemple d’UI ----
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Utilisateurs", 124)
with col2:
    st.metric("Conversions", "12%", delta="+2.3%")
with col3:
    st.metric("Satisfaction", "4.7 / 5")

# ---- Footer ----
st.divider()
st.caption("© 2026 – FairPlate | Fait avec ❤️ et Streamlit")