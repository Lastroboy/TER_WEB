import pandas as pd
import plotly.express as px

df = pd.read_csv("./Visualisation/code_python/data/festivals-de-cinema-en-bretagne.csv")  
colonne_interet = "Aidé par la Région Bretagne"  

data = df[colonne_interet].value_counts().reset_index()
data.columns = ["Catégorie", "Nombre"]

fig = px.pie(data,
             names = "Catégorie",
             values = "Nombre",
             # title = "Gratuité des évènements",
             color_discrete_sequence = px.colors.sequential.Blues[4:]
             )

fig.update_traces(textinfo="percent+label",  
                  hovertemplate = colonne_interet + " : " + "%{label}" + "<br>"
                                  "Nombre : " + "%{value}")
fig.show()

# fig.write_html("./Visualisation/camembert-nb-festivals-aides-par-region.html")

# Je me suis aidé de "https://plotly.com/python/pie-charts/"