import streamlit as st

# ---- Configuration de la page (onglet, layout, etc.) ----
st.set_page_config(
    page_title="FairPlate",
    #page_icon="",
    layout="wide",
)

# ---- En-tête / Hero ----
st.title("FairPlate")
st.subheader("Mangez mieux aujourd'hui pour préserver la planète de demain : le guide de la transition alimentaire")

# ---- Barre latérale ----
with st.sidebar:
    #st.image("assets/logo.png", caption="Mon logo", use_container_width=True)
    st.markdown("### Navigation")
    st.link_button("📊 Tableau de bord", "pages/1_📊_Tableau_de_bord.py")
    st.divider()
    st.markdown("**Paramètres**")
    dark_mode = st.toggle("Mode sombre (visuel)")

# ---- Contenu principal ----
st.subsubheader("Bienvenue 👋")
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