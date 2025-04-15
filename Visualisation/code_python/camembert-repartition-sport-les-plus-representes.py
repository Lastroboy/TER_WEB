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


# Comptage des occurrences par sport
# Nombre maximum de sports à afficher (ex: 5)
TOP_N = 5

# Comptage des occurrences par sport
sport_counts = df["nomSport"].value_counts()

# Séparer les top sports et les autres
top_sports = sport_counts.nlargest(TOP_N)  # Prend les TOP_N sports les plus fréquents
others = sport_counts[TOP_N:].sum()  # Somme des autres sports

# Ajouter une catégorie "Autres" si nécessaire
if others > 0:
    top_sports["Autres"] = others

# Création du graphique interactif avec un dégradé de jaune
fig = px.pie(
    names=top_sports.index, 
    values=top_sports.values,
    color=top_sports.index,  # Assure que chaque catégorie a une couleur unique
    color_discrete_sequence=px.colors.sequential.Blues  # Palette de bleu dégradé
)

# Modifier l'arrière-plan du graphique pour qu'il soit transparent
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Fond du graphique transparent
    paper_bgcolor='rgba(0,0,0,0)',  # Fond de la feuille transparent
    title_font=dict(size=18, color="#2C3E50"),
)

# Afficher le graphique interactif
fig.write_html("../camembert-repartition-sport-les-plus-representes.html")

#pourquoi ploty : Lisibilité & Simplicité 

#Matplotlib est plus simple et rapide pour ce type de visualisation statique.
#Un diagramme circulaire ne nécessite pas forcément d'interactivité avancée.
# Bokeh n’a pas de pie chart natif 

#Bokeh ne propose pas directement de pie chart (contrairement à Matplotlib et Seaborn).
#Il est possible de le créer avec un patch (forme personnalisée), mais c’est plus compliqué.

