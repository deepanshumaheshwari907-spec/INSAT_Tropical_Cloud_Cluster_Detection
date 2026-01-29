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
# ================= GLOBAL UI STYLE =================
st.markdown("""
<style>
/* Full page background */
.stApp {
    background: radial-gradient(circle at top, #0b1c2d, #020814);
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0e1625, #070b13);
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: linear-gradient(180deg, #0f172a, #020617);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 18px;
}

/* Section divider */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #4da3ff, transparent);
    margin: 28px 0;
}
</style>
""", unsafe_allow_html=True)


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
    st.markdown("### 🎛 System Controls")
    st.caption("Configure detection parameters and data source")

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
    


# ================= HERO =================
st.markdown(
    "## 🌩 INSAT-3D Tropical Cloud Risk Intelligence"
)

st.markdown(
    "**Satellite-based system to detect, analyze, and prioritize hazardous tropical cloud systems**"
)

st.write(
    "This platform uses real INSAT-3D infrared brightness temperature data and applied AI techniques "
    "to identify tropical cloud clusters, assess their intensity, and generate risk-oriented insights "
    "for research and decision support."
)
st.info(
    "🛰 Live Analysis Mode • Satellite IR data processed in real-time for cloud risk assessment"
)
# ================= LANDING INFO =================
st.markdown("## 👥 Who is this platform for?")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    **🌦 Weather & Climate Researchers**  
    Analyze tropical convective cloud systems using real satellite data.
    """)

with c2:
    st.markdown("""
    **🛰 Remote Sensing Students**  
    Learn how INSAT-3D infrared data is processed and interpreted.
    """)

with c3:
    st.markdown("""
    **⚠ Disaster & Risk Analysts**  
    Identify potentially hazardous cloud systems for early attention.
    """)
st.markdown("## ✨ What makes this platform different?")

st.markdown("""
• Uses **real INSAT-3D satellite data** (no dummy or toy datasets)  
• Focuses on **interpretability**, not black-box AI  
• Converts satellite observations into **risk-oriented intelligence**  
• Can be explored instantly using a **built-in demo scene**
""")

st.divider()
st.info(
    "🚀 You are viewing a live prototype of an INSAT-3D based cloud risk intelligence platform. "
    "This system is under active development and demonstrates how satellite data can be "
    "converted into actionable weather insights."
)

# ================= DATA LOADING (IMPORTANT PART) =================
st.markdown("### ⚡ Quick Demo")

run_demo = st.button("▶ Run 30-second Demo")

if run_demo:
    st.success("Demo started • Using built-in INSAT-3D satellite scene")

if data_source == "Demo File (Built-in)":

    demo_path = os.path.join("data", "demo_insat.h5")

    if not os.path.exists(demo_path):
        st.error("Demo INSAT file not found in data/demo_insat.h5")
        st.stop()

    st.success("✔ Running in DEMO mode using a preloaded INSAT-3D satellite scene")
    Tb, lat, lon = load_tb_lat_lon(demo_path)

else:
    st.markdown("## 🚀 Upload INSAT File")
    uploaded = st.file_uploader("Upload INSAT-3D L1C .h5 File", type=["h5"])

    if uploaded is None:
        st.info("Please upload a satellite file to continue.")
        st.stop()

    with open("uploaded_file.h5", "wb") as f:
        f.write(uploaded.getbuffer())

    Tb, lat, lon = load_tb_lat_lon("uploaded_file.h5")


# ================= PROCESS =================
mask = Tb < threshold
_, regions = detect_cloud_clusters(mask)

with st.spinner("Analyzing satellite data and detecting cloud systems..."):
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
st.markdown("## 🧠 How to read this dashboard")

st.write("""
This system analyzes **infrared satellite data** to detect **cold, deep convective cloud clusters**.

• **Lower temperature (Tb)** → stronger convection  
• **Larger radius** → wider cloud spread  
• **Higher risk score** → potentially dangerous weather system  

The dashboard highlights **high-priority tropical cloud systems** that may require closer monitoring.
""")

st.caption(
    "INSAT-3D Tropical Cloud Risk Intelligence Platform • Experimental decision-support system"
)
st.markdown("""
<div style="
    font-size:26px;
    font-weight:600;
    margin-top:40px;
    margin-bottom:10px;
    color:#ffffff;
">
📊 Detection Dashboard
</div>
""", unsafe_allow_html=True)


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
st.markdown("""
<div style="
    font-size:26px;
    font-weight:600;
    margin-top:50px;
    margin-bottom:14px;
    color:#ff4d4d;
">
🚨 High-Priority Tropical Cloud Systems
</div>
""", unsafe_allow_html=True)


top3 = df.head(3)
for i, row in top3.iterrows():
    st.markdown(
        f"""
        🚨 **ALERT SYSTEM #{i+1}**
        • Risk Level: **{row['risk_level']}**  
        • Risk Score: **{row['risk_score']} / 100**  
        • Mean Tb: **{row['mean_tb']:.1f} K**  
        • Radius: **{row['mean_radius_km']:.0f} km**
        """
    )

st.divider()
if run_demo:
    st.caption("📌 Demo mode highlights the most significant cloud systems in this scene")


# ================= TABLE =================
st.warning(
    "⚠ Scientific values are derived from satellite pixel analysis and intended for research and experimental use."
)

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
st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#9aa4b2;
        font-size:13px;
        padding:16px;
    ">
        INSAT-3D Tropical Cloud Risk Intelligence Platform<br>
        Built using real satellite data for applied AI & weather intelligence<br>
        <span style="font-size:12px;">
        Developed by Deepanshu Maheshwari • Experimental research & product prototype
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

