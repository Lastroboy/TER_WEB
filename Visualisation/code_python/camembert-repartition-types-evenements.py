import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



# Charger le fichier CSV dans un DataFrame
df = pd.read_csv("./fetes_et_manifestations.csv", delimiter=",")  # Changer le délimiteur si nécessaire (ex: ',' ou '\t')


# Afficher les premières lignes
print(df.head())

# Gérer les valeurs manquantes ou invalides et extraire le premier mot de la colonne 'TypeCategorie'
df['PremierMotCategorie'] = df['TypeCategorie'].apply(lambda x: str(x).split()[0] if isinstance(x, str) and x else 'Inconnu')

# Comptage des occurrences de chaque premier mot
categorie_counts = df['PremierMotCategorie'].value_counts()

# Filtrer pour ne garder que les 5 premières catégories les plus représentées
top_5_categories = categorie_counts.head(5)

# Calculer la proportion pour chaque catégorie
total_events = top_5_categories.sum()
top_5_proportions = top_5_categories / total_events  # Proportions des catégories

# Définir une palette de couleurs rouges pour le graphique (dégradé de rouge)
color_sequence = ['#ffcccc', '#ff9999', '#ff6666', '#ff3333', '#ff0000']  # Dégradé de rouge clair à foncé

# Créer le graphique en camembert (pie chart) avec dégradé de rouge
fig = px.pie(names=top_5_proportions.index, values=top_5_proportions.values, 
             labels={'value': 'Proportion d\'événements', 'names': 'Premier mot de catégorie'},
             color=top_5_proportions.index,  # Assigner les couleurs en fonction des catégories
             color_discrete_sequence=color_sequence)  # Utilisation de la palette de couleurs rouge

# Modifier l'arrière-plan du graphique pour qu'il soit transparent
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',  # Fond du graphique transparent
    paper_bgcolor='rgba(0,0,0,0)',  # Fond de la feuille transparent
    title_font=dict(size=18, color="#2C3E50"),
)

# Afficher le graphique
fig.write_html("../camembert-repartition-types-evenements.html")