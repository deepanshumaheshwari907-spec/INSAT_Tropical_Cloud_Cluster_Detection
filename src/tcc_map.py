import folium
import pandas as pd

print("Loading CSV...")
df = pd.read_csv("tcc_results.csv")

# Center map around India region
m = folium.Map(location=[10, 80], zoom_start=5)

print("Plotting TCCs on map...")

for _, row in df.iterrows():

    lat = row["center_lat"]
    lon = row["center_lon"]

    popup_text = f"""
    <b>Tropical Cloud Cluster</b><br>
    Pixel Count: {row['pixel_count']:.0f}<br>
    Mean Tb: {row['mean_tb']:.2f} K<br>
    Min Tb: {row['min_tb']:.2f} K<br>
    Mean Radius: {row['mean_radius_km']:.1f} km<br>
    Max Radius: {row['max_radius_km']:.1f} km<br>
    """

    # marker at center
    folium.Marker(
        location=[lat, lon],
        popup=popup_text,
        icon=folium.Icon(color="red", icon="cloud")
    ).add_to(m)

    # draw radius circle
    folium.Circle(
        location=[lat, lon],
        radius=row["mean_radius_km"] * 1000,   # km -> meters
        color="blue",
        fill=False
    ).add_to(m)

# save map file
m.save("tcc_map.html")

print("\nMap generated:  tcc_map.html")
print("Open file in browser to view map.")
