# 🌩 INSAT-3D Tropical Cloud Early Warning System

An **experimental research prototype** that analyzes INSAT-3D infrared satellite data  
to detect, analyze, and prioritize **tropical convective cloud systems**.

This project explores how **raw satellite observations** can be transformed into  
**early situational awareness and risk-oriented intelligence** using interpretable methods.

---

## 🚀 Live Demo

👉 **Live Application:** (https://insattropicalcloudclusterdetection-eumm4o7mcqwbpdirjd5iec.streamlit.app/)

The application includes a **built-in demo mode**, allowing users to explore the system  
without uploading satellite data files.

---

## 🎯 What does this system do?

• Detects cold convective cloud clusters from INSAT-3D infrared imagery  
• Identifies valid **Tropical Cloud Clusters (TCCs)** using spatial rules  
• Extracts scientifically meaningful features from each cluster  
• Assigns **relative risk scores** to prioritize potentially hazardous systems  
• Presents results via an **interactive dashboard and geospatial map**

The focus is on **interpretability and early risk awareness**, not black-box prediction.

---

## 🛰 Satellite Data Details

**Source:** ISRO / MOSDAC  
**Satellite:** INSAT-3D  
**Sensor:** Imager  
**Product Type:** L1C – SGP  
**Channel Used:** Infrared (Brightness Temperature)  
**Temporal Resolution:** 30-minute interval  
**Input Format:** `.h5`

---

## 🧠 Processing Workflow

1️⃣ Load INSAT-3D L1C infrared brightness temperature data  
2️⃣ Apply cold-cloud temperature threshold  
3️⃣ Detect connected convective cloud regions  
4️⃣ Filter valid Tropical Cloud Clusters (TCCs)  
5️⃣ Extract cluster-level scientific features  
6️⃣ Compute severity and relative risk scores  
7️⃣ Visualize insights through dashboard and map  

---

## 📊 Key Features Extracted (Per Cluster)

• Mean and minimum brightness temperature  
• Spatial coverage and radius (km)  
• Cluster center latitude and longitude  
• Severity classification  
• Relative risk score and priority level  

---

## 🧪 Application Capabilities

✔ Built-in demo mode  
✔ Adjustable temperature threshold  
✔ Cluster-wise scientific feature table  
✔ Risk-prioritized alerts  
✔ Human-readable summaries  
✔ Interactive geospatial visualization  
✔ CSV export of results  

---

## 👥 Intended Audience

• Weather and climate researchers  
• Remote sensing and satellite-data students  
• Disaster and risk monitoring analysts  
• Technical evaluators reviewing applied geospatial AI systems  

---

## 🛠 Tools & Technologies

• Python  
• NumPy, Pandas  
• h5py  
• Scikit-image  
• Folium  
• Streamlit  

---

## 📌 Project Status

This system is an **experimental research prototype** developed to explore  
INSAT-3D based cloud-structure analysis for **early situational awareness**.

It is **not an operational weather forecasting or official early-warning system**.

---

## ⚠ Scope & Limitations

• Does not predict rainfall amounts or cyclone landfall  
• Does not replace official forecasts or warning agencies  
• Region labeling is approximate and based on latitude–longitude bounds  
• Results are intended for **research and exploratory use only**

---

## 🔮 Future Scope

• Multi-timestamp cloud tracking  
• Time-series analysis of cloud evolution  
• Automated MOSDAC data ingestion  
• Validation against historical extreme weather events  

---

## ⚠ Disclaimer

This project is an **academic and exploratory research prototype**.  
It is not intended for operational forecasting, certified warnings,  
or public safety advisories.

---

## 👨‍💻 Author

**Developed by:**-  **Deepanshu Maheshwari**  
Applied AI | Satellite Data | Weather Intelligence  

---

## 🙌 Acknowledgements

Satellite Data Source — ISRO / MOSDAC  
Satellite Platform — INSAT-3D Imager
