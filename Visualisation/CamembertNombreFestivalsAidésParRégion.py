import pandas as pd
import plotly.express as px

df = pd.read_csv("Graphes/festivals-de-cinema-en-bretagne-nettoyé.csv")  
colonne_interet = "Aidé par la Région Bretagne"  

data = df[colonne_interet].value_counts().reset_index()
data.columns = ["Catégorie", "Nombre"]

fig = px.pie(data,
             names = "Catégorie",
             values = "Nombre",
             # title = "Gratuité des évènements",
             color_discrete_sequence = px.colors.sequential.Blues[4:]
             )

# fig.show()

fig.write_html("Graphes\GraphesTerminés\CamembertNombreFestivalsAidésParRégion.html")

# Je me suis aidé de "https://plotly.com/python/pie-charts/"