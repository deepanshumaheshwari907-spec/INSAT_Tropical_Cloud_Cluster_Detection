import numpy as np
from math import sqrt, pi

def is_valid_tcc(region, pixel_km2 = 4):
    """
    region = cluster object
    pixel_km2 = approx km2 per pixel (temporary assumption)

    returns True if passes TCC criteria
    """

    pixel_count = region.area

    area_km2 = pixel_count * pixel_km2

    # Equivalent circular radius (R = sqrt(A/pi))
    radius_km = sqrt(area_km2 / pi)

    # Convert km to degrees approx
    radius_deg = radius_km / 111

    if radius_deg < 1:
        return False

    if area_km2 < 34800:
        return False

    return True
