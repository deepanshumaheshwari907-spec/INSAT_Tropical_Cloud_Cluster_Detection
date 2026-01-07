INSAT-3D Tropical Cloud Cluster (TCC) Detection System

This project focuses on the detection and analysis of Tropical Cloud Clusters (TCC) using
INSAT-3D Infrared Brightness Temperature (IRBT) satellite observations.

The application identifies cold convective cloud regions, filters valid TCC structures,
computes their scientific characteristics, and visualizes them through an interactive map-based dashboard.

🎯 Project Overview

The project has been developed with the following objectives:

• Detect Tropical Cloud Clusters from INSAT-3D satellite imagery
• Apply IRBT-based thresholding to identify deep convective clouds
• Extract geometric and statistical properties of TCC systems
• Provide both scientific metrics and easy-to-understand interpretations
• Support research in tropical weather and convective cloud analysis

🛰 Satellite Data Details

Source : MOSDAC / ISRO
Satellite : INSAT-3D
Sensor : Imager
Product Type : L1C – SGP
Channel Used : Infrared (Brightness Temperature)
Temporal Resolution : 30-minute interval

Input Format : .h5 satellite file (uploaded through the app)

⚙️ Processing Workflow

The end-to-end workflow followed in this system is:

1️⃣ Load INSAT-3D L1C IRBT satellite data
2️⃣ Convert raw sensor counts to Brightness Temperature
3️⃣ Apply cold-cloud temperature threshold
4️⃣ Detect connected convective cloud regions
5️⃣ Validate Tropical Cloud Clusters based on:

• Minimum spatial coverage
• Cluster independence and structure shape

6️⃣ Compute TCC-specific features including:

• Pixel count
• Mean, Minimum and Median Tb
• Temperature variability (Std. deviation)
• Geographic center (Latitude–Longitude)
• Minimum / Maximum / Mean radius (km)

7️⃣ Present results through:

✔ Scientific feature table
✔ Human-readable descriptive summary
✔ Interactive geo-map visualization

🧪 Output Parameters

For every detected TCC, the system provides:

• Cluster center latitude & longitude
• Pixel count / cluster coverage
• Mean brightness temperature
• Minimum and median Tb
• Temperature standard deviation
• Minimum, maximum and mean radius
• Indicators of convective cloud-top intensity

💻 Tools & Technologies

• Python
• NumPy & Pandas
• h5py
• Scikit-Image
• Folium / Leaflet
• Streamlit (Web Application)

📊 Application Capabilities

✔ Automatic detection of TCC from satellite data
✔ Adjustable IRBT threshold
✔ Cluster-wise feature extraction
✔ Scientific & tabular output
✔ Human-interpretable AI summary
✔ Geo-referenced visualization on map
✔ Option to download detection results

📌 Relevance & Use-Cases

This work can support research and analysis in:

• Tropical weather monitoring
• Convective cloud structure studies
• Pre-cyclogenesis cloud assessment
• Monsoon convective system analysis
• Academic & satellite-data research applications

🚀 Planned Future Improvements

• Multi-scene / batch-level processing
• Time-series tracking of TCC movement
• Cloud lifecycle and evolution study
• Automated data ingestion from MOSDAC
• Cyclogenesis precursor investigation
• Real-time monitoring dashboard

📌 Current Project Status

The system is in a working and stable stage.

It successfully processes real INSAT-3D satellite data to:

• Detect convective cloud clusters
• Filter valid TCC structures
• Compute relevant physical and geometric parameters
• Present results through an interactive Streamlit dashboard

👨‍🎓 Academic Note

This project has been developed as part of an academic research initiative, demonstrating:

• Satellite data preprocessing
• Remote-sensing based feature extraction
• Convective cloud characterization
• Python-based scientific analysis
• Weather-research application development

🙌 Acknowledgements

Satellite Data — ISRO / MOSDAC
Platform — INSAT-3D Imager

Developed as part of student research work
