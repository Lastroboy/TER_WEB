import pandas as pd
import plotly.graph_objects as go
import csv
import plotly.io as pio


# Charger les données
activites = []
with open("DataClean_activités_culturelles_et_sportives.csv", "r", encoding="utf-8") as fm:
    for ligne in csv.DictReader(fm, delimiter=","):
        activites.append(ligne)

df = pd.DataFrame.from_dict(activites)

# Nettoyage des données
df["nomSport"] = df["nomSport"].astype(str).str.split("#").str[-1].str.strip()
df = df[df["nomSport"] != ""]  # Supprimer les lignes où "NomSport" est vide
df["ouvertureCovid"] = df["ouvertureCovid"].replace({"": None, "oui": "Ouvert", "non": "Fermé"})  # Remplacer les valeurs vides
df = df.dropna(subset=["ouvertureCovid"])
# print(df_grouped)  # Vérifie si les données sont bien groupées
# print(df_grouped.columns) 
# # Liste des villes uniques
villes = sorted(df["nomVille"].unique())

# # Création des options pour le menu déroulant
buttons = []
fig = go.Figure()
all_traces=[]
for ville in villes:
    df_ville = df[df["nomVille"] == ville]

#     # Grouper les données pour compter les activités ouvertes/fermées
    df_grouped = df_ville.groupby(["nomSport", "ouvertureCovid"]).size().unstack(fill_value=0)
    if "Ouvert" not in df_grouped.columns:
        df_grouped["Ouvert"] = 0
    if "Fermé" not in df_grouped.columns:
        df_grouped["Fermé"] = 0
    df_grouped = df_grouped[["Ouvert", "Fermé"]].fillna(0)
#     # Création des barres
    traces_ville = []
    for status, color in zip(["Ouvert", "Fermé"], ["blue", "red"]):
        if status in df_grouped.columns:  # Vérifie que la colonne existe
            trace = go.Bar(
                x=df_grouped.index,
                y=df_grouped[status],
                name=f"{status} - {ville}",
                marker=dict(color=color),
                visible=False  # Toutes les traces sont cachées par défaut
            )
            traces_ville.append(trace)

    all_traces.extend(traces_ville)

# Ajouter toutes les traces à la figure
fig.add_traces(all_traces)

# Création du menu déroulant
for i, ville in enumerate(villes):
    visibility = [False] * len(all_traces)  # Initialiser toutes les valeurs à False
    
    # Activer uniquement les traces correspondantes à la ville sélectionnée
    num_traces_per_ville = 2  # Une barre pour "Ouvert", une pour "Fermé"
    start_index = i * num_traces_per_ville
    end_index = start_index + num_traces_per_ville
    visibility[start_index:end_index] = [True] * num_traces_per_ville

    buttons.append(dict(
        label=ville,
        method="update",
        args=[{"visible": visibility}]
    ))

# Activer la première ville par défaut
for j in range(2):  
    fig.data[j].visible = True


# # Ajouter le menu déroulant
fig.update_layout(
    updatemenus=[{
        "buttons": buttons,
        "direction": "down",
        "showactive": True
    }],
    xaxis_title="Activités sportives",
    yaxis_title="Nombre d'activités",
    barmode="group",
    xaxis=dict(tickangle=-45)
)

# Sauvegarder le graphique dans un fichier HTML
pio.write_html(fig, file="activites_ouvertes_fermees_villes.html", auto_open=False)