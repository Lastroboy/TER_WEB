import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("./activités-sportives-culturelles.csv", delimiter=",")  # Changer le délimiteur si nécessaire (ex: ',' ou '\t')
source = ColumnDataSource(df)

# Afficher les premières lignes
print(df.head())

# Comptage des installations par code postal
# Supposons que df contient tes données
df = df.dropna(subset=["codePostal"])  # Supprime les valeurs NaN

# Assurer que les codes postaux sont bien des strings et récupérer les 2 premiers chiffres (département)
df["codePostal"] = df["codePostal"].astype(str)
df = df[df["codePostal"].str.len() >= 2]  # Filtrer les codes postaux trop courts
df["departement"] = df["codePostal"].str[:2]

# Compter le nombre d'installations par département
departement_counts = df["departement"].value_counts().reset_index()
departement_counts.columns = ["Département", "Nombre d'installations"]

# Création du graphique interactif avec Plotly
fig = px.bar(
    departement_counts,
    x="Département",
    y="Nombre d'installations",
    color_discrete_sequence=["#dc3545"]
)

# Personnalisation du graphique
fig.update_traces(textposition="outside")  # Afficher les valeurs au-dessus des barres
fig.update_layout(
    xaxis_title="Département",
    yaxis_title="Nombre d'installations",
    title_font=dict(size=18, color="#2C3E50"),
    xaxis=dict(tickmode="array", tickvals=departement_counts["Département"]),
    paper_bgcolor="rgba(0,0,0,0)",  # Fond global transparent
)

# Affichage interactif du graphique
fig.write_html("../histogram-repartition-infrastuctures-sportives-par-departement.html")



