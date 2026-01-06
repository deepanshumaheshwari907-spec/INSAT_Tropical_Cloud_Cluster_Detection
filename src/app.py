import streamlit as st
import pandas as pd

from thresholding import apply_irbt_threshold
from cluster_detect import detect_cloud_clusters
from tcc_filter import is_valid_tcc
from tcc_features import compute_tcc_features
from summary_generator import generate_tcc_summary

# Geo + Tb loader
from insat_reader import load_tb_lat_lon

from streamlit_folium import st_folium
import folium


st.title("INSAT-3D Tropical Cloud Cluster (TCC) Detection")
st.write("Upload INSAT L1C .h5 file to detect cloud clusters")


# ---------- FILE UPLOAD ----------
uploaded = st.file_uploader("Upload INSAT .h5 File", type=["h5"])

if uploaded is None:
    st.info("Please upload a satellite file to continue.")
    st.stop()


# ---------- SAVE TEMP FILE ----------
with open("uploaded_file.h5", "wb") as f:
    f.write(uploaded.getbuffer())

st.success("File uploaded successfully")
st.info("Processing file…" )


# ---------- SAFE LOAD (No Crash on Cloud) ----------
try:
    Tb, lat, lon = load_tb_lat_lon("uploaded_file.h5")
except FileNotFoundError:
    st.error("File could not be read. Try uploading again.")
    st.stop()

# ---------- PIPELINE ----------
# ---------- THRESHOLD CONTROL ----------
st.subheader("Brightness Temperature Threshold (K)")

threshold = st.slider(
    "Select IRBT Threshold",
    min_value=200,
    max_value=260,
    value=235,
    step=1
)

st.info(f"Using {threshold} K as cold cloud threshold")

# generate cloud mask
mask = Tb < threshold
labeled, regions = detect_cloud_clusters(mask)

results = []

for r in regions:
    if is_valid_tcc(r):

        feat = compute_tcc_features(r, Tb, lat, lon)

        # ADD SUMMARY HERE
        feat["summary"] = generate_tcc_summary(feat)

        results.append(feat)



# ---------- NO TCC CASE ----------
if len(results) == 0:
    st.warning("No valid Tropical Cloud Clusters detected in this scene.")
    st.stop()


# ---------- DATAFRAME ----------
df = pd.DataFrame(results)

st.success(f"{len(df)} Tropical Cloud Clusters detected")

st.subheader("Scientific TCC Feature Table")
st.dataframe(df, width='stretch')

# ---------- HUMAN FRIENDLY SUMMARY ----------
st.subheader("Human-Readable Cluster Interpretation")

for i, row in df.iterrows():

    # convection strength meaning
    if row["mean_tb"] < 210:
        strength = "very strong deep convection"
    elif row["mean_tb"] < 230:
        strength = "moderate convective system"
    else:
        strength = "weak / shallow cloud system"

    # size meaning
    if row["mean_radius_km"] > 800:
        size_desc = "very large tropical cloud cluster"
    elif row["mean_radius_km"] > 400:
        size_desc = "large spread convective system"
    else:
        size_desc = "small-to-moderate cloud cluster"

    st.write(f"""
**TCC #{i+1} Summary**

• This is a **{size_desc}**  
• Cloud top indicates **{strength}**  
• Approx spread size: **{row['mean_radius_km']:.1f} km**  
• Coldest cloud temperature: **{row['min_tb']:.2f} K**  
• Center located near **{row['center_lat']:.2f}° , {row['center_lon']:.2f}°**  
""")

    st.divider()


# ---------- MAP VISUALIZATION ----------
st.subheader("TCC Map Visualization")

m = folium.Map(location=[10, 80], zoom_start=5)

for _, row in df.iterrows():

    popup = f"""
    <b>Tropical Cloud Cluster</b><br>
    Mean Tb: {row['mean_tb']:.2f} K<br>
    Pixel Count: {row['pixel_count']:.0f}<br>
    Mean Radius: {row['mean_radius_km']:.1f} km<br>
    Max Radius: {row['max_radius_km']:.1f} km
    """

    folium.Marker(
        location=[row["center_lat"], row["center_lon"]],
        popup=popup,
        icon=folium.Icon(color="red", icon="cloud")
    ).add_to(m)

    folium.Circle(
        location=[row["center_lat"], row["center_lon"]],
        radius=row["mean_radius_km"] * 1000,
        color="blue",
        fill=False
    ).add_to(m)


st_folium(m, width=900, height=600)

