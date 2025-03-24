import csv
import pandas as pd
import plotly.express as px

fetes_manifs=[]
fm=open("DataClean_bretagne_fetes_et_manifestations.csv", "r", encoding="utf-8")
for ligne in csv.DictReader(fm, delimiter=","):
    fetes_manifs.append(ligne)
print(fetes_manifs[0])
df = pd.DataFrame.from_dict(fetes_manifs)
df['Published'] = df['Published'].str.replace(',', '.', regex=False)
df['Published'] = pd.to_datetime(df['Published'], format='%Y-%m-%dT%H:%M:%S', errors='coerce')
df['DateOnly'] = df['Published'].dt.date
df_grouped = df.groupby('DateOnly').size().reset_index(name='NombreFestivals')
print(df_grouped)
df_grouped['NombreFestivals'] = df_grouped['NombreFestivals'].rolling(window=7, min_periods=1).mean()
fig = px.line(df_grouped, x='DateOnly', y = "NombreFestivals")
fig.update_layout(
    xaxis_title="date",  # Nouveau titre pour l'axe X
    yaxis_title="nombre de festivals",     # Nouveau titre pour l'axe Y
)
fig.show()
