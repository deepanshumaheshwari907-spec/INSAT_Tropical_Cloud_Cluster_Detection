# 🌩 INSAT-3D Tropical Cloud Risk Intelligence Platform

A **satellite-based applied AI system** that detects, analyzes, and prioritizes  
**tropical convective cloud systems** using real **INSAT-3D Infrared Brightness Temperature (IRBT)** data.

This project demonstrates how **raw satellite observations** can be transformed into  
**actionable weather-risk intelligence** through scientific processing, feature extraction,  
and an interactive decision-support dashboard.

---

## 🚀 Live Demo

👉 **Live Application:** (Streamlit Cloud link here)

The application includes a **built-in demo mode**, allowing anyone to explore the platform  
without uploading satellite data files.

---

## 🎯 What does this platform do?

• Detects cold convective cloud clusters from INSAT-3D IR satellite imagery  
• Identifies valid **Tropical Cloud Clusters (TCCs)** using spatial and structural rules  
• Extracts physically meaningful scientific features from each cluster  
• Assigns **severity and risk scores** to prioritize hazardous systems  
• Presents results via an **interactive dashboard and geospatial map**  

The focus is on **interpretability and risk awareness**, not black-box prediction.

---

## 🛰 Satellite Data Details

**Source:** ISRO / MOSDAC  
**Satellite:** INSAT-3D  
**Sensor:** Imager  
**Product Type:** L1C – SGP  
**Channel Used:** Infrared (Brightness Temperature)  
**Temporal Resolution:** 30-minute interval  
**Input Format:** `.h5` satellite file  

---

## 🧠 Processing Workflow

1️⃣ Load INSAT-3D L1C IR brightness temperature data  
2️⃣ Apply cold-cloud IRBT threshold  
3️⃣ Detect connected convective cloud regions  
4️⃣ Filter valid Tropical Cloud Clusters (TCCs)  
5️⃣ Extract cluster-level scientific features  
6️⃣ Classify severity and compute risk scores  
7️⃣ Visualize insights through dashboard & map  

---

## 📊 Key Features Extracted (Per Cluster)

• Pixel count (spatial coverage)  
• Mean, minimum & median brightness temperature  
• Temperature standard deviation  
• Cluster center latitude & longitude  
• Minimum, maximum & mean radius (km)  
• Severity classification (Mild / Moderate / Severe)  
• Risk score and priority level  

---

## 🧪 Application Capabilities

✔ Built-in demo mode (no satellite file required)  
✔ Adjustable IRBT threshold  
✔ Cluster-wise scientific feature table  
✔ Risk-prioritized Top-3 cloud systems  
✔ Human-readable interpretation summaries  
✔ Interactive geospatial visualization  
✔ CSV export of detection results  

---

## 👥 Who is this platform for?

• Weather and climate researchers  
• Remote sensing and satellite-data students  
• Disaster and risk monitoring analysts  
• Recruiters evaluating applied AI / data science skills  

---

## 🛠 Tools & Technologies

• Python  
• NumPy, Pandas  
• h5py  
• Scikit-image  
• Folium / Leaflet  
• Streamlit  

---

## 📌 Project Status

This platform is a **working research and product prototype**.

It successfully processes **real INSAT-3D satellite data** to:
• Detect tropical convective cloud systems  
• Extract scientifically meaningful parameters  
• Provide interpretable risk intelligence  
• Demonstrate real-world applied AI development  

---

## 🔮 Planned Enhancements

• Multi-timestamp cloud tracking  
• Time-series analysis of cloud evolution  
• Automated MOSDAC data ingestion  
• Cyclogenesis precursor analysis  
• API-based integration for weather platforms  

---

## 👨‍💻 Author

**Developed by:** Deepanshu Maheshwari  
Applied AI | Satellite Data | Weather Intelligence  

This project reflects a strong interest in building  
**real-world AI systems using geospatial and satellite data**.

---

## 🙌 Acknowledgements

Satellite Data Source — ISRO / MOSDAC  
Satellite Platform — INSAT-3D Imager  
