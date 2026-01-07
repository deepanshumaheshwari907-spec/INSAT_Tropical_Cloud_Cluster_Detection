INSAT-3D Tropical Cloud Cluster (TCC) Detection System

This project focuses on the detection and analysis of Tropical Cloud Clusters (TCC) using INSAT-3D Infrared Brightness Temperature (IRBT) satellite observations.

The system identifies cold convective cloud regions, validates TCC structures, computes their scientific characteristics, and visualizes them through an interactive map-based dashboard.

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

Input Format : .h5 satellite file (uploaded through the application)

⚙️ Processing Workflow

The system follows the below processing pipeline:

1️⃣ Load INSAT-3D L1C IRBT satellite data
2️⃣ Convert raw sensor counts to Brightness Temperature
3️⃣ Apply cold-cloud temperature threshold
4️⃣ Detect connected convective cloud regions
5️⃣ Validate Tropical Cloud Clusters based on:

• Minimum spatial coverage
• Cluster independence and structural shape

6️⃣ Compute TCC-specific features such as:

• Pixel count
• Mean / Minimum / Median Tb
• Temperature standard deviation
• Geographic center (Latitude–Longitude)
• Minimum / Maximum / Mean radius (km)

7️⃣ Present outputs through:

✔ Scientific feature table
✔ Human-readable descriptive summary
✔ Interactive geo-map visualization

🧪 Output Parameters

For every detected TCC, the system provides:

• Cluster center latitude
• Cluster center longitude
• Pixel count / spatial coverage
• Mean brightness temperature
• Minimum and median Tb
• Standard deviation of Tb
• Minimum, maximum and mean radius
• Indicators of convective cloud-top intensity

💻 Tools & Technologies Used

• Python
• NumPy & Pandas
• h5py
• Scikit-Image
• Folium / Leaflet
• Streamlit (Web Application Framework)

📊 Application Capabilities

✔ Automatic detection of TCC from satellite data
✔ Adjustable IRBT threshold
✔ Cluster-wise feature extraction
✔ Scientific and tabular output
✔ Human-interpretable AI-based summary
✔ Geo-referenced visualization on map
✔ Option to download detection results

📌 Relevance & Use-Cases

This project can support:

• Tropical weather system monitoring
• Convective cloud structure research
• Pre-cyclogenesis cloud assessment
• Monsoon convection analysis
• Academic and satellite-data research studies

🚀 Future Enhancements (Planned)

• Multi-scene and batch processing
• Time-series tracking of TCC movement
• Cloud lifecycle and evolution study
• Automated data ingestion from MOSDAC
• Cyclogenesis precursor investigation
• Real-time monitoring dashboard

📌 Current Project Status

The system is presently in a working and stable stage.

Real INSAT-3D satellite data has been successfully processed to:

• Detect convective cloud clusters
• Filter valid TCC structures
• Compute physically meaningful parameters
• Present results using an interactive Streamlit dashboard

👨‍🎓 Academic Note

This project has been developed as part of an academic research-oriented work and demonstrates:

• Satellite data preprocessing
• Remote-sensing-based feature extraction
• Convective cloud characterization
• Python-based scientific computing
• Weather research application development

🙌 Acknowledgements

Satellite Data Source — ISRO / MOSDAC
Satellite Platform — INSAT-3D Imager

Developed as part of student research work
