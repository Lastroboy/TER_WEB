import pandas as pd
import plotly.express as px

# Charger le fichier
df = pd.read_csv("./data/activités-sportives-culturelles.csv")

# Extraire le département à partir du code postal
df['departement'] = df['codePostal'].astype(str).str[:2]

# Filtrer les départements d'intérêt
departements_cibles = ['56', '35', '22', '29']
df = df[df['departement'].isin(departements_cibles)]

# Nettoyer les valeurs de la colonne 'ouvertureCovid'
df['ouvertureCovid'] = df['ouvertureCovid'].astype(str).str.lower()
df['ouvertureCovid'] = df['ouvertureCovid'].map({'oui': 'Ouvert', 'non': 'Fermé'})
df['ouvertureCovid'].fillna('Inconnue', inplace=True)

# Compter le nombre d'activités par département et statut
df_counts = df.groupby(['departement', 'ouvertureCovid']).size().reset_index(name='count')

# Ordonner les statuts pour qu'ils apparaissent dans l'ordre souhaité
statut_order = ['Inconnue', 'Fermé', 'Ouvert']
df_counts['ouvertureCovid'] = pd.Categorical(df_counts['ouvertureCovid'], categories=statut_order, ordered=True)

# Trier les départements par total d'activités (du plus petit au plus grand)
dep_order = df_counts.groupby('departement')['count'].sum().sort_values().index.tolist()
df_counts['departement'] = pd.Categorical(df_counts['departement'], categories=dep_order, ordered=True)

# Définir les couleurs personnalisées
couleurs = {'Ouvert': '#ffc107', 'Fermé': '#dc3545', 'Inconnue': '#4c74b5'}

# Tracer l'histogramme interactif
fig = px.bar(df_counts, x='departement', y='count', color='ouvertureCovid',
             labels={'departement': 'Département', 'count': "Nombre d'activités", 'ouvertureCovid': 'Statut'},
             barmode='stack', category_orders={'departement': dep_order, 'ouvertureCovid': statut_order},
             color_discrete_map=couleurs)

# Masquer par défaut les valeurs inconnues tout en les rendant activables dans la légende
fig.for_each_trace(lambda trace: trace.update(visible='legendonly') if trace.name == 'Inconnue' else trace)

# Rendre le fond transparent
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)')

# Affichage du graphique
# fig.show()
fig.write_html("../histogram-ouverture-covid-loisirs-cultures.html")