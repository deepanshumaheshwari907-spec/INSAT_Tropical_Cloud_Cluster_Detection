import numpy as np
from geo_utils import haversine_km


def compute_tcc_features(region, Tb, lat, lon):

    # Pixels belonging to this cluster
    coords = region.coords

    # Brightness temperature values for cluster pixels
    t_vals = Tb[coords[:, 0], coords[:, 1]]

    # Region centroid (row, col in grid)
    center_row, center_col = region.centroid
    center_row = int(center_row)
    center_col = int(center_col)

    # Try reading lat-lon at centroid
    center_lat = lat[center_row, center_col]
    center_lon = lon[center_row, center_col]

    # If centroid falls in invalid projection area → pick first valid pixel
    if np.isnan(center_lat) or np.isnan(center_lon):
        for (r, c) in coords:
            if not np.isnan(lat[r, c]) and not np.isnan(lon[r, c]):
                center_lat = lat[r, c]
                center_lon = lon[r, c]
                break

    # Compute distance of every pixel from center (in km)
    distances = []

    for (r, c) in coords:
            if not np.isnan(lat[r, c]) and not np.isnan(lon[r, c]):
                d = haversine_km(
                    center_lat, center_lon,
                    lat[r, c], lon[r, c]
                )
                distances.append(d)

    distances = np.array(distances)

    # Build feature dictionary
    return {
        "pixel_count": float(region.area),

        "mean_tb": float(np.mean(t_vals)),
        "min_tb": float(np.min(t_vals)),
        "median_tb": float(np.median(t_vals)),
        "std_tb": float(np.std(t_vals)),

        "center_lat": float(center_lat),
        "center_lon": float(center_lon),

        "min_radius_km": float(np.min(distances)) if len(distances) else 0.0,
        "max_radius_km": float(np.max(distances)) if len(distances) else 0.0,
        "mean_radius_km": float(np.mean(distances)) if len(distances) else 0.0,
    }
