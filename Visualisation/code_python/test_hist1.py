import csv
import plotly.express as px
import pandas as pd

activites=[]
fm=open("DataClean_activités_culturelles_et_sportives.csv", "r", encoding="utf-8")
for ligne in csv.DictReader(fm, delimiter=","):
    activites.append(ligne)
print(activites[0])
for dico in activites:
    dico["codePostal"] = dico["codePostal"][0:2] 
df = pd.DataFrame.from_dict(activites)
print(df["ouvertureCovid"].unique())
df["ouvertureCovid"] = df["ouvertureCovid"].astype("category")
df["ouvertureCovid"] = df["ouvertureCovid"].replace("", "Unknown")
color_map = {"non": "#f97068", "oui": "#f8cb2e", "Unknown": "#4c74b5"} 
fig = px.histogram(df, x="codePostal", color="ouvertureCovid", color_discrete_map=color_map, category_orders={"ouvertureCovid": ["non", "oui", ""]}).update_xaxes(categoryorder='total ascending')
fig.update_layout(
    xaxis_title="departement",  # Nouveau titre pour l'axe X
    yaxis_title="activites pendant le covid",     # Nouveau titre pour l'axe Y
)
fig.show()