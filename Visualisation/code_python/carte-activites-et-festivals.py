import pandas as pd
import plotly.graph_objects as go
import os

df_activites = pd.read_csv("./activités-sportives-culturelles.csv")
df_festivals = pd.read_csv("./festivals-de-cinema-en-bretagne.csv")

carte = go.Figure()

carte.add_trace(go.Scattermapbox(
    lat = df_activites["latitude"], 
    lon = df_activites["longitude"],
    mode = "markers",
    marker = dict(size = 10, color = "#ffc107"),
    name = "Activités sportives et culturelles"
))

carte.add_trace(go.Scattermapbox(
    lat = df_festivals["latitude"], 
    lon = df_festivals["longitude"],
    mode = "markers",
    marker = dict(size = 10, color = "#4c74b5"),
    name = "Festivals de cinéma"
))

carte.update_layout(
    mapbox = dict(
        style = "open-street-map",
        zoom = 7,
        center = dict(lat = df_activites["latitude"].mean(), lon = df_activites["longitude"].mean())
    ),
    margin = dict(l = 0, r = 0, t = 0, b = 0),
    legend = dict(x = 0, y = 1)
)

# carte.show()

carte.write_html("Graphes\GraphesTerminés\carte-activites-et-festivals.html")

# Je me suis aidé de "https://plotly.com/python/maps/"