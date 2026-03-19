import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Tableau de bord", page_icon="📊", layout="wide")

st.title("📊 Tableau de bord – Données d’exemple")

# Données d'exemple (ou charge depuis assets/sample.csv)
df = pd.DataFrame({
    "mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
    "visites": [120, 180, 160, 240, 300, 280],
    "inscriptions": [12, 22, 18, 30, 35, 32]
})

# Sélecteurs
mois_sel = st.multiselect("Filtrer par mois :", df["mois"].unique(), default=list(df["mois"]))
df_f = df[df["mois"].isin(mois_sel)]

# Graphique Altair
chart = (
    alt.Chart(df_f)
    .transform_fold(["visites", "inscriptions"], as_=["type", "valeur"])
    .mark_line(point=True)
    .encode(
        x="mois:N",
        y="valeur:Q",
        color="type:N",
        tooltip=["mois", "type", "valeur"]
    )
    .properties(height=350)
)
st.altair_chart(chart, use_container_width=True)

st.dataframe(df_f, use_container_width=True)