from insat_reader import load_tb_lat_lon
from thresholding import apply_irbt_threshold
from cluster_detect import detect_cloud_clusters
from tcc_filter import is_valid_tcc
from tcc_features import compute_tcc_features
from summary_generator import generate_tcc_summary


print("Loading real INSAT Tb...")
Tb, lat, lon = load_tb_lat_lon()

print("Applying threshold...")
mask = apply_irbt_threshold(Tb)

print("Detecting clusters...")
labeled, regions = detect_cloud_clusters(mask)

print("Validating TCCs...")
valid = []

for r in regions:
    if is_valid_tcc(r):
        features = compute_tcc_features(r, Tb, lat, lon)

        valid.append(features)

print("\nTotal clusters detected:", len(regions))
print("Valid TCC systems:", len(valid))

for t in valid[:5]:

    print("\nTCC FOUND")
    for k,v in t.items():
        print(k,":",v)

    # ---- Generate Human Summary ----
    summary = generate_tcc_summary(t)
    print("summary :", summary)

