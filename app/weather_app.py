import folium
import streamlit as st
import geopandas as gpd
import requests
from shapely import wkt

from streamlit_folium import folium_static

r = requests.get("http://fastapi-container-prod:8000/")

data = r.json()

m = folium.Map(location=[40, -77], zoom_start=5)

# Prepare lists to hold data for GeoDataFrame
geometries = []
properties = []

for item in data:
    # Extract the WKT string and convert it to a Shapely geometry object
    geometry = wkt.loads(item['geom'])
    geometries.append(geometry)

    # Store other properties
    properties.append({
        'name': item['name'],
        'state': item['state'],
        'first_period': item['first_period'],
        'second_period': item['second_period'],
        'first_forecast': item['first_forecast'].split(".")[0],
        'second_forecast': item['second_forecast'].split(".")[0]
    })

# Create the GeoDataFrame
gdf = gpd.GeoDataFrame(properties, geometry=geometries, crs="EPSG:4326")

for _, r in gdf.iterrows():
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j)
    text = f"""
    <b>Name:</b> {r["name"]}
    <b>State:</b> {r["state"]}
    <b>{r["first_period"]}'s Forecast:</b> {r["first_forecast"]}
    <b>{r["second_period"]}'s Forecast:</b> {r["second_forecast"]}"""
    folium.Popup(text).add_to(geo_j)
    geo_j.add_to(m)

# display the map in Streamlit
st.title("Mid-Atlantic Weather Map 🌦️")
folium_static(m, width=1000)
