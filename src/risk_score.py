def clamp(x, low=0, high=100):
    return max(low, min(high, x))


def compute_risk_score(min_tb, mean_radius_km):
    """
    Computes a continuous risk score (0–100) for a Tropical Cloud Cluster
    based on cloud-top temperature and spatial size.
    """

    # Temperature-based risk (colder cloud tops are more intense)
    tb_score = (235 - min_tb) / (235 - 190) * 100
    tb_score = clamp(tb_score)

    # Size-based risk (larger clusters are more dangerous)
    size_score = (mean_radius_km / 1200) * 100

    # Weighted final risk score
    risk_score = 0.6 * tb_score + 0.4 * size_score

    return round(risk_score, 1)


def risk_level_from_score(risk_score):
    if risk_score >= 85:
        return "Extreme"
    elif risk_score >= 60:
        return "High"
    elif risk_score >= 30:
        return "Medium"
    else:
        return "Low"
