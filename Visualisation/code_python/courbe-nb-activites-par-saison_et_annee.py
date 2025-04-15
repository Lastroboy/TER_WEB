import pandas as pd
import plotly.graph_objects as go

# Charger le fichier CSV
file_path = "./data/fetes_et_manifestations2018.csv"
df = pd.read_csv(file_path)

# Convertir la colonne 'Published' en format datetime
df['Published'] = pd.to_datetime(df['Published'], errors='coerce')

# Fonction pour attribuer une saison et son ordre chronologique
def get_season_info(month):
    if month in [12, 1, 2]:
        return "Hiver", 1
    elif month in [3, 4, 5]:
        return "Printemps", 2
    elif month in [6, 7, 8]:
        return "Été", 3
    else:
        return "Automne", 4

# Appliquer la fonction pour extraire la saison et son ordre
df[['Saison', 'Saison_ordre']] = df['Published'].dt.month.apply(lambda x: pd.Series(get_season_info(x)))

# Extraire l'année
df['Année'] = df['Published'].dt.year

# Regrouper les données par année et saison et compter le nombre d'événements
df_count = df.groupby(['Année', 'Saison', 'Saison_ordre']).size().reset_index(name="Nombre d'activités")

# Trier les données correctement (Année puis Saison)
df_count = df_count.sort_values(['Année', 'Saison_ordre'])

# Ajouter une colonne combinée pour l'axe X
df_count['Saison_Annee'] = df_count['Année'].astype(int).astype(str) + " " + df_count['Saison']

# Définition des couleurs par saison
couleurs_saisons = {
    "Hiver": "#4c74b5", 
    "Printemps": "rgb(171, 99, 250)", 
    "Été": "#ffc107", 
    "Automne": "#25272e"
}

# Liste des saisons dans l'ordre voulu
ordre_saisons = ["Hiver", "Printemps", "Été", "Automne"]

# Calculer la courbe globale (somme des activités par saison et année)
df_global = df_count.groupby('Saison_Annee', as_index=False).agg({"Nombre d'activités": 'sum'})

# Création de la figure
fig = go.Figure()

# Ajouter la courbe globale (toujours visible)
fig.add_trace(go.Scatter(
    x=df_global["Saison_Annee"], 
    y=df_global["Nombre d'activités"], 
    mode="lines+markers", 
    line=dict(shape="spline", width=3, color="#dc3545"),  # Courbe globale
    marker=dict(size=8),
    name="Nombre total d'activités",
    visible=True  # Toujours affichée
))

# Ajouter les courbes des saisons
for saison in ordre_saisons:
    df_saison = df_count[df_count["Saison"] == saison]
    fig.add_trace(go.Scatter(
        x=df_saison["Saison_Annee"], 
        y=df_saison["Nombre d'activités"], 
        mode="lines+markers", 
        line=dict(shape="spline", width=3, color=couleurs_saisons[saison]),  
        marker=dict(size=6),
        name=f"{saison}",
        visible="legendonly"  # Masqué par défaut, activable via la légende
    ))

# Personnalisation du graphique
fig.update_layout(
    xaxis=dict(tickangle=-45, categoryorder="array", categoryarray=df_global["Saison_Annee"]),
    yaxis_title="Nombre d'activités",
    hovermode="x unified",
    font=dict(size=12),
    template="plotly",
    # plot_bgcolor="rgba(0,0,0,0)",  # Fond du graphique transparent
    paper_bgcolor="rgba(0,0,0,0)",  # Fond global transparent
)

# Afficher / Exporter le graphique interactif
fig.show()
# fig.write_html("../courbe-nb-activites-par-saison_et_annee.html")

