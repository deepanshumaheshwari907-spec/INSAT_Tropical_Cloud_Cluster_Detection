# INSAT-3D Tropical Cloud Cluster (TCC) Detection System

This project identifies Tropical Cloud Clusters (TCC) using 
INSAT-3D Infrared Brightness Temperature (IRBT) satellite data.

The system detects cold convective cloud regions, filters valid TCCs,
computes their scientific features, and visualizes them on a geo-map.

Live App:
<your streamlit link here>

---

## 🌍 Objective

• Detect Tropical Cloud Clusters (TCC)  
• Apply IRBT thresholding on INSAT-3D IR data  
• Compute size, intensity & cloud-top statistics  
• Track convective structure shape and spread  
• Provide scientific + human readable summary  

---

## 🛰 Dataset Used

Source : MOSDAC / ISRO  
Sensor : INSAT-3D Imager  
Product : L1C SGP  
Resolution : Half-Hourly IR Observation  

User uploads `.h5` file in app.

---

## ⚙️ Processing Pipeline

1️⃣ Load INSAT IRBT data  
2️⃣ Convert raw counts → Brightness Temperature  
3️⃣ Apply cold-cloud IR threshold  
4️⃣ Detect connected convective clusters  
5️⃣ Validate TCC based on
   • Minimum size  
   • Circularity / Independence  
6️⃣ Compute features
   • Pixel count  
   • Mean / Min / Median Tb  
   • Std deviation  
   • Center lat-lon  
   • Min / Max / Mean radius (km)  
7️⃣ Show outputs as

✔ Scientific table  
✔ Human-readable summary  
✔ Geo-map visualization  

---

## 📌 Technologies Used

• Python  
• NumPy, Pandas  
• h5py  
• Scikit-Image  
• Folium / Leaflet  
• Streamlit Web App  

---

## 🧪 Output Parameters (As per project requirement)

• Convective center latitude & longitude  
• Pixel count  
• Mean Tb  
• Minimum Tb  
• Median Tb  
• Standard deviation Tb  
• Min / Max / Mean radius  
• Cloud-top intensity indicators  

---

## 🚀 Future Scope

• Time-series TCC tracking  
• Movement & evolution analysis  
• Cyclogenesis precursor study  
• Near-real-time automation  
