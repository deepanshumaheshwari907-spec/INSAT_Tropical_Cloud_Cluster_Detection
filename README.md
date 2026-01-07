# INSAT-3D Tropical Cloud Cluster (TCC) Detection System

This project detects and analyzes **Tropical Cloud Clusters (TCC)** using  
INSAT-3D Infrared Brightness Temperature (IRBT) satellite observations.

The system identifies cold convective cloud regions, validates TCC structures,
computes their scientific characteristics, and visualizes them on an interactive map.


---

## 🎯 Project Objective

The primary objectives of this project are:

• Detect Tropical Cloud Clusters (TCC) from INSAT-3D satellite imagery  
• Apply IRBT thresholding to identify deep convective clouds  
• Compute geometric and physical characteristics of TCC  
• Provide scientific as well as human-interpretable insights  
• Assist in tropical weather & convective system analysis  


---

## 🛰 Satellite Dataset

Source : **MOSDAC / ISRO**  
Sensor : **INSAT-3D Imager**  
Product Type : **Level-1C (SGP)**  
Channel Used : **IR (Brightness Temperature)**  
Temporal Resolution : **30 Minutes**

Input Format Supported : **.h5 Satellite File (User Uploads in App)**


---

## ⚙️ Processing Workflow (Pipeline)

1️⃣ Load INSAT-3D L1C IRBT satellite data  
2️⃣ Convert raw image counts → Brightness Temperature  
3️⃣ Apply cold-cloud IR threshold  
4️⃣ Detect connected convective cloud clusters  
5️⃣ Validate TCC based on

• Minimum spatial extent  
• Independent circular cloud structure  

6️⃣ Compute TCC features

• Pixel count  
• Mean / Minimum / Median Tb  
• Temperature standard deviation  
• Geographical center (Lat-Lon)  
• Minimum / Maximum / Mean radius (km)

7️⃣ Generate outputs

✔ Scientific feature table  
✔ AI-generated human readable summary  
✔ Interactive geo-map visualization


---

## 🧪 Output Parameters (Per Detected Cluster)

The system provides the following parameters:

• Convective center latitude  
• Convective center longitude  
• Pixel count (cluster coverage)  
• Mean Brightness Temperature  
• Minimum Brightness Temperature  
• Median Tb  
• Standard deviation Tb  
• Minimum radius  
• Maximum radius  
• Mean radius  
• Cloud-top convective intensity indicator  


---

## 💻 Technologies Used

• Python  
• NumPy  
• Pandas  
• h5py  
• Scikit-Image  
• Folium / Leaflet  
• Streamlit (Web Interface)


---

## 📊 Application Features

✔ Automatic TCC Detection from Satellite Data  
✔ Adjustable IRBT Threshold  
✔ Cluster-wise Feature Extraction  
✔ Scientific Output Table  
✔ Human-Readable AI Summary  
✔ Geo-Referenced Cluster Visualization  
✔ Download Results Option  


---

## 📌 Use-Case & Significance

This project can support:

• Tropical weather system monitoring  
• Convective cloud structure studies  
• Pre-cyclogenesis cloud analysis  
• Monsoon convective activity research  
• Academic & research-based satellite studies  


---

## 🚀 Future Enhancements (Planned)

• Multi-scene batch processing  
• Time-series TCC motion tracking  
• Cloud lifecycle evolution analysis  
• Automatic MOSDAC data ingestion  
• Cyclone precursor detection support  
• Real-time monitoring dashboard  


---

## 📌 Project Status

The system is currently in a **working and stable stage**.

Real INSAT-3D satellite data has been successfully processed to:

• Detect Tropical Cloud Clusters  
• Filter valid convective structures  
• Compute scientifically meaningful parameters  
• Present results using an interactive web-based dashboard  


---

## 👨‍🎓 Academic Project Note

This work is developed as an academic research-oriented project and demonstrates:

• Satellite data preprocessing  
• Remote sensing-based feature extraction  
• Convective cloud characterization  
• Python-based scientific computing  
• Weather-research application development  


---

## 🙌 Credits

Satellite Data Source — **ISRO / MOSDAC**  
Platform — **INSAT-3D Imager**

Project Development — **Student Research Work**

