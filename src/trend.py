def classify_trend(min_tb, mean_tb, mean_radius_km):
    """
    Determines temporal behaviour of a Tropical Cloud Cluster
    using thermodynamic and spatial indicators.
    """

    if min_tb < 210 and mean_radius_km > 600:
        return "Intensifying"
    elif mean_tb < 225:
        return "Stable"
    else:
        return "Weakening"
