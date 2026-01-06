import csv
from insat_reader import load_tb_lat_lon
from thresholding import apply_irbt_threshold
from cluster_detect import detect_cloud_clusters
from tcc_filter import is_valid_tcc
from tcc_features import compute_tcc_features

print("Loading INSAT data...")
Tb, lat, lon = load_tb_lat_lon()

print("Applying threshold...")
mask = apply_irbt_threshold(Tb)

print("Detecting clusters...")
labeled, regions = detect_cloud_clusters(mask)

rows = []

print("Processing TCC features...")

for r in regions:

    if not is_valid_tcc(r):
        continue

    feat = compute_tcc_features(r, Tb, lat, lon)

    rows.append(feat)

print("\nTotal valid TCCs saved:", len(rows))

# ---- WRITE CSV FILE ----
with open("tcc_results.csv", "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print("\nCSV export complete:  tcc_results.csv")
