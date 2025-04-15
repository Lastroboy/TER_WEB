import plotly.graph_objects as go

# Coordonnées de l'Université de Rennes 2
lat = 48.119826
lon = -1.701728

# Création de la figure
fig = go.Figure(go.Scattermapbox(
    lat=[lat],
    lon=[lon],
    mode='markers+text',
    marker=go.scattermapbox.Marker(size=16, color='#4c74b5'),
    text=['Université de Rennes 2'],
    textposition='top right',
    textfont=dict(color='#4c74b5', size=14)
))

# Configuration du layout
fig.update_layout(
    mapbox=dict(
        style='open-street-map',
        center=dict(lat=lat, lon=lon),
        zoom=15
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)

# Affichage
# fig.show()
fig.write_html("./carte-universite-rennes2.html")

