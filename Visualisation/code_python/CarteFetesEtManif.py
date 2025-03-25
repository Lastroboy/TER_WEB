import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("Graphes/GraphesTerminés/fetes-et-manifestations-nettoyé.csv")


carte = go.Figure()

carte.add_trace(go.Scattermapbox(
    lat = df["Latitude"], 
    lon = df["Longitude"],
    mode = "markers",
    marker = dict(size = 10, color = "#4C74B5"),
    name = "Fetes et manifestations",
    text = df["ObjectName"] +", "+ df["Commune"],
    hoverinfo = "text"
))

carte.update_layout(
    mapbox = dict(
        style = "open-street-map",
        zoom = 7,
        center = dict(lat = df["Latitude"].mean(), lon = df["Longitude"].mean())
    ),
    margin = dict(l = 0, r = 0, t = 0, b = 0),
)

# carte.show()

carte.write_html("Graphes\GraphesTerminés\CarteFetesEtManifestations.html")

# Je me suis aidé de "https://plotly.com/python/maps/"