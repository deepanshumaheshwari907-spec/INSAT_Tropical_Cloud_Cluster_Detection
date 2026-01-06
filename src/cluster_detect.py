import numpy as np
from skimage.measure import label, regionprops

def detect_cloud_clusters(mask):
    """
    mask = binary cloud mask
    returns:
      labeled_image -> matrix with cluster ID
      regions -> list of cloud cluster objects
    """

    labeled_image = label(mask, connectivity=2)

    regions = regionprops(labeled_image)

    return labeled_image, regions



"""if __name__ == "__main__":
    from data_loader import load_sample_irbt
    from thresholding import apply_irbt_threshold

    Tb, lat, lon = load_sample_irbt()

    mask = apply_irbt_threshold(Tb)

    labeled_image, regions = detect_cloud_clusters(mask)

    print("Total Cloud Clusters Found:", len(regions))

    for i, r in enumerate(regions[:5]):
        print(f"Cluster {i+1} pixel count:", r.area)
    from tcc_filter import is_valid_tcc

valid_clusters = []

for r in regions:
    if is_valid_tcc(r):
        valid_clusters.append(r)

print("\nValid TCCs Detected:", len(valid_clusters))
from tcc_filter import is_valid_tcc
from tcc_features import compute_tcc_features
valid_clusters = []

for r in regions:
    if is_valid_tcc(r):
        features = compute_tcc_features(r, Tb, lat, lon)
        valid_clusters.append(features)

print("\nValid TCCs Detected:", len(valid_clusters))

for t in valid_clusters:
    print("\nTCC Found:")
    for k,v in t.items():
        print(k,":",v)"""

