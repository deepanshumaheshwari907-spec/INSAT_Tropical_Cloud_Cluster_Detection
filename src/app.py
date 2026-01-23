import os
import streamlit as st
import pandas as pd

from cluster_detect import detect_cloud_clusters
from tcc_filter import is_valid_tcc
from tcc_features import compute_tcc_features
from severity import classify_severity
from summary_generator import generate_tcc_summary
from insat_reader import load_tb_lat_lon

from streamlit_folium import st_folium
import folium


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="INSAT-3D Tropical Cloud Risk Intelligence",
    layout="wide"
)


# ================= HELPERS =================
def get_risk_color(level):
    if level == "Extreme":
        return "#ff4d4d"
    elif level == "High":
        return "#ff9933"
    elif level == "Medium":
        return "#ffd633"
    else:
        return "#66cc66"


def get_trend_icon(trend):
    if trend == "Intensifying":
        return "🔺"
    elif trend == "Weakening":
        return "🔻"
    else:
        return "⏸️"


# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## ⚙ Analysis Controls")

    data_source = st.radio(
        "Data Source",
        ["Demo File (Built-in)", "Upload Your Own File"],
        index=0
    )

    threshold = st.slider(
        "IR Brightness Temperature Threshold (K)",
        200, 260, 235, 1
    )

    st.caption(f"Cold clouds detected below {threshold} K")


# ================= HERO SECTION =================
st.markdown("""
<div style="
    max-width:1100px;
    margin:auto;
    text-align:center;
    padding:40px 20px;
    background: linear-gradient(180deg, #0b1c2d, #020814);
    border-radius:16px;
">
    <h1 style="color:#4da3ff; font-size:42px;">
        🌩 INSAT-3D Tropical Cloud Risk Intelligence
    </h1>

    <h3 style="color:#d0d7e2; font-weight:400;">
        Satellite-based detection & risk assessment of tropical convective cloud systems
    </h3>

    <p style="color:#9fb3c8; margin-top:14px;">
        Uses real INSAT-3D L1C infrared brightness temperature data to detect,
        classify and prioritize hazardous tropical cloud clusters.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ================= FEATURES =================
st.markdown("## 🔍 What this system provides")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**🛰 Satellite Detection**  \nDetects cold convective cloud clusters from INSAT-3D IR data.")

with c2:
    st.markdown("**⚠ Risk Intelligence**  \nAssigns severity, risk score and trend to prioritize dangerous systems.")

with c3:
    st.markdown("**🗺 Visual Monitoring**  \nInteractive map showing location, spread and risk intensity of TCCs.")


# ================= UPLOAD =================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("## 🚀 Start Analysis")
st.markdown("Upload an **INSAT-3D L1C `.h5` satellite file** to begin analysis.")

uploaded = st.file_uploader("Upload INSAT .h5 File", type=["h5"])

if uploaded is None:
    st.info("Please upload a satellite file to continue.")
    st.stop()

with open("uploaded_file.h5", "wb") as f:
    f.write(uploaded.getbuffer())

st.success("File uploaded successfully")
st.info("⏳ Processing INSAT-3D satellite data. Please wait…")


# ================= LOAD DATA =================
try:
    Tb, lat, lon = load_tb_lat_lon("uploaded_file.h5")
except FileNotFoundError:
    st.error("File could not be read.")
    st.stop()


# ================= PROCESS =================
mask = Tb < threshold
_, regions = detect_cloud_clusters(mask)

results = []
for r in regions:
    if is_valid_tcc(r):
        feat = compute_tcc_features(r, Tb, lat, lon)
        feat["severity"] = classify_severity(feat["min_tb"])
        feat["summary"] = generate_tcc_summary(feat)
        results.append(feat)

if len(results) == 0:
    st.warning("No valid Tropical Cloud Clusters detected.")
    st.stop()


# ================= DATAFRAME =================
df = pd.DataFrame(results)
df = df.sort_values(by="risk_score", ascending=False).reset_index(drop=True)


# ================= DASHBOARD =================
st.markdown("## 📊 Detection Dashboard")

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.metric("Detected Clusters", len(regions))
with c2:
    st.metric("Valid TCCs", len(df))
with c3:
    st.metric("Avg Tb (K)", f"{df['mean_tb'].mean():.1f}")
with c4:
    st.metric("Max Radius (km)", f"{df['max_radius_km'].max():.0f}")
with c5:
    st.metric("Highest Risk", f"{df['risk_score'].max():.1f}")


# ================= TOP-3 =================
st.markdown("## 🚨 Top-3 High-Risk Tropical Cloud Systems")

top3 = df.head(3)
for i, row in top3.iterrows():
    st.markdown(
        f"""
        🔴 **Priority #{i+1}**  
        • Risk Level: **{row['risk_level']}**  
        • Risk Score: **{row['risk_score']} / 100**  
        • Mean Tb: **{row['mean_tb']:.1f} K**  
        • Radius: **{row['mean_radius_km']:.0f} km**
        """
    )

st.divider()


# ================= TABLE =================
st.subheader("Scientific TCC Feature Table")
st.dataframe(df, use_container_width=True)

st.download_button(
    "⬇ Download CSV",
    df.to_csv(index=False).encode("utf-8"),
    "TCC_results.csv",
    "text/csv"
)


# ================= RISK SUMMARY =================
st.subheader("TCC Risk Intelligence Summary")

for i, row in df.iterrows():
    color = get_risk_color(row["risk_level"])

    st.markdown(
        f"""
        <div style="
            border-left:6px solid {color};
            padding:14px;
            margin-bottom:10px;
            background:#111;
            border-radius:6px
        ">
        <b>TCC #{i+1}</b><br>
        Severity: {row['severity']}<br>
        Risk Level: {row['risk_level']}<br>
        Risk Score: {row['risk_score']}<br>
        Trend: {row['trend']} {get_trend_icon(row['trend'])}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(row["risk_score"] / 100)
    st.divider()


# ================= MAP =================
st.subheader("Risk-Aware TCC Map")

m = folium.Map(location=[10, 80], zoom_start=5)

for idx, row in df.iterrows():
    color = get_risk_color(row["risk_level"])
    weight = 5 if idx < 3 else 1
    opacity = 0.45 if idx < 3 else 0.2

    folium.Circle(
        location=[row["center_lat"], row["center_lon"]],
        radius=row["mean_radius_km"] * 1000,
        color=color,
        weight=weight,
        fill=True,
        fill_opacity=opacity,
        popup=f"""
        <b>TCC #{idx+1}</b><br>
        Risk: {row['risk_level']} ({row['risk_score']})<br>
        Trend: {row['trend']}
        """
    ).add_to(m)

st_folium(m, width=1100, height=600)
