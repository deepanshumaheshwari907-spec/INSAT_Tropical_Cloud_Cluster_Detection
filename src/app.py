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

def format_lat_lon(lat, lon):
    lat_dir = "N" if lat >= 0 else "S"
    lon_dir = "E" if lon >= 0 else "W"
    return f"{abs(lat):.1f}°{lat_dir}, {abs(lon):.1f}°{lon_dir}"


def approximate_region(lat, lon):
    if 5 <= lat <= 22 and 80 <= lon <= 95:
        return "Bay of Bengal"
    if 5 <= lat <= 25 and 60 <= lon <= 75:
        return "Arabian Sea"
    if 18 <= lat <= 28 and 72 <= lon <= 82:
        return "Central India"
    if 8 <= lat < 18 and 75 <= lon <= 85:
        return "South India"
    return "Open Region"

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("### 🎮 Control Panel")
    st.caption("Configure detection parameters and data source")

    st.caption("Adjust settings for cloud detection")

    data_source = st.radio(
        "Data Source",
        ["Demo File (Built-in)", "Upload Your Own File"],
        index=0
    )

    threshold = st.slider(
    "Cloud Detection Sensitivity (Temperature)",
    200, 260, 235, 1,
    help="Lower value = only very cold and strong clouds detected"
    )



    st.caption(f"Cold clouds detected below {threshold} K")
    


# ================= HERO =================
st.markdown("## 🚨 Tropical Cloud Early Warning")
st.caption("INSAT-3D satellite based extreme weather alert system")


st.caption(
    "Detect high-risk tropical cloud systems from INSAT-3D satellite data "
    "before they turn into extreme weather events."
)

st.info("🛰 Live INSAT-3D Satellite Monitoring • Real-time risk assessment")


# ================= DATA LOADING (IMPORTANT PART) =================
st.markdown("### ⚡ Quick Demo")

run_demo = st.button("▶ Play Risk Scenario")

if run_demo:
    st.warning(
        "🌀 Scenario running: Rapid cloud cooling detected → Risk increasing → Alert generation in progress"
    )

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


# ================= LANDING INFO =================
#st.markdown("## 👥 Who is this platform for?")

#c1, c2, c3 = st.columns(3)

#with c1:
#   st.markdown("""
#  **🌦 Weather & Climate Researchers**  
#    Analyze tropical convective cloud systems using real satellite data.
#    """)

#with c2:
#    st.markdown("""
#    **🛰 Remote Sensing Students**  
#    Learn how INSAT-3D infrared data is processed and interpreted.
#    """)

#with c3:
#    st.markdown("""
#    **⚠ Disaster & Risk Analysts**  
#    Identify potentially hazardous cloud systems for early attention.
#    """)
#st.markdown("## ✨ What makes this platform different?")

#st.markdown("""
#• Uses **real INSAT-3D satellite data** (no dummy or toy datasets)  
#• Focuses on **interpretability**, not black-box AI  
#• Converts satellite observations into **risk-oriented intelligence**  
#• Can be explored instantly using a **built-in demo scene**
#""")

#st.divider()
#st.info(
#    "🚀 You are viewing a live prototype of an INSAT-3D based cloud risk intelligence platform. "
#    "This system is under active development and demonstrates how satellite data can be "
#    "converted into actionable weather insights."
#)

# ================= DATAFRAME =================
df = pd.DataFrame(results)
df = df.sort_values(by="risk_score", ascending=False).reset_index(drop=True)

main_alert = df.iloc[0]

coord_text = format_lat_lon(
    main_alert['center_lat'],
    main_alert['center_lon']
)

region_text = approximate_region(
    main_alert['center_lat'],
    main_alert['center_lon']
)


st.error(
f"""
🚨 EXTREME WEATHER WARNING

A high-risk tropical cloud system has been detected
by INSAT-3D satellite monitoring.

📍 Location: {coord_text} ({region_text})  
🌡 Cloud Temperature: {main_alert['mean_tb']:.1f} K  
📐 Cloud Radius: {main_alert['mean_radius_km']:.0f} km  

⚠ Risk Level: {main_alert['risk_level']}  
🔥 Risk Score: {main_alert['risk_score']} / 100  

💥 Possible Impact:
Heavy Rainfall • Thunderstorm • Flooding
"""
)
st.success("🛰 System Status: Active • Monitoring tropical cloud systems")
st.markdown("---")

st.warning(
    "⚠️ Disclaimer: This system is an experimental research prototype developed for "
    "academic and exploratory purposes. It is **not an operational weather forecasting "
    "or official early warning system**."
)

with st.expander("🔍 View System Scope & Responsibility"):
    
    st.markdown("### System Scope & Responsibility")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="
                background:#0f172a;
                border-left:6px solid #22c55e;
                padding:18px;
                border-radius:12px;
                height:100%;
            ">
            <h4>✅ What this system <b>DOES</b></h4>
            <ul>
                <li>Detects <b>cold, deep convective cloud clusters</b> using INSAT-3D infrared data</li>
                <li>Analyzes cloud properties such as <b>temperature, size, and spatial spread</b></li>
                <li>Assigns a <b>relative risk score</b> to prioritize potentially hazardous systems</li>
                <li>Presents results as <b>alerts, maps, and summaries</b></li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="
                background:#0f172a;
                border-left:6px solid #ef4444;
                padding:18px;
                border-radius:12px;
                height:100%;
            ">
            <h4>❌ What this system <b>DOES NOT</b> do</h4>
            <ul>
                <li>Does <b>not</b> predict exact rainfall amounts or cyclone landfall</li>
                <li>Does <b>not</b> replace official weather forecasts or warning agencies</li>
                <li>Does <b>not</b> claim operational or real-time forecasting accuracy</li>
                <li>Does <b>not</b> issue certified public alerts</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# ================= MAP =================
st.subheader("🗺 Impact Area of Active Weather Warning")
st.caption(
    "The map below shows the possible spatial influence of the detected high-risk cloud system"
)

st.info("🔴 Red circles = High risk | 🟡 Medium | 🟢 Low risk")
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

# ================= DASHBOARD =================
st.subheader("🧠 How to Read This Dashboard")

st.write(
    "This system continuously monitors **infrared satellite data** to identify "
    "**dangerous tropical cloud systems** before they evolve into extreme weather events."
)

st.markdown(
    """
    **What the system looks for:**

    • 🌡 **Colder clouds** → stronger vertical convection  
    • 📐 **Larger cloud spread** → wider area of possible impact  
    • ⚠️ **Higher risk score** → greater likelihood of hazardous weather  

    The dashboard automatically **prioritizes the most critical cloud systems**, "
    "so attention is focused where risk is highest.
    """
)

st.caption(
    "🛰 INSAT-3D Tropical Cloud Early Warning • Experimental decision-support prototype"
)

st.markdown("---")

st.markdown(
    "<div style='font-size:24px; font-weight:600;'>📊 Live Detection Overview</div>",
    unsafe_allow_html=True
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("🌀 Detected Clusters", len(regions))

with c2:
    st.metric("✅ Valid Cloud Systems", len(df))

with c3:
    st.metric(
        "🌡 Avg Cloud Temp (K)",
        f"{df['mean_tb'].mean():.1f}",
        help="Lower temperature indicates stronger convective activity"
    )

with c4:
    st.metric(
        "📐 Max Cloud Radius (km)",
        f"{df['max_radius_km'].max():.0f}",
        help="Represents the widest spatial spread among detected systems"
    )

with c5:
    st.metric(
        "🚨 Highest Risk Score",
        f"{df['risk_score'].max():.1f}",
        help="The most potentially dangerous cloud system in the current scene"
    )


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

st.markdown("## 🚨 LIVE WEATHER ALERTS")
st.caption("High-risk tropical cloud systems detected from satellite data")

with st.expander("⚠️ View Other High-Risk Cloud Systems"):
    top3 = df.head(3)
    for i, row in top3.iterrows():

        coord_text = format_lat_lon(
            row['center_lat'],
            row['center_lon']
        )

        st.warning(
            f"""
            ⚠️ **TCC #{i+1}**

            📍 Location: {coord_text}  
            ⚠ Risk Score: {row['risk_score']} / 100  
            ⏱ Trend: {row['trend']}
            """
        )

st.divider()
if run_demo:
    st.caption("📌 Demo mode highlights the most significant cloud systems in this scene")


# ================= TABLE =================
st.warning(
    "⚠ Scientific values are derived from satellite pixel analysis and intended for research and experimental use."
)

st.caption("🔬 Detailed scientific data (for researchers & analysis)")
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
if False:
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

show_all = st.checkbox("🔽 Show all detected cloud systems")

if show_all:
    display_df = df
else:
    display_df = df.head(6)

st.subheader("🧠 Cloud Risk Summary")

cards_per_row = 3
rows = [display_df.iloc[i:i+cards_per_row] for i in range(0, len(display_df), cards_per_row)]

for row_group in rows:
    cols = st.columns(3)
    for col, (_, row) in zip(cols, row_group.iterrows()):
        with col:
            st.markdown(
                f"""
                <div style="
                    background:#111;
                    border-left:5px solid {get_risk_color(row['risk_level'])};
                    padding:14px;
                    border-radius:10px;
                    margin-bottom:16px;
                ">
                <b>⚠️ TCC</b><br>
                🌡 Temp: {row['mean_tb']:.1f} K<br>
                📐 Radius: {row['mean_radius_km']:.0f} km<br>
                ⚠ Risk: {row['risk_level']}<br>
                </div>
                """,
                unsafe_allow_html=True
            )


st.markdown(
    """
    <div style="
        text-align:center;
        color:#9aa4b2;
        font-size:13px;
        padding:18px;
        margin-top:30px;
    ">
        🛰 <b>INSAT-3D Tropical Cloud Early Warning System</b><br>
        Turning satellite observations into early-warning intelligence<br>
        <span style="font-size:12px;">
        Built & developed by Deepanshu Maheshwari • Experimental research & product prototype
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

